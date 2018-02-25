# Copyright (C) 2018 Cuckoo Foundation.

import subprocess


class Qemu(object):
    whitelist = [
        "arch", "kernel", "machine", "memory"
    ]

    def __init__(self, profile=None):
        self.profile = profile
        self.console = []

        if not self._verify_config():
            raise QemuException

    def _verify_config(self):
        self.config = self.profile.config
        return all(c in self.whitelist for c in self.config.keys())

    def _format_opts(self):
        return " ".join(
            # TODO sanitize argv values (cmdline injection)
            "--%s %s" % (k, v) for k, v in self.config.iteritems()
        )

    def run(self):
        cmd = "quailbox-qemu %s" % self._format_opts()

        # TODO implement streaming console
        self.console.append("[+] %s" % cmd)

        # TODO implement quailbox-qemu command for argument translation
        subprocess.call(cmd, shell=True)

        return self.console


class QemuException(Exception):
    pass

