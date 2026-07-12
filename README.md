# Methys-DS

Methys is a C-powered data and computation engine with a small Python API and
an HTML-first frontend definition layer. It is not a Streamlit application.

## Direction

- Native algorithms and stateful computation live in `native/` as C code.
- `src/methys/` exposes a Python API and eventually loads the native library.
- `Frontend` composes user-provided HTML blocks and optional CSS/JavaScript
  into a self-contained document. Serving it is intentionally left to the host
  application.
- `InlineQuery` describes PostgreSQL SQL or MongoDB document queries for
  execution by the native engine. Database drivers are not Python dependencies.

## Layout

```text
native/             C public headers, source, and CMake build definition
src/methys/         Python package and frontend definitions
tests/              Python API tests
docs/               Design notes and native build instructions
```

## Quick example

```python
from methys import Frontend, InlineQuery

page = Frontend(title="Methys")
page.add_html("<main><h1>Hello from Methys</h1></main>")
page.add_css("main { font-family: sans-serif; margin: 2rem; }")
document = page.render()

query = InlineQuery.postgres(
    "SELECT name FROM customers WHERE account_id = :account_id",
    {"account_id": 42},
)
```

Build the native library with CMake:

```sh
cmake -S native -B native/build
cmake --build native/build
```
