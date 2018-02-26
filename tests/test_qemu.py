# Copyright (C) 2018 Cuckoo Foundation.

from quailbox.machinery.qemu import Qemu
from quailbox.profile.fritzbox import Fritzbox


def test_qemu():
    qemu = Qemu(Fritzbox("data/profiles/fritzbox.yml"))
    assert isinstance(qemu.profile, Fritzbox)
    assert qemu.argv0 == "quailbox-qemu"

    console = qemu.run()
    assert console[:2] == [
        "[    0.000000] Booting Linux on physical CPU 0x0\r",
        "[    0.000000] Linux version 4.1.17+ (sj0rz@kookoo)"
        " (gcc version 5.3.0 (GCC) ) #1 Mon Oct 2 14:03:05 CEST 2017\r",
    ]
