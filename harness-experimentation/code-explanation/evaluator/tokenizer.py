"""Lexer: turn an expression string into a flat list of tokens."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


class TokenType(Enum):
    NUMBER = auto()
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    LPAREN = auto()
    RPAREN = auto()
    EOF = auto()


@dataclass(frozen=True)
class Token:
    type: TokenType
    value: float | str | None
    position: int


_SINGLE = {
    "+": TokenType.PLUS,
    "-": TokenType.MINUS,
    "*": TokenType.STAR,
    "/": TokenType.SLASH,
    "(": TokenType.LPAREN,
    ")": TokenType.RPAREN,
}


class TokenizerError(ValueError):
    """Raised when the input contains an unexpected character."""


def tokenize(source: str) -> list[Token]:
    """Convert ``source`` into tokens.

    Numbers are parsed as floats (so ``3`` and ``3.14`` are both valid).
    Whitespace is ignored. Any other character raises ``TokenizerError``.
    """
    tokens: list[Token] = []
    i = 0
    n = len(source)

    while i < n:
        ch = source[i]

        if ch.isspace():
            i += 1
            continue

        if ch in _SINGLE:
            tokens.append(Token(_SINGLE[ch], ch, i))
            i += 1
            continue

        if ch.isdigit() or ch == ".":
            start = i
            has_dot = ch == "."
            i += 1
            while i < n and (source[i].isdigit() or source[i] == "."):
                if source[i] == ".":
                    if has_dot:
                        raise TokenizerError(f"invalid number at position {start}")
                    has_dot = True
                i += 1
            raw = source[start:i]
            try:
                number = float(raw)
            except ValueError as exc:
                raise TokenizerError(f"invalid number at position {start}") from exc
            tokens.append(Token(TokenType.NUMBER, number, start))
            continue

        raise TokenizerError(f"unexpected character {ch!r} at position {i}")

    tokens.append(Token(TokenType.EOF, None, n))
    return tokens
