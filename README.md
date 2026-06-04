# miraway-ai-agent-framework

A minimal starting point for a general-purpose AI agent framework written in Python.

## Purpose

This repository is initialized as a lightweight foundation for experimenting with agent-based automation, orchestration, and tool-using workflows.

## Planned direction

- Python-based agent framework
- Clear structure for future agent, tool, and workflow modules
- Room to add tests, packaging, and CI later

## Getting started

Install the project in editable mode with development dependencies:

```bash
pip install -e .[dev]
```

Run the CLI:

```bash
miraway-agent "hello world"
```

Or run it as a module:

```bash
python -m miraway_ai_agent_framework "hello world"
```

Run tests:

```bash
pytest
```

Run linting:

```bash
ruff check src tests
```

## Next steps

1. Add a source package structure.
2. Define the first agent use case.
3. Extend the framework with workflow, memory, and tool orchestration primitives.
