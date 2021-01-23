import datetime

import pytest
from freezegun import freeze_time

from accounting.formatter import format_bs


@pytest.fixture
def bs_dict():
    return {"total_asset": "資産総額： 1,000,000", "liability": "負債総額： 100,000", "net_asset": "総資産： 900,000"}


@freeze_time("2021-01-01")
def test_format_bs(bs_dict):
    assert format_bs(bs_dict) == "2021-01-01\n資産総額： 1,000,000\n負債総額： 100,000\n総資産： 900,000"
