#!/usr/bin/env python
"""constants module."""

from . import ureg, Q_

reference_temperature = T_0 = Q_(273.15, ureg.kelvin)
reference_pressure = p_0 = Q_(0.101325, ureg.megapascal)

lower_temperature_limit = T_min = Q_(200, ureg.kelvin)
upper_temperature_limit = T_max = Q_(3300, ureg.kelvin)
temperature_range = (lower_temperature_limit, upper_temperature_limit)

universal_gas_constant = R_m = Q_(8.314472, ureg.joule / (ureg.mol * ureg.kelvin))

components = {
    "n2",  # Nitrogen
    "o2",  # Oxygen
    "ar",  # Argon
    "ne",  # Neon
    "h2o",  # Water
    "co2",  # Carbon dioxide
    "co",  # Carbon monoxide
    "so2",  # Sulphur dioxide
}


class MolarMass:
    """Molar masses for components and mixtures in kg/mol. (from table 1)"""

    unit = ureg.kilogram / ureg.mol

    n2 = Q_(28.01348e-3, unit)
    o2 = Q_(31.9988e-3, unit)
    ar = Q_(39.938e-3, unit)
    ne = Q_(20.1797e-3, unit)
    h2o = Q_(18.01528e-3, unit)
    co2 = Q_(44.0095e-3, unit)
    co = Q_(28.0101e-3, unit)
    so2 = Q_(64.0648e-3, unit)

    @staticmethod
    def from_mole_fractions(n2=0, o2=0, ar=0, ne=0, h2o=0, co2=0, co=0, so2=0):
        """Calculate the molar mass for the given mixture in mole fractions in kg/mol."""
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
        """Calculate the molar mass for the given mixture in mass fractions in kg/mol."""
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


class SpecificGasConstant:
    """Specific gas constants for components and mixtures in J/(kg.K) (from table 1)."""

    n2 = Q_(296.8025, ureg.joule / (ureg.kg * ureg.kelvin))
    o2 = Q_(259.8370, ureg.joule / (ureg.kg * ureg.kelvin))
    ar = Q_(208.1324, ureg.joule / (ureg.kg * ureg.kelvin))
    ne = Q_(412.0216, ureg.joule / (ureg.kg * ureg.kelvin))
    h2o = Q_(461.5233, ureg.joule / (ureg.kg * ureg.kelvin))
    co2 = Q_(188.9245, ureg.joule / (ureg.kg * ureg.kelvin))
    co = Q_(296.8384, ureg.joule / (ureg.kg * ureg.kelvin))
    so2 = Q_(129.7822, ureg.joule / (ureg.kg * ureg.kelvin))

    @staticmethod
    def from_mole_fractions(n2=0, o2=0, ar=0, ne=0, h2o=0, co2=0, co=0, so2=0):
        """Calculate the specific gas constant for the given mixture in mole fractions in J/(kg.K)."""
        return R_m / MolarMass.from_mole_fractions(n2, o2, ar, ne, h2o, co2, co, so2)

    @staticmethod
    def from_mass_fractions(n2=0, o2=0, ar=0, ne=0, h2o=0, co2=0, co=0, so2=0):
        """Calculate the specific gas constant for the given mixture in mole fractions in J/(kg.K)."""
        return R_m / MolarMass.from_mass_fractions(n2, o2, ar, ne, h2o, co2, co, so2)
