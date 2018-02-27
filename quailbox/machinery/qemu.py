# Copyright (C) 2018 Cuckoo Foundation.

import os
import subprocess


class Qemu(object):
    argv0 = "quailbox-qemu"
    whitelist = [
        "append", "device", "drive", "kernel", "M", "m", "display", "serial",
    ]

    def __init__(self, profile=None):
        self.console = []
        self.procs = {}
        self.profile = profile

        if not self._verify_config():
            raise QemuException

        self.opts = self._format_opts()

    def _verify_config(self):
        self.config = self.profile.config
        return all(c in self.whitelist for c in self.config["opts"].keys())

    def _format_opts(self):
        opts = [self.argv0]
        for k, v in self.config["opts"].iteritems():
            opts.extend(("-%s" % k, (str(v))))
        return opts

    def _log_console(self, buf):
        self.console.extend([l for l in buf.split("\r\n") if l])

    def run(self, slave_fd=None):
        if slave_fd:
            q = subprocess.Popen(
                self.opts,
                preexec_fn=os.setsid,
                stdin=slave_fd,
                stdout=slave_fd,
                stderr=slave_fd,
                universal_newlines=True,
            )
        else:
            q = subprocess.Popen(
                self.opts,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
            )

        self.procs[q.pid] = q
        return q

    def stop(self, pid):
        proc = self.procs.get(pid)
        if proc:
            proc.kill()


class QemuException(Exception):
    pass
