# Copyright (C) 2018 Cuckoo Foundation.

import click
import os
import pty
import select
import sys
import termios
import tty

from quailbox.core.profile import Profile
from quailbox.machinery.qemu import Qemu
from quailbox.profile.fritzbox import Fritzbox


@click.command()
@click.option(
    "--profile", help="Name of profile to run.",
    default="fritzbox", required=True,
)
@click.option(
    "--interactive", help="Enable interactive mode (ESC to quit).",
    default=False, required=False, is_flag=True,
)
def main(profile, interactive):
    profile = os.path.basename(profile).split(".")[0]
    config = "data/profiles/%s.yml" % os.path.basename(profile)

    try:
        if profile == "fritzbox":
            p = Fritzbox(config)
        else:
            p = Profile(config)
        print "[+] quailbox profile %s" % profile
    except IOError:
        print "[-] quailbox failed to load profile: %s" % profile
        sys.exit(-1)

    slave_fd = None
    has_stdin = isinstance(sys.stdin, file)

    if has_stdin:
        old_tty = termios.tcgetattr(sys.stdin)

    if interactive:
        tty.setraw(sys.stdin.fileno())
        master_fd, slave_fd = pty.openpty()

    q = Qemu(p)
    console = q.run(slave_fd)

    if not interactive:
        print "[+] {0} quailbox console {0}".format("-" * 29)
        for _ in xrange(10):
            print console.stdout.readline().rstrip("\r\n")[:79]
    else:
        while console.poll() is None:
            r, w, e = select.select([sys.stdin, master_fd], [], [])
            if sys.stdin in r:
                d = os.read(sys.stdin.fileno(), 10240)

                # ESC key to quit
                if d[0] == "\x1b":
                    break

                os.write(master_fd, d)
            elif master_fd in r:
                o = os.read(master_fd, 10240)
                if o:
                    os.write(sys.stdout.fileno(), o)

    if has_stdin:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_tty)
    q.stop(console.pid)


def qemu():
    argv = ["/usr/bin/qemu-system-arm"]
    argv.extend(sys.argv[1:])
    os.execve(argv[0], argv, {})
