# Architecture

Methys separates presentation definitions from computation.

## Frontend

The Python `Frontend` object aggregates HTML, CSS, and JavaScript fragments.
It renders a document string; it does not start a server, own an event loop, or
impose a component framework. The application embedding Methys decides how that
document is delivered and how browser events reach its backend.

Because fragments are raw browser code, applications must sanitise untrusted
content before adding it.

## Inline data queries

`InlineQuery` is a Python-side request definition for PostgreSQL and MongoDB.
It does not open connections or execute queries. The native API defines the
supported dialects and will later own driver integration, safe parameter
binding, credential handling, execution, and result-buffer ownership. SQL and
MongoDB query documents must never be built by interpolating untrusted values;
callers should use the parameter channel instead.

## Native core

`native/` is the boundary for algorithms, data structures, memory management,
and numerical routines implemented in C. Its public C API lives under
`native/include/methys/`; code outside that directory must not depend on private
implementation details. The initial `methys_core_version` function is a build
and binding smoke-test target.

The Python `methys.native` module is intentionally a narrow seam for the future
binding layer. No calculation logic should be duplicated in Python once an
equivalent native implementation exists.
