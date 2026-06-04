"""Command-line entry point."""

import argparse

from .agent import Agent


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser."""

    parser = argparse.ArgumentParser(prog="miraway-agent")
    parser.add_argument("input_text", nargs="?", default="hello")
    parser.add_argument("--name", default="miraway")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    agent = Agent(name=args.name)
    print(agent.run(args.input_text))


if __name__ == "__main__":
    main()
