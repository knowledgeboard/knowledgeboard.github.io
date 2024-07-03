#!/usr/bin/env python3

from __future__ import annotations

from argparse import ArgumentParser, ArgumentTypeError
import sys

TEMPLATE_PATH = "/home/marculonis/Desktop/Projects/knowledgeboard.github.io/templates/"

groups = ["ai","graphics","it","movies","other","school","vim","test","cern","brain"]

def get_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument(
        "-g",
        "--group",
        required=True,
        type=str,
        help=(
            f"Choose group to add to - available groups: " + " ".join(groups)
        ),
    )

    parser.add_argument(
        "-n",
        "--name",
        required=True,
        nargs='+',
        type=str,
        help=(
            f"Set name of the new item"
        ),
    )

    parser.add_argument(
        "-u",
        "--url",
        required=True,
        type=str,
        help=(
            f"Set url of the new item"
        ),
    )

    return parser


parser = get_parser()
if not len(sys.argv) == 1:
    args = parser.parse_args(sys.argv[1:])

    if not args.group in groups: raise ArgumentTypeError(f"Unknown group type - {args.group}")

    with open(TEMPLATE_PATH+args.group+".md", 'a') as f:
        f.write("["+" ".join(args.name)+"]"+f"({args.url})\n")
        print(f"Successfully written to {args.group}.md")
### INTERACTIVE MODE
else: 
    print("(interactive mode)")
    while True:
        print("- Group: ", end="")
        group = input()
        if not group in groups:
            print(f"Unknown group type - {group}")
            print(f"Choose group to add to - available groups: " + " ".join(groups))
            continue

        break

    print("- Name: ", end="")
    name = input()
    print("- URL: ", end="")
    url = input()

    with open(TEMPLATE_PATH+group+".md", 'a') as f:
        f.write(f"[{name}]({url})\n")
        print(f"Successfully written to {group}.md")
