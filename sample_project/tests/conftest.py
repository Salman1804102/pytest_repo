import pytest

@pytest.fixture
def sample_numbers():
    return [1, 2, 3]

def helper_assert_sum(nums):
    assert sum(nums) == 6

