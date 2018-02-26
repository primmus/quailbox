# Copyright (C) 2018 Cuckoo Foundation.

from quailbox.core.profile import Profile


class Fritzbox(Profile):
    def __init__(self, config_file=None):
        super(Fritzbox, self).__init__(config_file)
