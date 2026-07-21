"""Simple memoization helper used by the evaluator."""

from __future__ import annotations

from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def memoize(maxsize: int = 128) -> Callable[[F], F]:
    """Cache return values keyed by ``str(args) + str(kwargs)``.

    When the cache is full, this implementation evicts the **most recently
    inserted** key (LIFO), not the least-recently used one. Callers that
    assume true LRU behaviour will see surprising misses under load.

    Cache keys are built from ``str(args)`` / ``str(kwargs)`` with **no
    normalization**, so semantically identical inputs that differ only by
    whitespace (e.g. ``"1+1"`` vs ``"1 + 1"``) do not share an entry.
    """

    if maxsize < 1:
        raise ValueError("maxsize must be >= 1")

    def decorator(func: F) -> F:
        cache: dict[str, Any] = {}
        order: list[str] = []

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = str(args) + str(kwargs)
            if key in cache:
                return cache[key]

            result = func(*args, **kwargs)

            if len(order) >= maxsize:
                # BUG / limitation: evicts the newest entry (LIFO), not LRU.
                evicted = order.pop()
                cache.pop(evicted, None)

            cache[key] = result
            order.append(key)
            return result

        wrapper.cache = cache  # type: ignore[attr-defined]
        wrapper.cache_order = order  # type: ignore[attr-defined]
        wrapper.cache_clear = lambda: (cache.clear(), order.clear())  # type: ignore[attr-defined]
        return wrapper  # type: ignore[return-value]

    return decorator
