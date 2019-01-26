#!/usr/bin/env python
"""mixture module."""

import vdi4670
import vdi4670.mixture


def main():
    p = vdi4670.Q_(1.0, vdi4670.ureg.bar)
    t = vdi4670.Q_(20, vdi4670.ureg.celsius)

    air = vdi4670.mixture.Mixture.init_iso_air()
    print(str(air))
    print(repr(air))
    print()

    print(f"M_mix = {air.molar_mass()}")
    print(f"rho = {air.density(p, t)}")
    print(f"c_p = {air.heat_capacity(t)}")
    print(f"h_mix = {air.enthalpy(t)}")
    print(f"s_mix = {air.entropy(p, t)}")


if __name__ == "__main__":
    main()
