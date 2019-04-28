import pytest

from Problem_001.sumcheck import SumCheck


@pytest.fixture
def sum_check():
    return SumCheck([10, 15, 3, 7])


def test_1(sum_check):
    assert sum_check.isSum(17) is True


def test_2(sum_check):
    assert sum_check.isSum(18) is True


def test_3(sum_check):
    assert sum_check.isSum(19) is False
