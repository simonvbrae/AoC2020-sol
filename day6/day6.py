# importing the module
import doctest
import collections
def solve_2(group):
    amount_of_people=len(group)
    d=collections.defaultdict(lambda: 0)
    for line in group:
        for let in line:
            d[let] += 1

    return sum([1 for let in d.keys() if d[let]==amount_of_people])

def solve(group):
    d=collections.defaultdict(lambda: 0)
    for line in group:
        for let in line:
            d[let] = 1

    return len(d.keys())


# invoking the testmod function
doctest.testmod(name='f1', verbose=True)

def main():
    counts_1=[]
    counts_2=[]
    f=open("input", "r")
    lines=[x.strip() for x in f.readlines()]

    group=[]
    for line in lines:
        if line == '':
            counts_1.append(solve(group))
            counts_2.append(solve_2(group))
            group=[]
        else:
            group.append(line)
    counts_1.append(solve(group))
    counts_2.append(solve_2(group))

    print(sum(counts_1))
    print(sum(counts_2))

main()