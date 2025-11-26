# http-request-cli

Minimal example project that exposes **two** command-line interfaces
for performing simple HTTP requests:

- `http-argparse`: implemented with the standard library `argparse`
- `http-typer`: implemented with `typer` (built on Click)

Both CLIs offer similar functionality so you can compare:

- Project structure
- Developer ergonomics
- Help output and UX

## Installation (editable)

```bash
uv pip install -e .
# or
pip install -e .
```

## Usage

Argparse version:

```bash
http-argparse https://httpbin.org/get -H "X-Demo: argparse"
```

Typer version:

```bash
http-typer request https://httpbin.org/get -H "X-Demo: typer"
```

This repository is intentionally small and focused so it can be used in
blog posts, talks, or training material comparing `argparse` and `typer`.
