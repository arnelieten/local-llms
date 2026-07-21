# Code explanation questions

Answer **Q1 through Q10 in order**. Use only the code in the `evaluator/` package.
Write your answers to `answers.md` in this folder. Do not modify the evaluator code.

The codebase is a small arithmetic expression evaluator:

- `tokenizer.py` — lexing
- `parser.py` — recursive-descent AST builder (precedence lives here)
- `evaluator.py` — tree walker + public `evaluate()`
- `cache.py` — `@memoize` decorator used by `evaluate`
- `cli.py` — CLI wrapper

You can check numeric behaviour with:

```bash
cd code-explanation
python -m evaluator.cli "2 * (3 + 4)"
```

---

## Q1 (easy — recall)

What does `evaluate("1 + 2")` return?

---

## Q2 (easy — locate)

Which file defines operator precedence for `+ -` vs `* /`?

---

## Q3 (easy–medium)

What does the `@memoize` decorator on `evaluate` cache, and what is used as the cache key?

---

## Q4 (medium — call path)

Walk the call path when evaluating `"2 * (3 + 4)"`, naming the main functions/methods involved from CLI (or `evaluate`) down to the numeric result.

---

## Q5 (medium)

How are unary minus and binary minus disambiguated? Where in the code does that decision happen?

---

## Q6 (medium — edge case)

What happens when evaluating `"1 / 0"`? Which exception surfaces, and is it wrapped by the evaluator?

---

## Q7 (medium — edge case)

What happens when evaluating a deeply nested but valid expression such as `"((((1+2)+3)+4)+5)"`? Does recursion depth become a practical concern for this codebase at normal sizes?

---

## Q8 (medium–hard — edge case)

What happens when the input contains an invalid character, e.g. `"2 + $"`? Which layer raises, and what exception type?

---

## Q9 (hard — bug / limitation)

There is a subtle limitation (or bug) in `cache.py`'s eviction policy and/or keying. Identify it and describe a concrete trigger that demonstrates surprising behaviour.

---

## Q10 (hard — extension design)

Propose how to add a new binary operator `^` meaning exponentiation (`2 ^ 3 == 8`), with higher precedence than `* /`. List every file that must change and what changes in each.
