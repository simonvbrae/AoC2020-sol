# importing the module
import doctest

def f1(a1):
    """
    >>> f1()
    BFFFBBFRRR: row 70, column 7, seat ID 567.
    >>> f2()
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    >>> f3()
    BBFFBBFRLL: row 102, column 4, seat ID 820.
    """
    result=0
    return result


# invoking the testmod function
doctest.testmod(name='f1', verbose=True)

def main():
    f=open("input", "r")
    lines=f.readlines()

main()