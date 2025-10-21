# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a LangChain-based agent project using Claude Sonnet 4.5 as the underlying model. The project demonstrates building an AI agent with custom tools.

## Development Setup

This project uses `uv` for dependency management and requires Python 3.12+.

**Install dependencies:**

```bash
uv sync
```

**Run the main agent:**

```bash
uv run python src/main.py
```

## Architecture

### Core Components

- **main.py**: Entry point containing the agent configuration and tool definitions
  - Uses `langchain.agents.create_agent()` to instantiate the agent
  - Model: `anthropic:claude-sonnet-4-5-20250929`
  - Tools are defined as Python functions with docstrings (LangChain converts them to tool schemas)
  - Agent is invoked with message dictionaries containing role and content

### Agent Configuration

The agent uses:

- **LangChain**: Framework for building the agent
- **langchain-anthropic**: Integration for Claude models
- **System prompt**: Customizable via the `system_prompt` parameter in `create_agent()`
- **Tools**: Functions decorated/passed to the agent that it can call during execution

### Adding New Tools

To add a tool to the agent:

1. Define a function with clear docstring (docstring becomes tool description)
2. Add type hints for parameters
3. Add the function to the `tools` list in `create_agent()`

Example:

```python
def my_tool(param: str) -> str:
    """Description of what this tool does."""
    return result
```

## Key Dependencies

- **langchain** (>=1.0.0a14): Agent framework
- **langchain-anthropic** (>=1.0.0a4): Claude model integration
