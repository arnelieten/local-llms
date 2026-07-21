"""Simple utility functions for harness evaluation.

Implement each function body. Do not change signatures or docstrings.
"""

from __future__ import annotations


def chunk(items: list, size: int) -> list[list]:
    """Split ``items`` into consecutive sublists of length ``size``.

    The final chunk may be shorter if ``len(items)`` is not divisible by
    ``size``.

    Args:
        items: Sequence to split.
        size: Maximum length of each chunk. Must be >= 1.

    Returns:
        A list of chunks. Returns ``[]`` when ``items`` is empty.

    Raises:
        ValueError: If ``size`` is less than 1.

    Examples:
        >>> chunk([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
    """
    raise NotImplementedError


def word_frequencies(text: str) -> dict[str, int]:
    """Count how often each word appears in ``text``.

    Words are sequences of alphanumeric characters. Matching is
    case-insensitive; keys in the result are lowercased. Punctuation
    is ignored (treated as a separator).

    Args:
        text: Input string.

    Returns:
        Mapping from lowercase word to occurrence count. Empty dict for
        empty or whitespace-only input.

    Examples:
        >>> word_frequencies("Hello, hello world!")
        {'hello': 2, 'world': 1}
    """
    raise NotImplementedError


def is_palindrome(s: str) -> bool:
    """Return whether ``s`` is a palindrome, ignoring case and non-alphanumeric characters.

    Args:
        s: Input string.

    Returns:
        ``True`` if the alphanumeric characters of ``s`` read the same
        forwards and backwards (case-insensitive); otherwise ``False``.
        An empty string (or a string with no alphanumeric characters)
        is considered a palindrome.

    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("race a car")
        False
    """
    raise NotImplementedError
