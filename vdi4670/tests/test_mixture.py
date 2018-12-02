#!/usr/bin/env python
"""mixture unit test module."""

from pytest import raises, approx
from .. import ureg, Q_
from ..mixture import Mixture


class TestMixture:

    def test_init_mole_fractions_fails_1(self):
        with raises(ValueError):
            Mixture()

    def test_init_mole_fractions_fails_2(self):
        with raises(ValueError):
            Mixture(n2=1.1)

    def test_init_mole_fractions_succeeds(self):
        n2 = Mixture(n2=1)
        assert isinstance(n2, Mixture)
        assert n2.x["n2"] == 1
        assert n2.x["o2"] == 0


class TestExamples:
    """Test case for testing the mixture examples given in the VDI 4670 document."""

    # example point 1:
    p1 = Q_(0.1, ureg.megapascal)
    T1 = Q_(1000, ureg.kelvin)

    # example point 2:
    p2 = Q_(2.0, ureg.megapascal)
    T2 = Q_(2000, ureg.kelvin)

    def test_nitrogen_density_ex1(self):
        n2 = Mixture(n2=1.0)
        expected = Q_(12.027, ureg.mol / ureg.meter ** 3)
        result = n2.molar_density(pressure=self.p1, temperature=self.T1)
        assert result.dimensionality == expected.dimensionality
        assert result.magnitude == approx(expected.magnitude, 1e-4)

    def test_nitrogen_density_ex2(self):
        n2 = Mixture(n2=1.0)
        expected = Q_(120.272, ureg.mol / ureg.meter ** 3)
        result = n2.molar_density(pressure=self.p2, temperature=self.T2)
        assert result.dimensionality == expected.dimensionality
        assert result.magnitude == approx(expected.magnitude, 1e-4)

    def test_nitrogen_heat_capacity_ex1(self):
        n2 = Mixture(n2=1.0)
        expected = Q_(32.698, ureg.joule / ureg.mol / ureg.kelvin)
        result = n2.molar_heat_capacity(temperature=self.T1)
        assert result.dimensionality == expected.dimensionality
        assert result.magnitude == approx(expected.magnitude, 1e-4)

    def test_nitrogen_heat_capacity_ex2(self):
        n2 = Mixture(n2=1.0)
        expected = Q_(35.969, ureg.joule / ureg.mol / ureg.kelvin)
        result =n2.molar_heat_capacity(temperature=self.T2)
        assert result.dimensionality == expected.dimensionality
        assert result.magnitude == approx(expected.magnitude, 1e-3)
