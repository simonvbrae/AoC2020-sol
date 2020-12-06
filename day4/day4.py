# importing the module
import doctest
import regex as re

def solve_1(passport):
    print(passport)
    header_pattern = re.compile(r"[a-z][a-z][a-z]:")
    
    present_headers=[m[:-1] for m in re.findall(header_pattern, passport)]
    
    required_fields=['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
    for i in required_fields:
        if i not in present_headers:
            return False
    return True

def main():
    f=open("input", "r")
    lines=f.read().split("\n\n")

    valid_passport_amount=0
    for l in lines:
        valid_passport_amount+=int(solve_1(l))
    print(valid_passport_amount)

main()