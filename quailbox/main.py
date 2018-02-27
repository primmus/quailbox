# Copyright (C) 2018 Cuckoo Foundation.

import click
import os
import sys

from quailbox.core.profile import Profile
from quailbox.machinery.qemu import Qemu
from quailbox.profile.fritzbox import Fritzbox


@click.command()
@click.option(
    "--profile", help="Name of profile to run.",
    default="fritzbox", required=True,
)
def main(profile):
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

    q = Qemu(p)
    pid, console = q.run()

    print "[+] {0} quailbox console {0}".format("-" * 29)
    for _ in xrange(10):
        print console.readline().rstrip("\r\n")[:79]

    q.stop(pid)
