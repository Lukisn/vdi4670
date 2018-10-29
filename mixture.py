#!/usr/bin/env python
"""mixture module."""

import pint

ureg = pint.UnitRegistry()


reference_temperature = 273.15  # T_0 [K]
reference_pressure = 0.101325  # p_0 [MPa]

lower_temperature_limit = 200  # [K]
upper_temperature_limit = 3300  # [K]
temperature_range = (lower_temperature_limit, upper_temperature_limit)

components = {"N2", "O2", "Ar", "Ne", "H2O", "CO2", "CO", "SO2"}


class MolarMass:  # [kg/mol]
    N2 = 28.01348e-3
    O2 = 31.9988e-3
    Ar = 39.938e-3
    Ne = 20.1797e-3
    H2O = 18.01528e-3
    CO2 = 44.0095e-3
    CO = 28.0101e-3
    SO2 = 64.0648e-3

    @staticmethod
    def from_mole_fractions(n2=0, o2=0, ar=0, ne=0, h2o=0, co2=0, co=0, so2=0):
        sum = n2 * MolarMass.N2
        sum += o2 * MolarMass.O2
        sum += ar * MolarMass.Ar
        sum += ne * MolarMass.Ne
        sum += h2o * MolarMass.H2O
        sum += co2 * MolarMass.CO2
        sum += co * MolarMass.CO
        sum += so2 * MolarMass.SO2
        return sum

    @staticmethod
    def from_mass_fractions(n2=0, o2=0, ar=0, ne=0, h2o=0, co2=0, co=0, so2=0):
        sum = n2 / MolarMass.N2
        sum += o2 / MolarMass.O2
        sum += ar / MolarMass.Ar
        sum += ne / MolarMass.Ne
        sum += h2o / MolarMass.H2O
        sum += co2 / MolarMass.CO2
        sum += co / MolarMass.CO
        sum += so2 / MolarMass.SO2
        result = 1 / sum
        return result


class Mixture:
    """Mixture class."""

    universal_gas_constant = 8.314472  # R_m [J/mol/K]
    # TODO: add coefficients

    def __init__(self, n2=0, o2=0, ar=0, ne=0, h2o=0, co2=0, co=0, so2=0):
        x = n2 + o2 + ar + ne + h2o + co2 + co + so2
        if x != 1:
            raise ValueError("mole fractions should sum up to a total of 1!")
        self._x_N2 = n2
        self._x_O2 = o2
        self._x_Ar = ar
        self._x_Ne = ne
        self._x_H2O = h2o
        self._x_CO2 = co2
        self._x_CO = co
        self._x_SO2 = so2

    def from_mass_fraction(self, n2=0, o2=0, ar=0, ne=0, h2o=0, co2=0, co=0, so2=0):
        xi = n2 + o2 + ar + ne + h2o + co2 + co + so2
        if xi != 1:
            raise ValueError("mass fractions should sum up to a total of 1!")
        M_mix = MolarMass.from_mass_fractions(n2, o2, ar, ne, h2o, co2, co, so2)
        self._x_N2 = n2 * M_mix / MolarMass.N2
        self._x_O2 = o2 * M_mix / MolarMass.O2
        self._x_Ar = ar * M_mix / MolarMass.Ar
        self._x_Ne = ne * M_mix / MolarMass.Ne
        self._x_H2O = h2o * M_mix / MolarMass.H2O
        self._x_CO2 = co2 * M_mix / MolarMass.CO2
        self._x_CO = co * M_mix / MolarMass.CO
        self._x_SO2 = so2 * M_mix / MolarMass.SO2

    def molar_mass(self):
        return MolarMass.from_mole_fractions(
            n2=self._x_N2,
            o2=self._x_O2,
            ar=self._x_Ar,
            ne=self._x_Ne,
            h2o=self._x_H2O,
            co2=self._x_CO2,
            co=self._x_CO,
            so2=self._x_SO2
        )
