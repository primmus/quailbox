# Copyright (C) 2018 Cuckoo Foundation.

from quailbox.profile.fritzbox import Fritzbox


# TODO #2 implement fritzbox poc
def test_fritzbox():
    fritz = Fritzbox("data/profiles/fritzbox.yml")
    assert fritz.config == {
        "arch": "arm",
        "image": "data/images/FRITZ.Box_7581.en-de-es-it-fr-pl.152.06.85.image",
        "opts": {
            "kernel": "data/kernels/4.1.17-fr1tz",
            "M": "virt",
            "m": 512,
        }
    }
