#!/usr/bin/env python
"""coefficients module."""


class B:
    """Temperature exponents from table 2."""

    __values = {
        1:  0.00,
        2: -1.50,
        3: -1.25,
        4: -0.75,
        5: -0.50,
        6: -0.25,
        7:  0.25,
        8:  0.50,
        9:  0.75,
        10: 1.00,
    }

    def __getitem__(self, key):
        return self.__values[key]


class A:
    """Coefficients a_k,i in J/mol/K from table 3."""

    __values = {
        "n2": {
            1:  2.475830346e6,
            2: -2.815239891e4,
            3:  1.116401165e5,
            4: -8.147644187e5,
            5:  2.185120405e6,
            6: -2.978031305e6,
            7: -1.308008001e6,
            8:  4.305948510e5,
            9: -8.082302563e4,
            10: 6.622545214e3,
        },
        "o2": {  # TODO: input values
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
            10: 0,
        },
        "ar": {  # TODO: input values
            1: 2.078618000e1,
            2: 0,  # TODO: check what "empty" means. 0/NaN/error?
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
            10: 0,
        },
        "ne": {  # TODO: input values
            1: 2.078618000e1,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
            10: 0,
        },
        "h2o": {  # TODO: input values
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
            10: 0,
        },
        "co2": {  # TODO: input values
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
            10: 0,
        },
        "co": {  # TODO: input values
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
            10: 0,
        },
        "so2": {  # TODO: input values
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
            10: 0,
        },
    }

    def __getitem__(self, key):
        component, index = key
        return self.__values[component][index]


class C:
    """Coefficients c_k,i in J/mol."""

    __values = {
        "n2": {
            0:  4.305300363e8,
            1:  6.762730590e8,
            2:  1.537965552e7,
            3: -1.219779913e8,
            4: -8.902116039e8,
            5:  1.193731277e9,
            6: -1.084599001e9,
            7: -2.858259084e8,
            8:  7.841132237e7,
            9: -1.261531969e7,
            10: 9.044741126e5,
        },
        "o2": {},
        "ar": {
            0: -5.677745067e3,
            1:  5.677745067e3,
        },
        "ne": {
            0: -5.677745067e3,
            1:  5.677745067e3,
        },
        "h2o": {},
        "co2": {},
        "co": {},
        "so2": {},
    }

    def __getitem__(self, key):
        component, index = key
        return self.__values[component][index]


class D:
    """Coefficients d_k,i in J/mol/K."""

    __values = {
        "n2": {
            0: -4.085709350e6,
            1:  2.475830346e6,
            2:  1.876826594e4,
            3: -8.931209320e4,
            4:  1.086352558e6,
            5: -4.370240810e6,
            6:  1.191212522e7,
            7: -5.232032004e6,
            8:  8.611897020e5,
            9: -1.077640342e5,
            10: 6.622545214e3,
        },
        "o2": {},
        "ar": {
            0: float("nan"),
            1: 2.078618000e1,
        },
        "ne": {
            0: float("nan"),
            1: 2.078618000e1,
        },
        "h2o": {},
        "co2": {},
        "co": {},
        "so2": {},
    }

    def __getitem__(self, key):
        component, index = key
        return self.__values[component][index]
