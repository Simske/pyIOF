import datetime

import pytest
from pydantic import TypeAdapter

from pyiof.xml_base import FlexDatetime, FlexTime


def test_dot_format_datetime():
    ta = TypeAdapter(FlexDatetime)
    assert ta.validate_python("2026-03-01T00.00.00") == datetime.datetime(2026, 3, 1, 0, 0, 0)
    assert ta.validate_python("2026-03-01T10.38.15") == datetime.datetime(2026, 3, 1, 10, 38, 15)
    # Standard colon format still works
    assert ta.validate_python("2026-03-01T00:00:00") == datetime.datetime(2026, 3, 1, 0, 0, 0)


def test_dot_format_time():
    ta = TypeAdapter(FlexTime)
    assert ta.validate_python("16.38.15") == datetime.time(16, 38, 15)
    assert ta.validate_python("16:38:15") == datetime.time(16, 38, 15)
