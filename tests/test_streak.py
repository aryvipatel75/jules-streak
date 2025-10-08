import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_single_streak():
    """Test a simple case with a single streak."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_multiple_streaks_longest_is_last():
    """Test with multiple streaks where the longest streak is at the end."""
    assert longest_positive_streak([1, 2, -1, 3, 4, 5]) == 3

def test_multiple_streaks_longest_is_first():
    """Test with multiple streaks where the longest streak is at the beginning."""
    assert longest_positive_streak([1, 2, 3, 4, -5, 1, 2]) == 4

def test_with_zeros():
    """Test that zeros correctly break a streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5]) == 3

def test_with_negatives():
    """Test that negative numbers correctly break a streak."""
    assert longest_positive_streak([1, -2, 3, -4, 5]) == 1

def test_all_non_positive():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -5, 0, -10]) == 0

def test_example_from_prompt():
    """Test the primary example given in the problem description."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_all_same_positive_number():
    """Test a streak of identical positive numbers."""
    assert longest_positive_streak([1, 1, 1]) == 3

def test_streak_at_the_end():
    """Test when the longest streak is at the very end of the list."""
    assert longest_positive_streak([-1, 0, 1, 2, 3, 4]) == 4