# importing the module
import doctest
import collections
def solve_2(group):
    concatted=''.join(group)
    counted=collections.Counter(concatted)

    return sum([1 for let in counted.keys() if counted[let]==len(group)])

def solve(group):
    concatted=''.join(group)
    counted=collections.Counter(concatted)

    return len(counted.keys())


# invoking the testmod function
doctest.testmod(name='f1', verbose=True)

def main():
    f=open("input", "r")
    lines=[x.strip() for x in f.readlines()]

    counts_1=0
    counts_2=0
    group=[]
    for line in lines:
        if line == '':
            counts_1 += solve(group)
            counts_2 += solve_2(group)
            group=[]
        else:
            group.append(line)
    counts_1 += solve(group)
    counts_2 += solve_2(group)

    print(counts_1)
    print(counts_2)

main()