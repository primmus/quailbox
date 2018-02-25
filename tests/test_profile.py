# Copyright (C) 2018 Cuckoo Foundation.

from quailbox.core.profile import Profile


def test_profile():
    p = Profile(None)
    assert p.config == {}
