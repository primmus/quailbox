# Copyright (C) 2018 Cuckoo Foundation.

import os

from quailbox.profile.fritzbox import Fritzbox


def test_config():
    fritz = Fritzbox("data/profiles/fritzbox.yml")
    config = {
        "arch": "arm",
        "image": "data/images/FRITZ.Box_7581.en-de-es-it-fr-pl.152.06.85.image",
        "init": "ifconfig eth0 192.168.3.20\n",
        "opts": {
            "append": "console=ttyS0 rw root=/dev/vda firmadyne.syscall=0",
            "device": [
                "virtio-blk-device,drive=rootfs",
                "virtio-net-device,netdev=net0",
            ],
            "display": "none",
            "drive": (
                "if=none,file=/tmp/20c3570af8c65996e0ee44a9bc571e75/"
                "var/tmp/filesystem.image,format=raw,id=rootfs"
            ),
            "kernel": "data/kernels/4.1.17-fr1tz",
            "M": "virt",
            "m": 512,
            "netdev": "tap,ifname=tap_qemu,script=no,downscript=no,id=net0",
            "nographic": None,
        }
    }

    if "TRAVIS" in os.environ:
        del config["opts"]["nographic"]
        config["opts"]["serial"] = "stdio"

    assert fritz.config == config


def test_rootfs():
    fritz = Fritzbox("data/profiles/fritzbox.yml")
    assert fritz.image.checksum == "20c3570af8c65996e0ee44a9bc571e75"
    assert fritz.get_rootfs() == (
        "/tmp/20c3570af8c65996e0ee44a9bc571e75/var/tmp/filesystem.image"
    )
