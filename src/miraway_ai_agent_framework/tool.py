"""Tool abstractions for the agent framework."""

from dataclasses import dataclass


@dataclass
class Tool:
    """Simple base class for concrete tools."""

    name: str
    description: str = ""

    def execute(self, input_text: str) -> str:
        """Execute the tool against text input.

        Subclasses should override this method.
        """

        raise NotImplementedError("Tool.execute() must be implemented by subclasses")