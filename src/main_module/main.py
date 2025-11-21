"""Main module
"""

import argparse

def main():
    print("Python template - main()")

    parser = argparse.ArgumentParser(description="Template CLI")
    subparsers = parser.add_subparsers(dest="command")
    list_parser = subparsers.add_parser("list", help="List data")

    args = parser.parse_args()

    if args.command == "list":
        print("list action goes here")

if __name__ == "__main__":
    main()