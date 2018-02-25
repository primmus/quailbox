# Copyright (C) 2018 Cuckoo Foundation.


class Qemu(object):
    def __init__(self, profile=None):
        self.profile = profile
        self.console = None

    def run(self):
        return self.console
