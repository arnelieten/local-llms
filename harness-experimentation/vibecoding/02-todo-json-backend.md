# Task 2 — Todo UI + Local JSON Database

**Say in harness:** `do task 2`  
**Difficulty:** medium  
**Stack:** HTML/CSS/JS frontend + Flask backend + JSON file storage  
**Output folder:** [`02-todo-json-backend/`](02-todo-json-backend/) (create all files here)

---

## Prompt

Build a small full-stack todo app that persists todos in a **local JSON file**.

**Important:** write every generated file into the folder `vibecoding/02-todo-json-backend/`. Do not put files elsewhere. Do not modify this `.md` file.

Requirements:

1. **Backend (Flask):**
   - Single entrypoint `app.py` that serves the UI and a small REST API.
   - Persist todos to a file named `todos.json` in the same folder as `app.py`.
   - If `todos.json` does not exist, create it with an empty list `[]`.
   - Each todo is an object: `{ "id": <string or int>, "text": <string>, "done": <bool> }`.
   - Endpoints (or equivalent form posts — pick one style and stick to it):
     - list all todos
     - create a todo
     - toggle done
     - delete a todo
   - Start with: `python app.py` listening on `http://127.0.0.1:5000`.

2. **Frontend:**
   - Served by Flask (templates and/or static files).
   - User can add a todo, see the list, toggle done, and delete.
   - After a browser refresh, todos are still there (loaded from `todos.json`).

3. **Constraints:**
   - Use only Flask + the Python standard library for persistence (read/write JSON).
   - No SQLite, no external database.
   - Keep the project small: ideally `app.py`, one HTML template, optional CSS/JS.

Acceptance criteria:

- `python app.py` (from `02-todo-json-backend/`) starts without errors.
- Adding a todo writes it to `todos.json`.
- Restarting the server and refreshing the browser still shows the todos.
- Toggle and delete update `todos.json` correctly.
