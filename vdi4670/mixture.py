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
        self._x_n2 = n2
        self._x_o2 = o2
        self._x_ar = ar
        self._x_ne = ne
        self._x_h2o = h2o
        self._x_co2 = co2
        self._x_co = co
        self._x_so2 = so2

    @classmethod
    def air(cls):
        return cls(n2=0.781109, o2=0.209548, ar=0.009343)

    @classmethod
    def test_gas(cls):
        return cls(n2=0.6, o2=0.1, ar=0.01, h2o=0.17, co2=0.1, co=0.01, so2=0.01)

    def molar_mass(self):
        return MolarMass.from_mole_fractions(
            n2=self._x_n2,
            o2=self._x_o2,
            ar=self._x_ar,
            ne=self._x_ne,
            h2o=self._x_h2o,
            co2=self._x_co2,
            co=self._x_co,
            so2=self._x_so2
        )

    # TODO: implement default calculation procedures for non-dissociated mixtures.
    def molar_density(self, pressure, temperature):
        """Calculate the molar density of the mixture in mol/m3."""
        raise NotImplementedError

    def density(self, pressure, temperature):
        """Calculate the mass density of the mixture in kg/m3."""
        raise NotImplementedError

    def molar_heat_capacity(self, temperature):
        """Calculate the isobaric heat capacity of the mixture in J/mol/K."""
        raise NotImplementedError

    def heat_capacity(self, temperature):
        """Calculate the specific isobaric heat capacity of the mixture in J/kg/K."""
        raise NotImplementedError

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
        """Calculate the soecific entropy of the mixture in J/kg/K."""
        raise NotImplementedError
