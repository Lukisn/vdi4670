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
        assert n2._x_N2 == 1
        assert n2._x_O2 == 0
