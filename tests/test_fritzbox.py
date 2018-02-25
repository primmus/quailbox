# Copyright (C) 2018 Cuckoo Foundation.

from quailbox.profile.fritzbox import Fritzbox


# TODO #2 implement fritzbox poc
def test_fritzbox():
    fritz = Fritzbox("data/profiles/fritzbox.yml")
    assert fritz.config == {
        "arch": "arm",
        "memory": 512,
        "machine": "virt",
        "kernel": "4.1.17-fr1tz",
    }
