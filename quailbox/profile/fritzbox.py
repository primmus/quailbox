# Copyright (C) 2018 Cuckoo Foundation.

import glob2
import hashlib
import os
import tarfile
import tempfile

from quailbox.core.profile import Profile


class Fritzbox(Profile):
    def __init__(self, config_file=None):
        super(Fritzbox, self).__init__(config_file)

        image = self.config.get("image")
        if image:
            self.image = Image(image)

        self.config["opts"]["device"] = "virtio-blk-device,drive=rootfs"
        self.config["opts"]["drive"] = (
            "if=none,file=%s,format=raw,id=rootfs"
            % self.get_rootfs()
        )

    def get_rootfs(self):
        return self.image.get_rootfs()


class Image(object):
    def __init__(self, path):
        self.path = path

        def image_files(entries):
            for entry in entries:
                if entry.name.endswith(".image"):
                    yield entry

        with tarfile.open(path, "r") as tar:
            content = tar.fileobj.read()
            self.checksum = hashlib.md5(content).hexdigest()

            tmp = os.path.join(
                tempfile.gettempdir(),
                self.checksum,
            )

            for f in image_files(tar):
                tar.extract(f.name, path=tmp)

        self.files = {
            os.path.basename(image).split(".")[0]: image
            for image in glob2.glob("%s/**/*.image" % tmp)
        }

    def get_kernel(self):
        return self.files["kernel"]

    def get_rootfs(self):
        return self.files["filesystem"]
