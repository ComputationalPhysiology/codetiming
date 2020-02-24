import math
import time

import pytest

from codetiming import Timer, TimerCollection, TimerError


def test_error_if_timer_not_running():
    """Test that timer raises error if it is stopped before started"""
    t = Timer(name="error_if_timer_not_running")
    with pytest.raises(TimerError):
        t.stop()


def test_error_if_restarting_running_timer():
    """Test that restarting a running timer raises an error"""
    t = Timer(name="error_if_restarting_running_timer")
    t.start()
    with pytest.raises(TimerError):
        t.start()


def test_last_starts_as_nan():
    """Test that .last attribute is initialized as nan"""
    t = Timer(name="last_starts_as_nan")
    assert math.isnan(t.last)


def test_timer_sets_last():
    """Test that .last attribute is properly set"""
    with Timer(name="sets_last") as t:
        time.sleep(0.02)
    assert t.last >= 0.02


def test_timer_total_time():
    """Test that .last attribute is properly set"""
    t = Timer(name="total_time")
    sleeptime = 0.02
    for i in range(5):
        t.start()
        time.sleep(sleeptime)
        t.stop()
        assert t.total_time >= (i + 1) * sleeptime


def test_lap_time():
    """Test that .last attribute is properly set"""
    t = TimerCollection(name="lap_time")
    assert len(t.lap_times) == 0
    sleeptime = 0.02
    for i in range(5):
        t.start("0")
        time.sleep(sleeptime)
        t.stop("0")
        assert len(t.lap_times["0"]) == i + 1
        assert sleeptime <= t.lap_times["0"][-1] < sleeptime * 1.5


def test_multiple_timers():

    """Test that .last attribute is properly set"""
    t = TimerCollection(name="multiple_timers")
    # num_timers =
    assert len(t.lap_times) == 0
    sleeptime = 0.02
    for i in range(5):
        t.start("0")
        time.sleep(sleeptime)
        t.stop("0")
        assert len(t.lap_times["0"]) == i + 1
        assert sleeptime <= t.lap_times["0"][-1] < sleeptime * 1.5


if __name__ == "__main__":
    test_lap_time()
