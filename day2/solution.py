# importing the module
import doctest

import collections
import regex

def is_valid_1(password, let, mi, ma):
    c = collections.Counter(password.strip())
    if c[let] > ma or c[let] < mi:
        return False
    return True

def is_valid_2(password, let, mi, ma):
    c=0
    c+=int(password[mi-1] == let)
    c+=int(password[ma-1] == let)

    return c == 1

def main():
    pattern = regex.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")

    f = open("input", "r")
    lines = [x.strip() for x in f.readlines()]

    c = 0
    for line in lines:
        mi, ma, letter, pw = pattern.match(line).groups()
        c += int(is_valid_1(pw, letter, int(mi), int(ma)))

    print(c)

main()
