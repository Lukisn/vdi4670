#!/usr/bin/env python
"""Unit test module for testing coefficient classes."""

import pytest
from .. import ureg, Q_
from ..coefficients import B, A


class TestB:
    """Test temperature exponents b_i implemented in class B."""

    @pytest.fixture
    def b(self):
        return B()

    def test_initialization(self):
        assert isinstance(B(), B)

    def test_indexing_in_range_succeeds(self, b):
        assert b[1] == 0  # first
        assert b[10] == 1  # last

    def test_indexing_out_of_range_fails(self, b):
        with pytest.raises(KeyError):
            _ = b[0]  # index below range
            _ = b[11]  # index above range

    def test_index_operator_assignment(self, b):
        with pytest.raises(TypeError):
            b[1] = 0

    def test_index_operator_deletion(self, b):
        with pytest.raises(TypeError):
            del b[1]


class TestA:
    """Test coefficients a_k,i implemented in class A."""

    @pytest.fixture
    def a(self):
        return A()

    def test_initialization(self):
        assert isinstance(A(), A)

    def test_indexing_in_range_succeeds(self, a):
        assert a["n2", 1] == Q_(2.475830346e6, ureg.joule / (ureg.mol * ureg.kelvin))  # first
        assert a["n2", 10] == Q_(6.622545214e3, ureg.joule / (ureg.mol * ureg.kelvin))  # last

    def test_indexing_out_of_range_fails(self, a):
        with pytest.raises(KeyError):
            _ = a["n2", 0]  # index below range
            _ = a["n2", 11]  # index above range
            _ = a["invalid component", 1]  # invalid component

    def test_index_operator_assignment(self, a):
        with pytest.raises(TypeError):
            a["n2", 1] = 0

    def test_index_operator_deletion(self, a):
        with pytest.raises(TypeError):
            del a["n2", 1]
