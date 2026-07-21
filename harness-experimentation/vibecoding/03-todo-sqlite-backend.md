# Task 3 — Todo UI + SQLite Database

**Say in harness:** `do task 3`  
**Difficulty:** harder (same UI as Task 2, SQLite instead of JSON)  
**Stack:** HTML/CSS/JS frontend + Flask backend + SQLite  
**Output folder:** [`03-todo-sqlite-backend/`](03-todo-sqlite-backend/) (create all files here)

---

## Prompt

Build a small full-stack todo app that persists todos in a **SQLite** database.

**Important:** write every generated file into the folder `vibecoding/03-todo-sqlite-backend/`. Do not put files elsewhere. Do not modify this `.md` file.

Requirements:

1. **Backend (Flask):**
   - Single entrypoint `app.py` that serves the UI and a small REST API (or form-based routes).
   - Use SQLite via the Python standard library (`sqlite3`). Database file: `todos.db` next to `app.py`.
   - On startup, create the table if it does not exist:
     - `todos(id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT NOT NULL, done INTEGER NOT NULL DEFAULT 0)`
   - Support: list, create, toggle done, delete.
   - Start with: `python app.py` on `http://127.0.0.1:5000`.

2. **Frontend:**
   - Served by Flask.
   - User can add a todo, see the list, toggle done, and delete.
   - After a browser refresh (and after a server restart), todos are still there.

3. **Constraints:**
   - Flask + `sqlite3` only for storage (no SQLAlchemy required).
   - **Do not** use a JSON file for persistence.
   - Keep the project small: `app.py`, one HTML template, optional CSS/JS.

Acceptance criteria:

- `python app.py` (from `03-todo-sqlite-backend/`) starts without errors and creates `todos.db` if missing.
- CRUD operations update the SQLite table.
- Restarting the server preserves todos.
- The UI remains usable for the four operations above.
