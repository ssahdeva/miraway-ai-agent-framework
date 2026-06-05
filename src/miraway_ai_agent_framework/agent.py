from typing import Callable, Any, Dict


class Agent:
    def __init__(self) -> None:
        self.tools: Dict[str, Callable[..., Any]] = {}

    def register_tool(self, name: str, func: Callable[..., Any]) -> None:
        self.tools[name] = func

    def run(self, message: str = "") -> str:
        """Run the agent. If a tool is registered, call the first tool with the message."""
        if self.tools:
            first = next(iter(self.tools.values()))
            try:
                return str(first(message))
            except Exception:
                return "tool-error"
        return f"Agent received: {message}"
