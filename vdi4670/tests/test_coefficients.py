#!/usr/bin/env python
"""coefficients module."""

import pytest
from ..coefficients import B


class TestB:
    def test_index_operator_fails(self):
        with pytest.raises(KeyError):
            _ = B[0]

    def test_index_operator(self):
        assert B[1] == 0


class TestA:
    def test_(self):
        pass
