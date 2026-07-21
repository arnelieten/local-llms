"""Recursive-descent parser with operator precedence.

Grammar (informal):

    expression  := term (("+" | "-") term)*
    term        := unary (("*" | "/") unary)*
    unary       := ("+" | "-") unary | primary
    primary     := NUMBER | "(" expression ")"
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from .tokenizer import Token, TokenType, tokenize


class ParseError(ValueError):
    """Raised when tokens do not form a valid expression."""


@dataclass
class Number:
    value: float


@dataclass
class UnaryOp:
    op: str
    operand: "Expr"


@dataclass
class BinaryOp:
    op: str
    left: "Expr"
    right: "Expr"


Expr = Union[Number, UnaryOp, BinaryOp]


class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self._tokens = tokens
        self._index = 0

    def parse(self) -> Expr:
        expr = self._expression()
        if self._peek().type is not TokenType.EOF:
            tok = self._peek()
            raise ParseError(f"unexpected token {tok.type.name} at position {tok.position}")
        return expr

    def _expression(self) -> Expr:
        # Lower precedence: + -
        node = self._term()
        while self._match(TokenType.PLUS, TokenType.MINUS):
            op = self._previous().value
            assert isinstance(op, str)
            right = self._term()
            node = BinaryOp(op, node, right)
        return node

    def _term(self) -> Expr:
        # Higher precedence: * /
        node = self._unary()
        while self._match(TokenType.STAR, TokenType.SLASH):
            op = self._previous().value
            assert isinstance(op, str)
            right = self._unary()
            node = BinaryOp(op, node, right)
        return node

    def _unary(self) -> Expr:
        # Unary +/- are distinguished from binary here: they appear before
        # a primary / another unary, not between two terms.
        if self._match(TokenType.PLUS, TokenType.MINUS):
            op = self._previous().value
            assert isinstance(op, str)
            return UnaryOp(op, self._unary())
        return self._primary()

    def _primary(self) -> Expr:
        if self._match(TokenType.NUMBER):
            value = self._previous().value
            assert isinstance(value, float)
            return Number(value)

        if self._match(TokenType.LPAREN):
            expr = self._expression()
            if not self._match(TokenType.RPAREN):
                tok = self._peek()
                raise ParseError(f"expected ')' at position {tok.position}")
            return expr

        tok = self._peek()
        raise ParseError(f"expected expression at position {tok.position}")

    def _match(self, *types: TokenType) -> bool:
        if self._peek().type in types:
            self._advance()
            return True
        return False

    def _advance(self) -> Token:
        tok = self._tokens[self._index]
        if tok.type is not TokenType.EOF:
            self._index += 1
        return tok

    def _previous(self) -> Token:
        return self._tokens[self._index - 1]

    def _peek(self) -> Token:
        return self._tokens[self._index]


def parse(source: str) -> Expr:
    """Tokenize and parse ``source`` into an AST."""
    return Parser(tokenize(source)).parse()
