#!/usr/bin/env python
"""constants module."""

reference_temperature = T_0 = 273.15  # [K]
reference_pressure = p_0 = 0.101325  # [MPa]

lower_temperature_limit = T_min = 200  # [K]
upper_temperature_limit = T_max = 3300  # [K]
temperature_range = (lower_temperature_limit, upper_temperature_limit)

universal_gas_constant = R_m = 8.314472  # [J/mol/K]

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

