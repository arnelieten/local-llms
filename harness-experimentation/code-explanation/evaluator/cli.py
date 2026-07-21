"""Command-line entrypoint for the expression evaluator."""

from __future__ import annotations

import sys

from .evaluator import evaluate
from .parser import ParseError
from .tokenizer import TokenizerError


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        print("usage: python -m evaluator.cli <expression>", file=sys.stderr)
        return 2

    source = " ".join(args)
    try:
        result = evaluate(source)
    except (TokenizerError, ParseError, ZeroDivisionError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    # Print ints without a trailing .0 when the value is integral.
    if float(result).is_integer():
        print(int(result))
    else:
        print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
