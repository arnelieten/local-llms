# Harness Experimentation

Tasks for a coding agent. Open this folder in your harness and run a task.

**Model under test:** local via Ollama (same setup for every harness).  
Same prompts for every harness — only the harness changes.

---

## How to run a task

Type one of:

| You type      | What it means                              |
| ------------- | ------------------------------------------ |
| **do task 1** | Vibecoding Tier 1 — frontend-only todo     |
| **do task 2** | Vibecoding Tier 2 — todo UI + JSON file DB |
| **do task 3** | Vibecoding Tier 3 — todo UI + SQLite DB    |
| **do task 4** | Function implementation — fill all stubs   |
| **do task 5** | Code explanation — answer all 10 questions |

If needed, paste the instruction under each task below.

---

## Task list

### Task 1 — Vibecoding: frontend-only todo

- **Prompt:** [`vibecoding/01-todo-frontend-only.md`](vibecoding/01-todo-frontend-only.md)
- **Write files into:** [`vibecoding/01-todo-frontend-only/`](vibecoding/01-todo-frontend-only/)

> Read `vibecoding/01-todo-frontend-only.md` and implement the Prompt section. Put all generated files only in `vibecoding/01-todo-frontend-only/`. Do not modify the `.md` file.

### Task 2 — Vibecoding: UI + JSON backend

- **Prompt:** [`vibecoding/02-todo-json-backend.md`](vibecoding/02-todo-json-backend.md)
- **Write files into:** [`vibecoding/02-todo-json-backend/`](vibecoding/02-todo-json-backend/)

> Read `vibecoding/02-todo-json-backend.md` and implement the Prompt section. Put all generated files only in `vibecoding/02-todo-json-backend/`. Do not modify the `.md` file.

### Task 3 — Vibecoding: UI + SQLite backend

- **Prompt:** [`vibecoding/03-todo-sqlite-backend.md`](vibecoding/03-todo-sqlite-backend.md)
- **Write files into:** [`vibecoding/03-todo-sqlite-backend/`](vibecoding/03-todo-sqlite-backend/)

> Read `vibecoding/03-todo-sqlite-backend.md` and implement the Prompt section. Put all generated files only in `vibecoding/03-todo-sqlite-backend/`. Do not modify the `.md` file.

### Task 4 — Function implementation

- **Files:** [`function-implementation/`](function-implementation/) (`simple.py`, `algorithms.py`, `sdk_functions.py`)
- **Secrets:** read `OPENAI_API_KEY`, `GCP_PROJECT_ID`, and `GCP_PROJECT_NUMBER` from [`.env`](.env) — never hard-code them

> Implement the function bodies in `function-implementation/simple.py`, `algorithms.py`, and `sdk_functions.py`. Do not change signatures or docstrings. Leave `raise NotImplementedError` only if you cannot implement a function. Read `OPENAI_API_KEY`, `GCP_PROJECT_ID`, and `GCP_PROJECT_NUMBER` from `.env`; never hard-code keys.

### Task 5 — Code explanation

- **Code:** [`code-explanation/evaluator/`](code-explanation/evaluator/)
- **Questions:** [`code-explanation/questions.md`](code-explanation/questions.md)
- **Write answers to:** [`code-explanation/answers.md`](code-explanation/answers.md)

> Read `code-explanation/questions.md` and answer Q1 through Q10 in order, using only the code in `code-explanation/evaluator/`. Write answers to `code-explanation/answers.md`. Do not modify the evaluator code.

---

## Folder layout

```
harness-experimentation/
  README.md
  .env
  vibecoding/
    01-todo-frontend-only.md
    01-todo-frontend-only/
    02-todo-json-backend.md
    02-todo-json-backend/
    03-todo-sqlite-backend.md
    03-todo-sqlite-backend/
  function-implementation/
    simple.py
    algorithms.py
    sdk_functions.py
    requirements.txt
    tests/
  code-explanation/
    evaluator/
    questions.md
    answers.md          # you create this for task 5
```
