#!/usr/bin/env python
"""mixture unit test module."""

from pytest import raises, approx
from .. import ureg, Q_
from ..mixture import Mixture


class TestMixture:
    """Test case for testing mixture class."""

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


class PintApprox:
    """Class providing functionality for testing pint quantities for approximate equality."""

    # Units
    density_unit = ureg.mol / ureg.meter ** 3
    heat_capacity_unit = ureg.joule / ureg.mol / ureg.kelvin
    enthalpy_unit = ureg.joule / ureg.mol
    entropy_unit = ureg.joule / (ureg.mol * ureg.kelvin)

    # Mixtures
    n2 = Mixture(n2=1.0)
    o2 = Mixture(o2=1.0)
    ar = Mixture(ar=1.0)
    ne = Mixture(ne=1.0)
    h2o = Mixture(h2o=1.0)
    co2 = Mixture(co2=1.0)
    co = Mixture(co=1.0)
    so2 = Mixture(so2=1.0)
    test_gas = Mixture.test_gas()

    # Test Function
    @staticmethod
    def assert_approx(result, expected, rel_err=1e-6, abs_err=1e-12):
        assert result.dimensionality == expected.dimensionality
        assert result.magnitude == approx(expected.magnitude, rel=rel_err, abs=abs_err)


class TestExamplesOne(PintApprox):
    """Test case for testing the first set of mixture examples given in the VDI 4670 document."""

    # example point 1:
    p, t = Q_(0.1, ureg.megapascal), Q_(1000, ureg.kelvin)

    def test_nitrogen_density(self):
        expected = Q_(12.027, self.density_unit)
        result = self.n2.molar_density(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_nitrogen_heat_capacity(self):
        expected = Q_(32.698, self.heat_capacity_unit)
        result = self.n2.molar_heat_capacity(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_nitrogen_enthalpy(self):
        expected = Q_(22190.5, self.enthalpy_unit)
        result = self.n2.molar_enthalpy(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-2)

    def test_nitrogen_entropy(self):
        expected = Q_(39.221, self.entropy_unit)
        result = self.n2.molar_entropy(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)


class TestExamplesTwo(PintApprox):
    """Test case for testing the second set of mixture examples given in the VDI 4670 document."""

    # example point 2:
    p, t = Q_(2.0, ureg.megapascal), Q_(2000, ureg.kelvin)

    def test_nitrogen_density(self):
        expected = Q_(120.272, ureg.mol / ureg.meter ** 3)
        result = self.n2.molar_density(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_nitrogen_heat_capacity(self):
        expected = Q_(35.969, ureg.joule / ureg.mol / ureg.kelvin)
        result = self.n2.molar_heat_capacity(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_nitrogen_enthalpy(self):
        expected = Q_(56866.8, self.enthalpy_unit)
        result = self.n2.molar_enthalpy(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-2)

    def test_nitrogen_entropy(self):
        expected = Q_(38.219, self.entropy_unit)
        result = self.n2.molar_entropy(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)