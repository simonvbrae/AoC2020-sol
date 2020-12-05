# importing the module
import doctest

def id_to_seat(id_s):
    """
    >>> id_to_seat("BFFFBBFRRR")
    BFFFBBFRRR: row 70, column 7, seat ID 567.
    >>> id_to_seat("FFFBBBFRRR")
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    >>> id_to_seat("BBFFBBFRLL")
    BBFFBBFRLL: row 102, column 4, seat ID 820.
    """
    id=0

    row=0
    exp=64
    for let in id_s[0:7]:
        if let == "F":
            row+=0
        elif let == "B":
            row+=exp
        exp/=2

    col=0
    exp=4
    for let in id_s[7:]:
        if let == "L":
            col+=0
        elif let == "R":
            col+=exp
        exp/=2


    # for letter in id[5:7]:

    id=row*8 + col
    print(f"{id}: row {int(row)}, column {int(col)}, seat ID {id}.")
    return id


# invoking the testmod function
doctest.testmod(name='id_to_seat', verbose=True)

def main():
    print("ok")
    f=open("input", "r")
    lines=f.readlines()

    seats=list(range(1000))
    m=0
    for l in lines:
        x=id_to_seat(l)
        if x > m:
            m=x
        seats.remove(x)

    print(seats)

main()