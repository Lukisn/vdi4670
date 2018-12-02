#!/usr/bin/env python
"""coefficients module."""

from . import ureg, Q_


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
            1: Q_(2.475830346e6, ureg.joule / (ureg.mol * ureg.kelvin)),
            2: Q_(-2.815239891e4, ureg.joule / (ureg.mol * ureg.kelvin)),
            3: Q_(1.116401165e5, ureg.joule / (ureg.mol * ureg.kelvin)),
            4: Q_(-8.147644187e5, ureg.joule / (ureg.mol * ureg.kelvin)),
            5: Q_(2.185120405e6, ureg.joule / (ureg.mol * ureg.kelvin)),
            6: Q_(-2.978031305e6, ureg.joule / (ureg.mol * ureg.kelvin)),
            7: Q_(-1.308008001e6, ureg.joule / (ureg.mol * ureg.kelvin)),
            8: Q_(4.305948510e5, ureg.joule / (ureg.mol * ureg.kelvin)),
            9: Q_(-8.082302563e4, ureg.joule / (ureg.mol * ureg.kelvin)),
            10: Q_(6.622545214e3, ureg.joule / (ureg.mol * ureg.kelvin)),
        },
        "o2": {  # TODO: input values
            1: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            2: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            3: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            4: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            5: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            6: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            7: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            8: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            9: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            10: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
        },
        "ar": {
            1: Q_(2.078618000e1, ureg.joule / (ureg.mol * ureg.kelvin)),
            2: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            2: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            3: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            4: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            5: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            6: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            7: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            8: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            9: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            10: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
        },
        "ne": {
            1: Q_(2.078618000e1, ureg.joule / (ureg.mol * ureg.kelvin)),
            2: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            3: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            4: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            5: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            6: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            7: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            8: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            9: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            10: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
        },
        "h2o": {  # TODO: input values
            1: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            2: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            3: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            4: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            5: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            6: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            7: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            8: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            9: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            10: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
        },
        "co2": {  # TODO: input values
            1: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            2: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            3: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            4: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            5: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            6: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            7: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            8: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            9: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            10: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
        },
        "co": {  # TODO: input values
            1: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            2: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            3: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            4: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            5: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            6: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            7: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            8: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            9: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            10: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
        },
        "so2": {  # TODO: input values
            1: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            2: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            3: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            4: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            5: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            6: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            7: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            8: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            9: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
            10: Q_(0, ureg.joule / (ureg.mol * ureg.kelvin)),
        },
    }

    def __getitem__(self, key):
        component, index = key
        return self.__values[component][index]


class C:
    """Coefficients c_k,i in J/mol."""

    __values = {
        "n2": {
            0: Q_(4.305300363e8, ureg.joule / ureg.mol),
            1: Q_(6.762730590e8, ureg.joule / ureg.mol),
            2: Q_(1.537965552e7, ureg.joule / ureg.mol),
            3: Q_(-1.219779913e8, ureg.joule / ureg.mol),
            4: Q_(-8.902116039e8, ureg.joule / ureg.mol),
            5: Q_(1.193731277e9, ureg.joule / ureg.mol),
            6: Q_(-1.084599001e9, ureg.joule / ureg.mol),
            7: Q_(-2.858259084e8, ureg.joule / ureg.mol),
            8: Q_(7.841132237e7, ureg.joule / ureg.mol),
            9: Q_(-1.261531969e7, ureg.joule / ureg.mol),
            10: Q_(9.044741126e5, ureg.joule / ureg.mol),
        },
        "o2": {},
        "ar": {
            0: Q_(-5.677745067e3, ureg.joule / ureg.mol),
            1: Q_(5.677745067e3, ureg.joule / ureg.mol),
        },
        "ne": {
            0: Q_(-5.677745067e3, ureg.joule / ureg.mol),
            1: Q_(5.677745067e3, ureg.joule / ureg.mol),
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
