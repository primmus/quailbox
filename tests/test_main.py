# Copyright (C) 2018 Cuckoo Foundation.

from click.testing import CliRunner

from quailbox.main import main


def test_main():
    r = CliRunner()
    res = r.invoke(main, ["--profile", "fritzbox"])
    assert res.exit_code == 0

    res = r.invoke(main, ["--profile", "null"])
    assert res.exit_code == -1
