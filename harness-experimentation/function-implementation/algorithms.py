"""Classic algorithm functions for harness evaluation.

Implement each function body. Do not change signatures or docstrings.
"""

from __future__ import annotations


def longest_increasing_subsequence(nums: list[int]) -> int:
    """Return the length of the longest strictly increasing subsequence.

    A subsequence is derived by deleting zero or more elements without
    changing the order of the remaining elements. Strictly increasing
    means each next value is greater than the previous.

    Args:
        nums: List of integers (may be empty or contain duplicates).

    Returns:
        Length of the LIS. ``0`` when ``nums`` is empty.

    Examples:
        >>> longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
        4
        >>> longest_increasing_subsequence([0, 1, 0, 3, 2, 3])
        4
    """
    raise NotImplementedError


def dijkstra(
    graph: dict[str, list[tuple[str, int]]],
    start: str,
) -> dict[str, int]:
    """Compute shortest-path distances from ``start`` using Dijkstra's algorithm.

    ``graph`` maps a node name to a list of ``(neighbor, weight)`` edges.
    Weights are non-negative integers. Nodes with no outgoing edges may
    be omitted from ``graph`` or mapped to an empty list.

    Args:
        graph: Adjacency list with non-negative edge weights.
        start: Source node. Must appear in the graph or be reachable as a key.

    Returns:
        Mapping from each reachable node (including ``start``) to the
        minimum distance from ``start``. Unreachable nodes are omitted.

    Examples:
        >>> g = {"A": [("B", 1), ("C", 4)], "B": [("C", 2)], "C": []}
        >>> dijkstra(g, "A")
        {'A': 0, 'B': 1, 'C': 3}
    """
    raise NotImplementedError


def edit_distance(a: str, b: str) -> int:
    """Compute the Levenshtein edit distance between ``a`` and ``b``.

    Allowed operations are single-character insert, delete, and substitute,
    each costing 1.

    Args:
        a: First string.
        b: Second string.

    Returns:
        Minimum number of edits to transform ``a`` into ``b``.

    Examples:
        >>> edit_distance("kitten", "sitting")
        3
        >>> edit_distance("", "abc")
        3
    """
    raise NotImplementedError
