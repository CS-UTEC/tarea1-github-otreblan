#!/usr/bin/env python3

from argparse import ArgumentParser

parser = ArgumentParser(description="Hello")

parser.add_argument("name", metavar="NAME", type=str)

args = parser.parse_args()

print("Hello "+args.name+"!")
