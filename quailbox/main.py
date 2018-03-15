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
    old_tty = None
    p = load_profile(profile)
    has_stdin = isinstance(sys.stdin, file)

    q = Qemu(p)
    if has_stdin:
        old_tty = termios.tcgetattr(sys.stdin)

    if interactive:
        tty.setraw(sys.stdin.fileno())
        master_fd, slave_fd = pty.openpty()

        console = q.run(slave_fd)
        init = q.profile.config.get("init")
        interactive_mode(console, master_fd, init)
    else:
        console = q.run()
        bootlog_mode(console)

    if has_stdin:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_tty)
    q.stop(console.pid)


def load_profile(profile):
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

    return p


def interactive_mode(console, master_fd, init=None):
    booted = False
    while console.poll() is None:
        r, w, e = select.select([sys.stdin, master_fd], [], [], 2)
        if sys.stdin in r:
            d = os.read(sys.stdin.fileno(), 10240)

            # ESC key to quit
            if d[0] == "\x1b":
                if len(d) == 1:
                    break

            os.write(master_fd, d)
        elif master_fd in r:
            o = os.read(master_fd, 10240)
            if o:
                os.write(sys.stdout.fileno(), o)
        else:
            # When console goes quiet assume boot has completed.
            # Boot completion should be properly detected using VMI.
            if not booted:
                print "\r[+] system boot complete\r"
                booted = True
                if init:
                    print "\r[+] executing init script\r"
                    os.write(master_fd, init)


# TODO: keep this running as long as qemu runs
# using console.poll(). Provide option to write
# bootlog to file. Implement init script feeding.
def bootlog_mode(console):
    print "[+] {0} quailbox console {0}".format("-" * 29)
    for _ in xrange(10):
        print console.stdout.readline().rstrip("\r\n")[:79]


def qemu():
    argv = ["/usr/bin/qemu-system-arm"]
    argv.extend(sys.argv[1:])
    os.execve(argv[0], argv, {})
