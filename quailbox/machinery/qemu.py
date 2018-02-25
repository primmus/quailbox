# Copyright (C) 2018 Cuckoo Foundation.


class Qemu(object):
    whitelist = ["arch", "kernel", "machine", "memory"]

    def __init__(self, profile=None):
        self.profile = profile
        self.console = None

    def _verify_config(self):
        config = self.profile.config
        return all(c in self.whitelist for c in config.keys())

    def run(self):
        if not self._verify_config():
            raise QemuException
        return self.console


class QemuException(Exception):
    pass

