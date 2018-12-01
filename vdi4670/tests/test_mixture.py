#!/usr/bin/env python
"""mixture unit test module."""

import pytest
from ..mixture import Mixture


class TestMixture:

    def test_init_mole_fractions_fails_1(self):
        with pytest.raises(ValueError):
            Mixture()

    def test_init_mole_fractions_fails_2(self):
        with pytest.raises(ValueError):
            Mixture(n2=1.1)

    def test_init_mole_fractions_succeeds(self):
        n2 = Mixture(n2=1)
        assert isinstance(n2, Mixture)
        assert n2.x["n2"] == 1
        assert n2.x["o2"] == 0

    def test_molar_heat_capacity(self):
        n2 = Mixture(n2=1)
        print(n2.molar_heat_capacity(300))
        print(n2.heat_capacity(300))


class TestExamples:
    """Test case for testing the mixture examples given in the VDI 4670 document."""

    pass
