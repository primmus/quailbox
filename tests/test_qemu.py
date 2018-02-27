# Copyright (C) 2018 Cuckoo Foundation.

from quailbox.machinery.qemu import Qemu
from quailbox.profile.fritzbox import Fritzbox


def test_qemu():
    qemu = Qemu(Fritzbox("data/profiles/fritzbox.yml"))
    assert isinstance(qemu.profile, Fritzbox)
    assert qemu.argv0 == "quailbox-qemu"

    console = qemu.run()
    assert console.stdout.readline() == (
        "[    0.000000] Booting Linux on physical CPU 0x0\n"
    )

    qemu.stop(console.pid)
