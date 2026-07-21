# Task 1 — Frontend-only Todo (HTML/CSS)

**Say in harness:** `do task 1`  
**Difficulty:** simple  
**Stack:** HTML + CSS only (no JavaScript, no backend, no build step)  
**Output folder:** [`01-todo-frontend-only/`](01-todo-frontend-only/) (create all files here)

---

## Prompt

Build a single-file todo list **UI mock** using only HTML and CSS.

**Important:** write every generated file into the folder `vibecoding/01-todo-frontend-only/`. Do not put files elsewhere. Do not modify this `.md` file.

Requirements:

1. Create `index.html` inside `01-todo-frontend-only/` (CSS may be inline in a `<style>` tag, or a separate `styles.css` in the same folder).
2. The page must look like a todo app:
   - A clear title (e.g. "My Todos")
   - An input field and an "Add" button (visual only — no need for them to work)
   - A list of at least 3 sample todos already written in the HTML
   - Each sample todo shows: a checkbox (visual), the task text, and a delete control (visual, e.g. a button or ×)
3. Style it so it looks intentional: readable typography, spacing, a centered card/container, and a clear completed vs incomplete look for at least one item (e.g. strikethrough or muted color on one sample todo).
4. **No JavaScript.** Do not use `<script>`, frameworks, or external CDNs except optional system fonts.
5. **No backend.** Do not persist anything.

Acceptance criteria:

- Opening `01-todo-frontend-only/index.html` with Live Server shows a polished static todo UI.
- Browser console has **no errors**.
- HTML/CSS has **no syntax mistakes** that break rendering.
- Page remains usable at a typical laptop width (~1200px) without horizontal overflow.
