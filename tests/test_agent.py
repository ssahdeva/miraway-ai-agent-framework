from miraway_ai_agent_framework import Agent, Tool


class EchoTool(Tool):
    def __init__(self) -> None:
        super().__init__(name="echo")

    def execute(self, input_text: str) -> str:
        return input_text.upper()


def test_agent_run_returns_message() -> None:
    agent = Agent(name="test-agent")

    assert agent.run("ping") == "test-agent received: ping"


def test_agent_uses_registered_tool() -> None:
    agent = Agent(name="test-agent")
    agent.add_tool(EchoTool())

    assert agent.run("ping") == "test-agent used echo: PING"


def test_tool_protocol_accepts_callable_tool() -> None:
    assert isinstance(EchoTool(), Tool)
