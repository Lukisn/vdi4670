#!/usr/bin/env python
"""coefficients module."""

from . import ureg, Q_


class B:
    """Temperature exponents. (from table 2)"""

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
    """Coefficients a_k,i in J/(mol.K) from. (from table 3)"""

    __unit = ureg.joule / (ureg.mol * ureg.kelvin)

    __values = {
        "n2": {
            1: Q_(+2.475830346e6, __unit),
            2: Q_(-2.815239891e4, __unit),
            3: Q_(+1.116401165e5, __unit),
            4: Q_(-8.147644187e5, __unit),
            5: Q_(+2.185120405e6, __unit),
            6: Q_(-2.978031305e6, __unit),
            7: Q_(-1.308008001e6, __unit),
            8: Q_(+4.305948510e5, __unit),
            9: Q_(-8.082302563e4, __unit),
            10: Q_(+6.622545214e3, __unit),
        },
        "o2": {
            1: Q_(+6.408242565e5, __unit),
            2: Q_(-1.599937045e3, __unit),
            3: Q_(+9.984801256e3, __unit),
            4: Q_(-1.280873444e5, __unit),
            5: Q_(+4.186599156e5, __unit),
            6: Q_(-6.720142804e5, __unit),
            7: Q_(-3.799977202e5, __unit),
            8: Q_(+1.378691801e5, __unit),
            9: Q_(-2.806965185e4, __unit),
            10: Q_(+2.459943097e3, __unit),
        },
        "ar": {
            1: Q_(+2.078618000e1, __unit),
            2: Q_(0, __unit),
            3: Q_(0, __unit),
            4: Q_(0, __unit),
            5: Q_(0, __unit),
            6: Q_(0, __unit),
            7: Q_(0, __unit),
            8: Q_(0, __unit),
            9: Q_(0, __unit),
            10: Q_(0, __unit),
        },
        "ne": {
            1: Q_(+2.078618000e1, __unit),
            2: Q_(0, __unit),
            3: Q_(0, __unit),
            4: Q_(0, __unit),
            5: Q_(0, __unit),
            6: Q_(0, __unit),
            7: Q_(0, __unit),
            8: Q_(0, __unit),
            9: Q_(0, __unit),
            10: Q_(0, __unit),
        },
        "h2o": {
            1: Q_(-4.747782033e6, __unit),
            2: Q_(+4.799919289e4, __unit),
            3: Q_(-1.931588954e5, __unit),
            4: Q_(+1.460728340e6, __unit),
            5: Q_(-4.000075762e6, __unit),
            6: Q_(+5.576209858e6, __unit),
            7: Q_(+2.570488297e6, __unit),
            8: Q_(-8.670521019e5, __unit),
            9: Q_(+1.666429390e5, __unit),
            10: Q_(-1.396634620e4, __unit),
        },
        "co2": {
            1: Q_(+1.103695150e6, __unit),
            2: Q_(-1.365096910e4, __unit),
            3: Q_(+5.357704944e4, __unit),
            4: Q_(-3.816063864e5, __unit),
            5: Q_(+1.008950325e6, __unit),
            6: Q_(-1.352938737e6, __unit),
            7: Q_(-5.701809626e5, __unit),
            8: Q_(+1.828513133e5, __unit),
            9: Q_(-3.329618224e4, __unit),
            10: Q_(+2.635366727e3, __unit),
        },
        "co": {
            1: Q_(+2.670755728e6, __unit),
            2: Q_(-2.715629936e4, __unit),
            3: Q_(+1.096509012e5, __unit),
            4: Q_(-8.303525865e5, __unit),
            5: Q_(+2.269213594e6, __unit),
            6: Q_(-3.151865706e6, __unit),
            7: Q_(-1.438126165e6, __unit),
            8: Q_(+4.824833432e5, __unit),
            9: Q_(-9.227524508e4, __unit),
            10: Q_(+7.701550175e3, __unit),
        },
        "so2": {
            1: Q_(-2.076653674e6, __unit),
            2: Q_(+2.589571253e4, __unit),
            3: Q_(-1.012523438e5, __unit),
            4: Q_(+7.161863952e5, __unit),
            5: Q_(-1.889754780e6, __unit),
            6: Q_(+2.535020356e6, __unit),
            7: Q_(+1.082842148e6, __unit),
            8: Q_(-3.524395911e5, __unit),
            9: Q_(+6.552035769e4, __unit),
            10: Q_(-5.325634796e3, __unit),
        },
    }

    def __getitem__(self, key):
        component, index = key
        return self.__values[component][index]


class C:
    """Coefficients c_k,i in J/mol."""
    
    __unit = ureg.joule / ureg.mol

    __values = {
        "n2": {
            0: Q_(+4.305300363e8, __unit),
            1: Q_(+6.762730590e8, __unit),
            2: Q_(+1.537965552e7, __unit),
            3: Q_(-1.219779913e8, __unit),
            4: Q_(-8.902116039e8, __unit),
            5: Q_(+1.193731277e9, __unit),
            6: Q_(-1.084599001e9, __unit),
            7: Q_(-2.858259084e8, __unit),
            8: Q_(+7.841132237e7, __unit),
            9: Q_(-1.261531969e7, __unit),
            10: Q_(+9.044741126e5, __unit),
        },
        "o2": {

        },
        "ar": {
            0: Q_(-5.677745067e3, __unit),
            1: Q_(+5.677745067e3, __unit),
        },
        "ne": {
            0: Q_(-5.677745067e3, __unit),
            1: Q_(+5.677745067e3, __unit),
        },
        "h2o": {

        },
        "co2": {

        },
        "co": {

        },
        "so2": {

        },
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
