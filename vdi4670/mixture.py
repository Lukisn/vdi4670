#!/usr/bin/env python
"""mixture module."""

from math import log

from . import ureg, Q_
from .constants import MolarMass, R_m, components, T_0, p_0
from .coefficients import A, B, C, D

a = A()
b = B()
c = C()
d = D()


class Mixture:
    """Mixture class."""

    def __init__(self, n2=0., o2=0., ar=0., ne=0., h2o=0., co2=0., co=0., so2=0.):
        """Initialize mixture from mole fractions."""
        x = n2 + o2 + ar + ne + h2o + co2 + co + so2
        if x != 1:
            raise ValueError("mole fractions should sum up to a total of 1!")
        self.x = {
            "n2": n2,
            "o2": o2,
            "ar": ar,
            "ne": ne,
            "h2o": h2o,
            "co2": co2,
            "co": co,
            "so2": so2,
        }

    @classmethod
    def air(cls):
        """Initialize the standard mixture for air according to ISO 2533."""
        return cls(n2=0.781109, o2=0.209548, ar=0.009343)

    @classmethod
    def test_gas(cls):
        """Initialize the test gas mixture according to VDI 4670-1."""
        return cls(n2=0.6, o2=0.1, ar=0.01, h2o=0.17, co2=0.1, co=0.01, so2=0.01)

    def molar_mass(self):
        """Calculate the molar mass of the mixture (M_mix).

        M_mix = sum_k=1..K(x_k * M_k)  - formula (3)
        """
        return MolarMass.from_mole_fractions(
            n2=self.x["n2"],
            o2=self.x["o2"],
            ar=self.x["ar"],
            ne=self.x["ne"],
            h2o=self.x["h2o"],
            co2=self.x["co2"],
            co=self.x["co"],
            so2=self.x["o2"]
        )

    def specific_gas_constant(self):
        """Calculate the specific gas constant of the mixture (R_mix).

        R_mix = R_m / M_mix  - formula (7)
        """
        M_mix = self.molar_mass()
        return R_m / M_mix

    @staticmethod
    def molar_density(pressure, temperature):
        """Calculate the molar density of the mixture (rho_m) in mol/m3.

        This value is independent of the composition of the mixture.

        rho_m = p / (R_m * T)  - formula (8)
        """
        p, T = pressure, temperature
        rho_m = p / (R_m * T)
        rho_m.ito(ureg.mol / ureg.meter ** 3)
        return rho_m

    def density(self, pressure, temperature):
        """Calculate the mass density of the mixture (rho_mix) in kg/m3.

        rho_mix = p / (R_mix T) = p M_mix / (R_m T)  - formula (9)
        """
        p, T = pressure, temperature
        M_mix = self.molar_mass()
        rho_mix = p * M_mix / (R_m * T)
        rho_mix.ito(ureg.kilogram / ureg.meter ** 3)
        return rho_mix

    def molar_heat_capacity(self, temperature):
        """Calculate the isobaric heat capacity of the mixture (c_p,m,mix) in J/(mol.K).

        c_p,m,mix(T,x) = sum_k=1..K(x_k * c_p,m,k(T))  - formula (11)
        c_p,m,k(T) = sum_i=1..10(a_k,i * (T / T_0) ** b_i)  - formula (10)
        """
        T = temperature
        c_pmmix = Q_(0, ureg.joule / (ureg.mol * ureg.kelvin))
        for k in components:
            c_pmk = Q_(0, ureg.joule / (ureg.mol * ureg.kelvin))
            for i in range(1, 11):
                term = a[k, i] * (T / T_0) ** b[i]
                c_pmk += term
            c_pmmix += self.x[k] * c_pmk
        c_pmmix.ito(ureg.joule / (ureg.mol * ureg.kelvin))
        return c_pmmix

    def heat_capacity(self, temperature):
        """Calculate the specific isobaric heat capacity of the mixture (c_p,mix) in J/(kg.K).

        c_p,mix = c_p,m,mix(T,x) / M_mix  - formula (13)
        """
        c_pmmix = self.molar_heat_capacity(temperature)
        M_mix = self.molar_mass()
        c_pmix = c_pmmix / M_mix
        c_pmix.ito(ureg.joule / ureg.meter ** 3 / ureg.kelvin)
        return c_pmix

    def molar_enthalpy(self, temp):
        """Calculate the molar enthalpy of the mixture (h_m,mix) in J/mol.

        h_m,mix(T,x) = sum_k=1..K(x_k * h_m,k(T))  - formula (15)
        h_m,k(T) = c_k,0 + sum_i=1..10(c_k,i * (T / T_0) ** (b_i + 1))  - formula (14)
        """
        unit = ureg.joule / ureg.mol
        h_mmix = Q_(0, unit)
        for k in components:
            h_mk = c[k, 0]
            for i in range(1, 11):
                term = c[k, i] * (temp / T_0) ** (b[i] + 1)
                h_mk += term
            h_mmix += self.x[k] * h_mk
        h_mmix.ito(unit)
        return h_mmix

    def enthalpy(self, temp):
        """Calculate the specific enthalpy of the mixture (h_mix) in J/kg.

        h_mix = h_m,mix / M_mix  - formula (17)
        """
        h_mmix = self.molar_enthalpy(temp)
        M_mix = self.molar_mass()
        h_mix = h_mmix / M_mix
        h_mix.ito(ureg.joule / ureg.kilogram)

    def molar_entropy(self, t, p):
        """Calculate the molar entropy of the mixture in J/(mol.K).

        s_m,mix(T,p,x) = sum_k=1..K(x_k * s_m,k(T,p))
                         - R_m * sum_k=1..K(x_k * ln(x_k))  - formula (19)
        s_m,k(T,p) = d_k,0 + d_k,1 * ln(T / T0) - R_m * ln(p / p_0)
                     + sum_i=2..10(d_k,i * (T / T_0) ** b_i)  - formula (18)
        """
        unit = ureg.joule / (ureg.mol * ureg.kelvin)
        s_mmix = Q_(0, unit)
        sum1 = Q_(0, unit)
        sum2 = Q_(0, unit)
        for k in components:
            s_mk = d[k, 0] + d[k, 1] * log(t / T_0) - R_m * log(p / p_0)
            for i in range(2, 11):
                s_mk += d[k, i] * (t / T_0) ** b[i]
            sum1 += self.x[k] * s_mk
            sum2 += self.x[k] * log(self.x[k])
        s_mmix = sum1 - R_m * sum2
        s_mmix.ito(unit)
        return s_mmix

    def entropy(self, t, p):
        """Calculate the specific entropy of the mixture in J/(kg.K).

        s_mix = s_m,mix / M_mix  - formula (21)
        """
        s_mmix = self.molar_entropy(t, p)
        M_mix = self.molar_mass()
        s_mix = s_mmix / M_mix
        s_mix.ito(ureg.joule / (ureg.kilogram * ureg.kelvin))
        return s_mix
