#!/usr/bin/env python
"""mixture module."""

# from . import ureg, Q_
from .constants import *


class Mixture:
    """Mixture class."""

    def __init__(self, n2=0., o2=0., ar=0., ne=0., h2o=0., co2=0., co=0., so2=0.):
        """Initialize mixture from mole fractions."""
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

    @classmethod
    def air(cls):
        return cls(n2=0.781109, o2=0.209548, ar=0.009343)

    @classmethod
    def test_gas(cls):
        return cls(n2=0.6, o2=0.1, ar=0.01, h2o=0.17, co2=0.1, co=0.01, so2=0.01)

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


