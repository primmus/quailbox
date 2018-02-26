# Copyright (C) 2018 Cuckoo Foundation.

from quailbox.profile.fritzbox import Fritzbox


# TODO #2 implement fritzbox poc
def test_fritzbox():
    fritz = Fritzbox("data/profiles/fritzbox.yml")
    assert fritz.config == {
        "kernel": "data/kernels/4.1.17-fr1tz",
        "M": "virt",
        "m": 512,
    }
