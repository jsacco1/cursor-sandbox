#!/usr/bin/env python3
"""Day-2 sandbox: greet from the command line."""

import sys


def main() -> None:
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
