# Copyright (C) 2018 Cuckoo Foundation.

import mock

from quailbox.machinery.qemu import Qemu
from quailbox.profile.fritzbox import Fritzbox


# TODO #1 implement qemu wrapper
def test_qemu():
    qemu = Qemu(Fritzbox("data/profiles/fritzbox.yml"))
    assert isinstance(qemu.profile, Fritzbox)

    console = qemu.run()
    assert console == mock.ANY
