"""Main module
"""

import argparse

def main():
    print("Python template - main()")

    # Setup parsers
    parser = argparse.ArgumentParser(description="Template CLI")
    subparsers = parser.add_subparsers(dest="command")
    list_parser = subparsers.add_parser("list", help="List data")

    # Parse user input
    args = parser.parse_args()

    if args.command == "list":
        print("list action goes here")

if __name__ == "__main__":
    main()