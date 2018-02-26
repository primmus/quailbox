# Copyright (C) 2018 Cuckoo Foundation.

from quailbox.profile.fritzbox import Fritzbox


def test_config():
    fritz = Fritzbox("data/profiles/fritzbox.yml")
    assert fritz.config == {
        "arch": "arm",
        "image": "data/images/FRITZ.Box_7581.en-de-es-it-fr-pl.152.06.85.image",
        "opts": {
            "append": "console=ttyS0 debug",
            "kernel": "data/kernels/4.1.17-fr1tz",
            "M": "virt",
            "m": 512,
            "serial": "stdio",
        }
    }


def test_rootfs():
    fritz = Fritzbox("data/profiles/fritzbox.yml")
    assert fritz.image.checksum == "20c3570af8c65996e0ee44a9bc571e75"
    assert fritz.get_rootfs() == (
        "/tmp/20c3570af8c65996e0ee44a9bc571e75/var/tmp/filesystem.image"
    )
