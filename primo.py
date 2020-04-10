#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import List
from math import sqrt


def is_prime(i: int) -> bool:
    if(i == 2):
        return True

    prime_vec: List[int] = [2]
    for j in range(3, int(sqrt(i))+2, 2):
        prime_vec.append(j)

    for j in prime_vec:
        if(i % j == 0):
            return False

    return True


def is_palindrome(s: str) -> bool:
    for i in range(0, int(len(s)/2)):
        if(s[i] is not s[len(s)-1-i]):
            return False

    return True


parser = ArgumentParser(description="Hello")

parser.add_argument("-n", "--number", type=int, help="Number to check")
parser.add_argument("-s", "--string", type=str, help="Word to check")

args = parser.parse_args()

exit_code: int = 0

if(args.number is not None):
    if(not is_prime(args.number)):
        exit_code |= 1

if(args.string is not None):
    if(not is_palindrome(args.string)):
        exit_code |= 2

exit(exit_code)
