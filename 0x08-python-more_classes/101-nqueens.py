#!/usr/bin/python3


import sys


def nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def solve(queens, xy_diff, xy_sum):
        x = len(queens)
        if x == n:
            solutions.append(queens)
            return
        for y in range(n):
            if y not in queens and x-y not in xy_diff and x+y not in xy_sum:
                solve(queens+[y], xy_diff+[x-y], xy_sum+[x+y])

    solutions = []
    solve([], [], [])
    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    nqueens(n)
