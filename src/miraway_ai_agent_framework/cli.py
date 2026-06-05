from .agent import Agent


def main() -> None:
    a = Agent()
    print(a.run("hello"))
