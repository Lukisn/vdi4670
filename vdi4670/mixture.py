#!/usr/bin/env python
"""mixture module."""

from . import ureg, Q_
from .constants import MolarMass, R_m, components, T_0
from .coefficients import A, B

a = A()
b = B()


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
        """Calculate the molar mass of the mixture (M_mix)."""
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
        """Calculate the specific gas constant of the mixture (R_mix)."""
        M_mix = self.molar_mass()
        return R_m / M_mix

    @staticmethod
    def molar_density(pressure, temperature):
        """Calculate the molar density of the mixture in mol/m3 (rho_m).

        This value is independent of the composition of the mixture.

        rho_m = p / (R_m T)
        """
        p, T = pressure, temperature
        rho_m = p / (R_m * T)
        rho_m.ito(ureg.mol / ureg.meter ** 3)
        return rho_m

    def density(self, pressure, temperature):
        """Calculate the mass density of the mixture in kg/m3 (rho_mix).

        rho_mix = p / (R_mix T) = p M_mix / (R_m T)
        """
        p, T = pressure, temperature
        M_mix = self.molar_mass()
        rho_mix = p * M_mix / (R_m * T)
        rho_mix.ito(ureg.kilogram / ureg.meter ** 3)
        return rho_mix

    def molar_heat_capacity(self, temperature):
        """Calculate the isobaric heat capacity of the mixture in J/mol/K (c_p,m,mix)."""
        T = temperature
        c_pmmix = Q_(0, ureg.joule / ureg.mol / ureg.kelvin)
        for k in components:
            c_pmk = Q_(0, ureg.joule / ureg.mol / ureg.kelvin)
            for i in range(1, 11):
                term = a[k, i] * (T / T_0) ** b[i]
                c_pmk += term
            c_pmmix += self.x[k] * c_pmk
        c_pmmix.ito(ureg.joule / ureg.mol / ureg.kelvin)
        return c_pmmix

    def heat_capacity(self, temperature):
        """Calculate the specific isobaric heat capacity of the mixture in J/kg/K (c_p,mix)."""
        c_pmmix = self.molar_heat_capacity(temperature)
        M_mix = self.molar_mass()
        c_pmix = c_pmmix / M_mix
        c_pmix.ito(ureg.joule / ureg.meter ** 3 / ureg.kelvin)
        return c_pmix

    # TODO: implement default calculation procedures for non-dissociated mixtures.
    def molar_enthalpy(self, temperature):
        """Calculate the molar enthalpy of the mixture in J/mol."""
        raise NotImplementedError

    def enthalpy(self, temperature):
        """Calculate the specific enthalpy of the mixture in J/kg."""
        raise NotImplementedError

    def molar_entropy(self, temperature):
        """Calculate the molar entropy of the mixture in J/mol/K."""
        raise NotImplementedError

    def entropy(self, temperature):
        """Calculate the specific entropy of the mixture in J/kg/K."""
        raise NotImplementedError
