# Copyright (C) 2018 Cuckoo Foundation.

import pipes
import subprocess


class Qemu(object):
    argv0 = "quailbox-qemu"
    whitelist = [
        "arch", "kernel", "machine", "memory"
    ]

    def __init__(self, profile=None):
        self.profile = profile
        self.console = []

        if not self._verify_config():
            raise QemuException

        self.cmdline = "%s %s" % (self.argv0, self._format_opts())

    def _verify_config(self):
        self.config = self.profile.config
        return all(c in self.whitelist for c in self.config.keys())

    def _format_opts(self):
        return " ".join(
            "--%s %s" % (
                k, pipes.quote(str(v))
            ) for k, v in self.config.iteritems()
        )

    def run(self):
        # TODO implement streaming console
        self.console.append("[+] %s" % self.cmdline)

        # TODO implement quailbox-qemu command for argument translation
        subprocess.call(self.cmdline, shell=True)
        return self.console


class QemuException(Exception):
    pass
