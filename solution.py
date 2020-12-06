# importing the module
import doctest

def solve_1(input):
    """
    >>> solve_1()
    BFFFBBFRRR: row 70, column 7, seat ID 567.
    >>> solve_1()
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    >>> solve_1()
    BBFFBBFRLL: row 102, column 4, seat ID 820.
    """
    result=0
    return result


# invoking the testmod function
doctest.testmod(name='solve_1', verbose=True)

def main():
    f=open("input", "r")
    lines=f.readlines()

main()