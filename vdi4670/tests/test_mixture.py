#!/usr/bin/env python
"""mixture unit test module."""

from pytest import raises, approx
from .. import ureg, Q_
from ..mixture import Mixture


class TestMixture:
    """Test case for testing mixture class."""

    def test_init_no_mole_fractions_fails(self):
        with raises(ValueError):
            Mixture()

    def test_init_high_mole_fractions_fails(self):
        x = 1 + 1e-5
        with raises(ValueError):
            Mixture(n2=x)

    def test_init_low_mole_fractions_fails(self):
        x = 1 - 1e-5
        with raises(ValueError):
            Mixture(n2=x)

    def test_init_high_mole_fractions_succeeds(self):
        x = 1 + 1e-7
        n2 = Mixture(n2=x)
        assert isinstance(n2, Mixture)
        assert n2.x["n2"] == x
        assert n2.x["o2"] == 0

    def test_init_low_mole_fractions_succeeds(self):
        x = 1 - 1e-7
        n2 = Mixture(n2=x)
        assert isinstance(n2, Mixture)
        assert n2.x["n2"] == x
        assert n2.x["o2"] == 0

    def test_init_exact_mole_fractions_succeeds(self):
        n2 = Mixture(n2=1)
        assert isinstance(n2, Mixture)
        assert n2.x["n2"] == 1
        assert n2.x["o2"] == 0

    def test_init_air_succeeds(self):
        air = Mixture.init_iso_air()
        assert isinstance(air, Mixture)
        assert air.x["n2"] == 0.781109
        assert air.x["o2"] == 0.209548
        assert air.x["ar"] == 0.009343

    def test_init_gas_succeeds(self):
        gas = Mixture.init_example_gas()
        assert isinstance(gas, Mixture)
        assert gas.x["n2"] == 0.6
        assert gas.x["o2"] == 0.1
        assert gas.x["ar"] == 0.01
        assert gas.x["h2o"] == 0.17
        assert gas.x["co2"] == 0.1
        assert gas.x["co"] == 0.01
        assert gas.x["so2"] == 0.01


class TestExamplesBase:
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
    combustion_gas = Mixture.init_example_gas()

    # Test Function
    @staticmethod
    def assert_approx(result, expected, rel_err=1e-6, abs_err=1e-12):
        assert result.dimensionality == expected.dimensionality
        assert result.magnitude == approx(expected.magnitude, rel=rel_err, abs=abs_err)


class TestExamplesOne(TestExamplesBase):
    """Test case for testing the first set of mixture examples given in the VDI 4670 document."""

    # example point 1:
    p, t = Q_(0.1, ureg.megapascal), Q_(1000, ureg.kelvin)

    # Nitrogen
    def test_n2_density(self):
        expected = Q_(12.027, self.density_unit)
        result = self.n2.molar_density(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_n2_heat_capacity(self):
        expected = Q_(32.698, self.heat_capacity_unit)
        result = self.n2.molar_heat_capacity(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_n2_enthalpy(self):
        expected = Q_(22190.5, self.enthalpy_unit)
        result = self.n2.molar_enthalpy(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-2)

    def test_n2_entropy(self):
        expected = Q_(39.221, self.entropy_unit)
        result = self.n2.molar_entropy(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    # Oxygen
    def test_o2_density(self):
        expected = Q_(12.027, self.density_unit)
        result = self.o2.molar_density(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_o2_heat_capacity(self):
        expected = Q_(34.880, self.heat_capacity_unit)
        result = self.o2.molar_heat_capacity(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_o2_enthalpy(self):
        expected = Q_(23439.2, self.enthalpy_unit)
        result = self.o2.molar_enthalpy(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-2)

    def test_o2_entropy(self):
        expected = Q_(41.112, self.entropy_unit)
        result = self.o2.molar_entropy(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    # Argon
    def test_ar_density(self):
        expected = Q_(12.027, self.density_unit)
        result = self.ar.molar_density(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_ar_heat_capacity(self):
        expected = Q_(20.786, self.heat_capacity_unit)
        result = self.ar.molar_heat_capacity(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_ar_enthalpy(self):
        expected = Q_(15108.4, self.enthalpy_unit)
        result = self.ar.molar_enthalpy(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-2)

    def test_ar_entropy(self):
        expected = Q_(27.084, self.entropy_unit)
        result = self.ar.molar_entropy(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    # Neon
    def test_ne_density(self):
        expected = Q_(12.027, self.density_unit)
        result = self.ne.molar_density(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_ne_heat_capacity(self):
        expected = Q_(20.786, self.heat_capacity_unit)
        result = self.ne.molar_heat_capacity(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_ne_enthalpy(self):
        expected = Q_(15108.4, self.enthalpy_unit)
        result = self.ne.molar_enthalpy(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-2)

    def test_ne_entropy(self):
        expected = Q_(27.084, self.entropy_unit)
        result = self.ne.molar_entropy(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    # Water
    def test_h2o_density(self):
        expected = Q_(12.027, self.density_unit)
        result = self.h2o.molar_density(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_h2o_heat_capacity(self):
        expected = Q_(41.295, self.heat_capacity_unit)
        result = self.h2o.molar_heat_capacity(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_h2o_enthalpy(self):
        expected = Q_(26841.3, self.enthalpy_unit)
        result = self.h2o.molar_enthalpy(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-2)

    def test_h2o_entropy(self):
        expected = Q_(46.953, self.entropy_unit)
        result = self.h2o.molar_entropy(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    # Carbon dioxide
    def test_co2_density(self):
        expected = Q_(12.027, self.density_unit)
        result = self.co2.molar_density(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_co2_heat_capacity(self):
        expected = Q_(54.316, self.heat_capacity_unit)
        result = self.co2.molar_heat_capacity(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_co2_enthalpy(self):
        expected = Q_(34319.4, self.enthalpy_unit)
        result = self.co2.molar_enthalpy(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-2)

    def test_co2_entropy(self):
        expected = Q_(58.830, self.entropy_unit)
        result = self.co2.molar_entropy(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    # Carbon monoxide
    def test_co_density(self):
        expected = Q_(12.027, self.density_unit)
        result = self.co.molar_density(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_co_heat_capacity(self):
        expected = Q_(33.186, self.heat_capacity_unit)
        result = self.co.molar_heat_capacity(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_co_enthalpy(self):
        expected = Q_(22414.6, self.enthalpy_unit)
        result = self.co.molar_enthalpy(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-2)

    def test_co_entropy(self):
        expected = Q_(39.538, self.entropy_unit)
        result = self.co.molar_entropy(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    # Sulphur dioxide
    def test_so2_density(self):
        expected = Q_(12.027, self.density_unit)
        result = self.so2.molar_density(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_so2_heat_capacity(self):
        expected = Q_(54.288, self.heat_capacity_unit)
        result = self.so2.molar_heat_capacity(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_so2_enthalpy(self):
        expected = Q_(35329.5, self.enthalpy_unit)
        result = self.so2.molar_enthalpy(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-2)

    def test_so2_entropy(self):
        expected = Q_(60.984, self.entropy_unit)
        result = self.so2.molar_entropy(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    # Combustion gas
    def test_combustion_gas_density(self):
        expected = Q_(12.027, self.density_unit)
        result = self.combustion_gas.molar_density(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_combustion_gas_heat_capacity(self):
        expected = Q_(36.641, self.heat_capacity_unit)
        result = self.combustion_gas.molar_heat_capacity(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_combustion_gas_enthalpy(self):
        expected = Q_(24381.7, self.enthalpy_unit)
        result = self.combustion_gas.molar_enthalpy(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-2)

    def test_combustion_gas_entropy(self):
        expected = Q_(52.815, self.entropy_unit)
        result = self.combustion_gas.molar_entropy(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)


class TestExamplesTwo(TestExamplesBase):
    """Test case for testing the second set of mixture examples given in the VDI 4670 document."""

    # example point 2:
    p, t = Q_(2.0, ureg.megapascal), Q_(2000, ureg.kelvin)

    # Nitrogen
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

    # Oxygen
    def test_o2_density(self):
        expected = Q_(120.272, self.density_unit)
        result = self.o2.molar_density(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_o2_heat_capacity(self):
        expected = Q_(37.783, self.heat_capacity_unit)
        result = self.o2.molar_heat_capacity(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_o2_enthalpy(self):
        expected = Q_(59935.0, self.enthalpy_unit)
        result = self.o2.molar_enthalpy(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-2)

    def test_o2_entropy(self):
        expected = Q_(41.389, self.entropy_unit)
        result = self.o2.molar_entropy(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    # Argon
    def test_ar_density(self):
        expected = Q_(120.272, self.density_unit)
        result = self.ar.molar_density(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_ar_heat_capacity(self):
        expected = Q_(20.786, self.heat_capacity_unit)
        result = self.ar.molar_heat_capacity(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_ar_enthalpy(self):
        expected = Q_(35894.6, self.enthalpy_unit)
        result = self.ar.molar_enthalpy(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-2)

    def test_ar_entropy(self):
        expected = Q_(16.584, self.entropy_unit)
        result = self.ar.molar_entropy(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    # Neon
    def test_ne_density(self):
        expected = Q_(120.272, self.density_unit)
        result = self.ne.molar_density(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_ne_heat_capacity(self):
        expected = Q_(20.786, self.heat_capacity_unit)
        result = self.ne.molar_heat_capacity(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_ne_enthalpy(self):
        expected = Q_(35894.6, self.enthalpy_unit)
        result = self.ne.molar_enthalpy(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-2)

    def test_ne_entropy(self):
        expected = Q_(16.584, self.entropy_unit)
        result = self.ne.molar_entropy(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    # Water
    def test_h2o_density(self):
        expected = Q_(120.272, self.density_unit)
        result = self.h2o.molar_density(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_h2o_heat_capacity(self):
        expected = Q_(51.763, self.heat_capacity_unit)
        result = self.h2o.molar_heat_capacity(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_h2o_enthalpy(self):
        expected = Q_(73880.3, self.enthalpy_unit)
        result = self.h2o.molar_enthalpy(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-2)

    def test_h2o_entropy(self):
        expected = Q_(54.226, self.entropy_unit)
        result = self.h2o.molar_entropy(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    # Carbon dioxide
    def test_co2_density(self):
        expected = Q_(120.272, self.density_unit)
        result = self.co2.molar_density(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_co2_heat_capacity(self):
        expected = Q_(60.350, self.heat_capacity_unit)
        result = self.co2.molar_heat_capacity(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_co2_enthalpy(self):
        expected = Q_(92376.5, self.enthalpy_unit)
        result = self.co2.molar_enthalpy(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-2)

    def test_co2_entropy(self):
        expected = Q_(73.927, self.entropy_unit)
        result = self.co2.molar_entropy(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    # Carbon monoxide
    def test_co_density(self):
        expected = Q_(120.272, self.density_unit)
        result = self.co.molar_density(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_co_heat_capacity(self):
        expected = Q_(36.234, self.heat_capacity_unit)
        result = self.co.molar_heat_capacity(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_co_enthalpy(self):
        expected = Q_(57459.5, self.enthalpy_unit)
        result = self.co.molar_enthalpy(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-2)

    def test_co_entropy(self):
        expected = Q_(38.802, self.entropy_unit)
        result = self.co.molar_entropy(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    # Sulphur dioxide
    def test_so2_density(self):
        expected = Q_(120.272, self.density_unit)
        result = self.so2.molar_density(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_so2_heat_capacity(self):
        expected = Q_(57.893, self.heat_capacity_unit)
        result = self.so2.molar_heat_capacity(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_so2_enthalpy(self):
        expected = Q_(91880.0, self.enthalpy_unit)
        result = self.so2.molar_enthalpy(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-2)

    def test_so2_entropy(self):
        expected = Q_(75.133, self.entropy_unit)
        result = self.so2.molar_entropy(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    # Combustion gas
    def test_combustion_gas_density(self):
        expected = Q_(120.272, self.density_unit)
        result = self.combustion_gas.molar_density(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_combustion_gas_heat_capacity(self):
        expected = Q_(41.343, self.heat_capacity_unit)
        result = self.combustion_gas.molar_heat_capacity(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)

    def test_combustion_gas_enthalpy(self):
        expected = Q_(63763.2, self.enthalpy_unit)
        result = self.combustion_gas.molar_enthalpy(t=self.t)
        self.assert_approx(result, expected, rel_err=1e-2)

    def test_combustion_gas_entropy(self):
        expected = Q_(55.017, self.entropy_unit)
        result = self.combustion_gas.molar_entropy(p=self.p, t=self.t)
        self.assert_approx(result, expected, rel_err=1e-4)
