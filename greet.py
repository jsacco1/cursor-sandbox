#!/usr/bin/env python3
"""Day-2 sandbox: greet from the command line."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Greet someone by name.")
    parser.add_argument("--name", default="world", help="Name to greet (default: world)")
    args = parser.parse_args()
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
