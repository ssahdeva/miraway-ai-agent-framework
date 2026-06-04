"""Core agent primitives."""

from dataclasses import dataclass, field
from typing import Protocol, runtime_checkable


@runtime_checkable
class Tool(Protocol):
    """Protocol for callable tools that an agent can invoke."""

    name: str

    def execute(self, input_text: str) -> str:
        """Execute the tool against a text input."""


@dataclass
class Agent:
    """Minimal agent base class for future expansion."""

    name: str
    description: str = ""
    tools: list[Tool] = field(default_factory=list)

    def add_tool(self, tool: Tool) -> None:
        """Register a tool with the agent."""
        self.tools.append(tool)

    def run(self, input_text: str) -> str:
        """Placeholder execution hook for an agent workflow."""
        if self.tools:
            tool_output = self.tools[0].execute(input_text)
            return f"{self.name} used {self.tools[0].name}: {tool_output}"

        return f"{self.name} received: {input_text}"
