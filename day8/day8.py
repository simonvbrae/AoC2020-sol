# importing the module
import doctest

# def solve_1(input):
#     """
#     >>> solve_1()
#     BFFFBBFRRR: row 70, column 7, seat ID 567.
#     >>> solve_1()
#     FFFBBBFRRR: row 14, column 7, seat ID 119.
#     >>> solve_1()
#     BBFFBBFRLL: row 102, column 4, seat ID 820.
#     """
#     result=0
#     return result


def solve(linenr, cur_accval, accvals, lines, can_change_ins):
    if linenr == len(lines):
        print("Program terminated with accval")
        print(cur_accval)
        return True
    if linenr in accvals:
        return False
    accvals[linenr] = cur_accval

    line = lines[linenr]

    op = line[:3]
    if op == "acc":
        return solve(linenr+1, cur_accval+int(line[4:]), accvals, lines, can_change_ins)

    else: # Op == "acc"
        inti = int(line[4:])
        if not can_change_ins:
            if op == "nop":
                return solve(linenr+1, cur_accval, accvals, lines, can_change_ins)
            return solve(linenr+inti, cur_accval, accvals, lines, can_change_ins)
        else:
            if op == "nop":
                if solve(linenr+1, cur_accval, accvals, lines, True):
                    return True
                else:
                    if solve(linenr+inti, cur_accval, accvals, lines, False):
                        return False
            if op == "jmp":
                if solve(linenr+inti, cur_accval, accvals, lines, True):
                    return True
                else:
                    return solve(linenr+1, cur_accval, accvals, lines, False)


def main():
    f=open("input", "r")
    lines=[line.strip() for line in f.readlines()]

    accvals=dict()
    linenr=0
    acc=0
    solve(0, 0, accvals, lines, True)
    f.close()

def main_2():
    f=open("input", "r")
    lines=[line.strip() for line in f.readlines()]

    accvals=dict()
    linenr=0
    acc=0
    while True:
        if linenr in accvals:
            print("duplicate")
            print(linenr)
            print("accval was")
            print(acc)
            return
        accvals[linenr] = acc

        line = lines[linenr]
        op = line[:3]
        if op == "jmp":
            inti = int(line[4:])
            linenr += inti
            continue
        if op == "acc":
            inti = int(line[4:])
            acc += inti
        linenr+=1

main_2()
main()