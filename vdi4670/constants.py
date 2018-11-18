#!/usr/bin/env python
"""constants module."""

reference_temperature = T_0 = 273.15  # [K]
reference_pressure = p_0 = 0.101325  # [MPa]

lower_temperature_limit = T_min = 200  # [K]
upper_temperature_limit = T_max = 3300  # [K]
temperature_range = (lower_temperature_limit, upper_temperature_limit)

universal_gas_constant = R_m = 8.314472  # [J/mol/K]

components = {"N2", "O2", "Ar", "Ne", "H2O", "CO2", "CO", "SO2"}


class MolarMass:
    """Molar masses for components and mixtures in kg/mol."""

    n2 = 28.01348e-3
    o2 = 31.9988e-3
    ar = 39.938e-3
    ne = 20.1797e-3
    h2o = 18.01528e-3
    co2 = 44.0095e-3
    co = 28.0101e-3
    so2 = 64.0648e-3

    @staticmethod
    def from_mole_fractions(n2=0, o2=0, ar=0, ne=0, h2o=0, co2=0, co=0, so2=0):
        """Calculate the molar mass for the given mixture in mole fractions."""
        total = n2 * MolarMass.n2
        total += o2 * MolarMass.o2
        total += ar * MolarMass.ar
        total += ne * MolarMass.ne
        total += h2o * MolarMass.h2o
        total += co2 * MolarMass.co2
        total += co * MolarMass.co
        total += so2 * MolarMass.so2
        return total

    @staticmethod
    def from_mass_fractions(n2=0, o2=0, ar=0, ne=0, h2o=0, co2=0, co=0, so2=0):
        """Calculate the molar mass for the given mixture in mass fractions."""
        total = n2 / MolarMass.n2
        total += o2 / MolarMass.o2
        total += ar / MolarMass.ar
        total += ne / MolarMass.ne
        total += h2o / MolarMass.h2o
        total += co2 / MolarMass.co2
        total += co / MolarMass.co
        total += so2 / MolarMass.so2
        result = 1 / total
        return result
