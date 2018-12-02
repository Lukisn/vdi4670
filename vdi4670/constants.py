#!/usr/bin/env python
"""constants module."""

from . import ureg, Q_

reference_temperature = T_0 = Q_(273.15, ureg.kelvin)  # [K]
reference_pressure = p_0 = Q_(0.101325, ureg.megapascal)  # [MPa]

lower_temperature_limit = T_min = Q_(200, ureg.kelvin)  # [K]
upper_temperature_limit = T_max = Q_(3300, ureg.kelvin)  # [K]
temperature_range = (lower_temperature_limit, upper_temperature_limit)

universal_gas_constant = R_m = Q_(8.314472, ureg.joule / (ureg.mol * ureg.kelvin))  # [J/mol/K]

components = {"n2", "o2", "ar", "ne", "h2o", "co2", "co", "so2"}


class MolarMass:
    """Molar masses for components and mixtures in kg/mol."""

    n2 = Q_(8.01348e-3, ureg.kg / ureg.mol)
    o2 = Q_(31.9988e-3, ureg.kg / ureg.mol)
    ar = Q_(39.938e-3, ureg.kg / ureg.mol)
    ne = Q_(20.1797e-3, ureg.kg / ureg.mol)
    h2o = Q_(18.01528e-3, ureg.kg / ureg.mol)
    co2 = Q_(44.0095e-3, ureg.kg / ureg.mol)
    co = Q_(28.0101e-3, ureg.kg / ureg.mol)
    so2 = Q_(64.0648e-3, ureg.kg / ureg.mol)

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
