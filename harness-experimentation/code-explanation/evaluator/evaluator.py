"""Evaluate an expression AST to a numeric result."""

from __future__ import annotations

from .cache import memoize
from .parser import BinaryOp, Expr, Number, UnaryOp, parse


class EvaluationError(ValueError):
    """Raised when evaluation fails for a semantic reason."""


def _eval_node(node: Expr) -> float:
    if isinstance(node, Number):
        return node.value

    if isinstance(node, UnaryOp):
        value = _eval_node(node.operand)
        if node.op == "+":
            return +value
        if node.op == "-":
            return -value
        raise EvaluationError(f"unknown unary operator {node.op!r}")

    if isinstance(node, BinaryOp):
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        if node.op == "+":
            return left + right
        if node.op == "-":
            return left - right
        if node.op == "*":
            return left * right
        if node.op == "/":
            # Division by zero propagates as ZeroDivisionError (not wrapped).
            return left / right
        raise EvaluationError(f"unknown binary operator {node.op!r}")

    raise EvaluationError(f"unknown node type {type(node)!r}")


@memoize(maxsize=8)
def evaluate(source: str) -> float:
    """Parse and evaluate an arithmetic expression string.

    Supports ``+ - * /``, parentheses, unary ``+/-``, and floating-point
    numbers. Operator precedence: ``* /`` bind tighter than ``+ -``.
    """
    tree = parse(source)
    return _eval_node(tree)
