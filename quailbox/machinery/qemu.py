# Copyright (C) 2018 Cuckoo Foundation.

import pipes
import subprocess


class Qemu(object):
    argv0 = "quailbox-qemu"
    whitelist = [
        "append", "kernel", "M", "m", "serial",
    ]

    def __init__(self, profile=None):
        self.profile = profile
        self.console = []

        if not self._verify_config():
            raise QemuException

        self.opts = self._format_opts()

    def _verify_config(self):
        self.config = self.profile.config
        return all(c in self.whitelist for c in self.config["opts"].keys())

    def _format_opts(self):
        opts = [self.argv0]
        for k, v in self.config["opts"].iteritems():
            opts.extend(("-%s" % k, pipes.quote(str(v))))
        return opts

    def _log_console(self, buf):
        self.console.extend([l for l in buf.split("\r\n") if l])

    def run(self):
        q = subprocess.Popen(
            self.opts,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        log, err = q.communicate()
        self._log_console(log)
        self._log_console(err)

        return self.console


class QemuException(Exception):
    pass
