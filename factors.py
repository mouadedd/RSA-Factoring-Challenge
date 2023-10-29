#!/usr/bin/python3
from sys import argv


def sdivof(n):
    n = abs(n)
    for i in range(2, n + 1):
        if n % i == 0:
            return i
            break


def factors(x):
    q = sdivof(x)
    p = x // q
    print(f"{x}={p}*{q}")


if len(argv) != 2:
    exit()

try:
    with open(argv[1]) as file:
        sterr = file.readline()
        while sterr != "":
            x = int(sterr.strip())
            factors(x)
            sterr = file.readline()
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
