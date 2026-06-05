from miraway_ai_agent_framework import Agent


def test_agent_run_returns_message():
    a = Agent()
    assert "Agent received" in a.run("hello")


def test_agent_uses_registered_tool():
    a = Agent()
    a.register_tool("echo", lambda x: f"echo:{x}")
    assert a.run("x") == "echo:x"


def test_tool_protocol_accepts_callable_tool():
    from miraway_ai_agent_framework.tool import Tool

    def my_tool(x):
        return x

    assert my_tool("ok") == "ok"
