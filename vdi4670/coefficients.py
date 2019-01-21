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
            9: Q_(-2.806954185e4, __unit),
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
    """Coefficients c_k,i in J/mol. (from table 4)"""
    
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
            0: Q_(+5.295253592e7, __unit),
            1: Q_(+1.750411457e8, __unit),
            2: Q_(+8.740456077e5, __unit),
            3: Q_(-1.090939385e7, __unit),
            4: Q_(-1.399482325e8, __unit),
            5: Q_(+2.287139119e8, __unit),
            6: Q_(-2.447476009e8, __unit),
            7: Q_(-8.303710182e7, __unit),
            8: Q_(+2.510597770e7, __unit),
            9: Q_(-4.381254489e6, __unit),
            10: Q_(+3.359667285e5, __unit),
        },
        "ar": {
            0: Q_(-5.677745067e3, __unit),
            1: Q_(+5.677745067e3, __unit),
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
            0: Q_(-5.677745067e3, __unit),
            1: Q_(+5.677745067e3, __unit),
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
            0: Q_(-7.574888563e8, __unit),
            1: Q_(-1.296856662e9, __unit),
            2: Q_(-2.622195908e7, __unit),
            3: Q_(+2.110454091e8, __unit),
            4: Q_(+1.595991784e9, __unit),
            5: Q_(-2.185241389e9, __unit),
            6: Q_(+2.030855630e9, __unit),
            7: Q_(+5.617031027e8, __unit),
            8: Q_(-1.578901878e8, __unit),
            9: Q_(+2.601058216e7, __unit),
            10: Q_(-1.907453732e6, __unit),
        },
        "co2": {
            0: Q_(+2.042361458e8, __unit),
            1: Q_(+3.014743302e8, __unit),
            2: Q_(+7.457524419e6, __unit),
            3: Q_(-5.853828422e7, __unit),
            4: Q_(-4.169431378e8, __unit),
            5: Q_(+5.511895625e8, __unit),
            6: Q_(-4.927402880e8, __unit),
            7: Q_(-1.245959439e8, __unit),
            8: Q_(+3.329722415e7, __unit),
            9: Q_(-5.197058388e6, __unit),
            10: Q_(+3.599252107e5, __unit),
        },
        "co": {
            0: Q_(+4.306836224e8, __unit),
            1: Q_(+7.295169271e8, __unit),
            2: Q_(+1.483548634e7, __unit),
            3: Q_(-1.198045747e8, __unit),
            4: Q_(-9.072432360e8, __unit),
            5: Q_(+1.239671386e9, __unit),
            6: Q_(-1.147909490e9, __unit),
            7: Q_(-3.142593296e8, __unit),
            8: Q_(+8.786021680e7, __unit),
            9: Q_(-1.440284754e7, __unit),
            10: Q_(+1.051839215e6, __unit),
        },
        "so2": {
            0: Q_(-3.845730250e8, __unit),
            1: Q_(-5.672379511e8, __unit),
            2: Q_(-1.414682776e7, __unit),
            3: Q_(+1.106283108e8, __unit),
            4: Q_(+7.825052554e8, __unit),
            5: Q_(-1.032373036e9, __unit),
            6: Q_(+9.232544137e8, __unit),
            7: Q_(+2.366226662e8, __unit),
            8: Q_(-6.417924954e7, __unit),
            9: Q_(+1.022679183e7, __unit),
            10: Q_(-7.273485723e5, __unit),
        },
    }

    def __getitem__(self, key):
        component, index = key
        return self.__values[component][index]


class D:
    """Coefficients d_k,i in J/(mol.K). (from table 5)"""

    __unit = ureg.joule / (ureg.mol * ureg.kelvin)

    __values = {
        "n2": {
            0: Q_(-4.085709350e6, __unit),
            1: Q_(+2.475830346e6, __unit),
            2: Q_(+1.876826594e4, __unit),
            3: Q_(-8.931209320e4, __unit),
            4: Q_(+1.086352558e6, __unit),
            5: Q_(-4.370240810e6, __unit),
            6: Q_(+1.191212522e7, __unit),
            7: Q_(-5.232032004e6, __unit),
            8: Q_(+8.611897020e5, __unit),
            9: Q_(-1.077640342e5, __unit),
            10: Q_(+6.622545214e3, __unit),
        },
        "o2": {
            0: Q_(-7.353805669e5, __unit),
            1: Q_(+6.408242565e5, __unit),
            2: Q_(+1.066624697e3, __unit),
            3: Q_(-7.987841005e3, __unit),
            4: Q_(+1.707831259e5, __unit),
            5: Q_(-8.373198312e5, __unit),
            6: Q_(+2.688057122e6, __unit),
            7: Q_(-1.519990881e6, __unit),
            8: Q_(+2.757383602e5, __unit),
            9: Q_(-3.742605580e4, __unit),
            10: Q_(+2.459943097e3, __unit),
        },
        "ar": {
            0: Q_(0, __unit),
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
            0: Q_(0, __unit),
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
            0: Q_(+7.373724814e6, __unit),
            1: Q_(-4.747782033e6, __unit),
            2: Q_(-3.199946193e4, __unit),
            3: Q_(+1.545271163e5, __unit),
            4: Q_(-1.947637787e6, __unit),
            5: Q_(+8.000151524e6, __unit),
            6: Q_(-2.230483943e7, __unit),
            7: Q_(+1.028195319e7, __unit),
            8: Q_(-1.734104204e6, __unit),
            9: Q_(+2.221905853e5, __unit),
            10: Q_(-1.396634620e4, __unit),
        },
        "co2": {
            0: Q_(-1.912121053e6, __unit),
            1: Q_(+1.103695150e6, __unit),
            2: Q_(+9.100646067e3, __unit),
            3: Q_(-4.286163955e4, __unit),
            4: Q_(+5.088085152e5, __unit),
            5: Q_(-2.017900650e6, __unit),
            6: Q_(+5.411754948e6, __unit),
            7: Q_(-2.280723850e6, __unit),
            8: Q_(+3.657026266e5, __unit),
            9: Q_(-4.439490965e4, __unit),
            10: Q_(+2.635366727e3, __unit),
        },
        "co": {
            0: Q_(-4.203685809e6, __unit),
            1: Q_(+2.670755728e6, __unit),
            2: Q_(+1.810419957e4, __unit),
            3: Q_(-8.772072096e4, __unit),
            4: Q_(+1.107136782e6, __unit),
            5: Q_(-4.538427188e6, __unit),
            6: Q_(+1.260746282e7, __unit),
            7: Q_(-5.752504660e6, __unit),
            8: Q_(+9.649666864e5, __unit),
            9: Q_(-1.230336601e5, __unit),
            10: Q_(+7.701550175e3, __unit),
        },
        "so2": {
            0: Q_(+3.543224735e6, __unit),
            1: Q_(-2.076653674e6, __unit),
            2: Q_(-1.726380835e4, __unit),
            3: Q_(+8.100187504e4, __unit),
            4: Q_(-9.549151936e5, __unit),
            5: Q_(+3.779509560e6, __unit),
            6: Q_(-1.014008142e7, __unit),
            7: Q_(+4.331368592e6, __unit),
            8: Q_(-7.048791822e5, __unit),
            9: Q_(+8.736047692e4, __unit),
            10: Q_(-5.325634796e3, __unit),
        },
    }

    def __getitem__(self, key):
        component, index = key
        return self.__values[component][index]
