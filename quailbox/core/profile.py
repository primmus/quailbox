# Copyright (C) 2018 Cuckoo Foundation.

import yaml


class Profile(object):
    config = {}

    def __init__(self, config_file):
        if config_file:
            with open(config_file, "r") as conf:
                self.config = yaml.load(conf)
