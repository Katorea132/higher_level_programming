#!/usr/bin/python3
"""This module holds the algorithm to solve the code
through backtrack
"""


def ValPos(table, y, x):
    """Returns False if not a valid position, true if so

    Args:
        table (list of lists): The table
        y (int): Positions in Y axis
        x (int): Position in X axis

    Returns:
        bool: true or false depending on if a valid position or not
    """
    return all((False if table[pos] is x or abs(table[pos] - x)
                is abs(pos - y) else True for pos in range(y)))


def PosTable(table, y):
    """Moves through the positions of the tables, mainly through Y
    Prints whenever a valid answer is found (meaning when Y reaches it's limit)

    Args:
        table (matrix): Holds the table of NxN
        y (int): Holds current position of Y axis
    """
    if y is len(table):
        print([[posY, table[posY]] for posY in range(len(table))])
        return

    for x in range(len(table)):
        if ValPos(table, y, x):
            table[y] = x
            PosTable(table, y + 1)

if __name__ == "__main__":
    import sys

    if len(sys.argv) is not 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            exit(1)
    except:
        print("N must be a number")
        exit(1)
    PosTable([0 for col in range(n)], 0)
