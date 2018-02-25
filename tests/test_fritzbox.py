# Copyright (C) 2018 Cuckoo Foundation.

from quailbox.profile.fritzbox import Fritzbox


def test_fritzbox():
    fritz = Fritzbox("data/profiles/fritzbox.yml")
    assert fritz.config == {
        "arch": "arm",
        "memory": 512,
        "machine": "virt",
    }
