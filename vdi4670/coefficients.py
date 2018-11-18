#!/usr/bin/env python
"""coefficients module."""


class B:
    """Temperature exponents from table 2."""

    __values = {
        1: 0.0,
        2: -1.5,
        3: -1.25,
        4: -0.75,
        5: -0.5,
        6: -0.25,
        7: 0.25,
        8: 0.5,
        9: 0.75,
        10: 1,
    }

    def __getitem__(self, key):
        return self.__values[key]


class A:
    """Coefficients a_k,i in J/mol/K from table 3."""

    __values = {
        "n2": {
            1: 2.4e6,
            2: -2.8e4,
            3: 1.1e5,
            4: -8.1e5,
            5: 2.1e6,
            6: -2.9e6,
            7: -1.3e6,
            8: 4.3e5,
            9: -8.0e4,
            10: 6.6e3,
        },
        "o2": {},
        "ar": {},
        "ne": {},
        "h2o": {},
        "co2": {},
        "co": {},
        "so2": {},
    }

    def __getitem__(self, key):
        component, index = key
        return self.__values[component][index]
