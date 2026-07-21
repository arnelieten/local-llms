"""Tests for simple.py and algorithms.py.

These fail with NotImplementedError until a harness implements the stubs.
SDK functions are validated manually (credentials required).
"""

from __future__ import annotations

import pytest

from algorithms import dijkstra, edit_distance, longest_increasing_subsequence
from simple import chunk, is_palindrome, word_frequencies


class TestChunk:
    def test_even_split(self) -> None:
        assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]

    def test_remainder(self) -> None:
        assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

    def test_empty(self) -> None:
        assert chunk([], 3) == []

    def test_size_one(self) -> None:
        assert chunk(["a", "b"], 1) == [["a"], ["b"]]

    def test_invalid_size(self) -> None:
        with pytest.raises(ValueError):
            chunk([1, 2], 0)


class TestWordFrequencies:
    def test_basic(self) -> None:
        assert word_frequencies("Hello, hello world!") == {"hello": 2, "world": 1}

    def test_empty(self) -> None:
        assert word_frequencies("") == {}
        assert word_frequencies("   ") == {}

    def test_case_insensitive(self) -> None:
        assert word_frequencies("Foo FOO foo") == {"foo": 3}


class TestIsPalindrome:
    def test_classic(self) -> None:
        assert is_palindrome("A man, a plan, a canal: Panama") is True

    def test_not_palindrome(self) -> None:
        assert is_palindrome("race a car") is False

    def test_empty(self) -> None:
        assert is_palindrome("") is True
        assert is_palindrome("!!!") is True

    def test_simple(self) -> None:
        assert is_palindrome("racecar") is True
        assert is_palindrome("hello") is False


class TestLongestIncreasingSubsequence:
    def test_example(self) -> None:
        assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4

    def test_second_example(self) -> None:
        assert longest_increasing_subsequence([0, 1, 0, 3, 2, 3]) == 4

    def test_empty(self) -> None:
        assert longest_increasing_subsequence([]) == 0

    def test_decreasing(self) -> None:
        assert longest_increasing_subsequence([5, 4, 3, 2, 1]) == 1

    def test_strictly_increasing(self) -> None:
        assert longest_increasing_subsequence([1, 2, 3, 4]) == 4


class TestDijkstra:
    def test_basic(self) -> None:
        g = {"A": [("B", 1), ("C", 4)], "B": [("C", 2)], "C": []}
        assert dijkstra(g, "A") == {"A": 0, "B": 1, "C": 3}

    def test_unreachable_omitted(self) -> None:
        g = {"A": [("B", 1)], "B": [], "Z": []}
        result = dijkstra(g, "A")
        assert result == {"A": 0, "B": 1}
        assert "Z" not in result

    def test_start_only(self) -> None:
        assert dijkstra({"A": []}, "A") == {"A": 0}


class TestEditDistance:
    def test_kitten_sitting(self) -> None:
        assert edit_distance("kitten", "sitting") == 3

    def test_empty(self) -> None:
        assert edit_distance("", "abc") == 3
        assert edit_distance("abc", "") == 3
        assert edit_distance("", "") == 0

    def test_identical(self) -> None:
        assert edit_distance("same", "same") == 0
