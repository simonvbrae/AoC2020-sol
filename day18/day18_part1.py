# importing the module
import doctest
import regex as re

###
### Initial solution for part one
### Better solution in file for part two
###
number_regex = re.compile(r" [\+\*] [0-9]*$")
parens_regex = re.compile(r"^[^\(\)]*\((.*)\)$")
def solve_1(problem):
    """
    >>> solve_1("2 * 3")
    6
    >>> solve_1("2 * 3 + (4 * 5)")
    26
    >>> solve_1("5 + (8 * 3 + 9 + 3 * 4 * 3)")
    437
    >>> solve_1("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")
    12240
    >>> solve_1("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")
    13632
    >>> solve_1("(2 + 1) * (2 + 1)")
    9
    >>> solve_1("1 + 2 * 3 + 4 * 5 + 6")
    71
    >>> solve_1("1 + (2 * 3) + (4 * (5 + 6))")
    51
    """
    if len(problem) == 0:
        return 0
    if re.match(r"^[0-9]*$", problem):
        return int(problem)
    
    result=0
    number_match = re.findall(number_regex, problem)
    if number_match:
        op = number_match[0][1]
        num = int(number_match[0][2:])
        solved_firstpart = solve_1(problem[:-(len(number_match[0]))])
        if op == "*":
            result = num * solved_firstpart
        elif op == "+":
            result = num + solved_firstpart
    else:
        parenthesis_match = re.findall(parens_regex, problem)
        
        # Now find the substring ranging from the last unmatched opening parenthesis until the end of the string
        conts_startindex = find_last_unmatched_parens(parenthesis_match[0])
        if conts_startindex:
            parenthesis_match = [parenthesis_match[0][conts_startindex+1:]]

        # Replace the brackets with the result of the expression in the brackets
        result = solve_1(problem[:-(len(parenthesis_match[0])+2)]+str(solve_1(parenthesis_match[0])))

    return result

def find_last_unmatched_parens(s):
    conts_startindex = len(s)
    amount_closing_parens = 0
    amount_opening_parens = 0
    while conts_startindex>0 and amount_closing_parens >= amount_opening_parens:
        conts_startindex-=1
        amount_closing_parens += int(s[conts_startindex] == ')')
        amount_opening_parens += int(s[conts_startindex] == '(') 
    return conts_startindex

# invoking the testmod function
doctest.testmod(name='solve_1', verbose=True)

def main():
    f=open("input", "r")
    lines=[line.strip() for line in f.readlines()]
    
    s=0
    for line in lines:
        s += solve_1(line)
    print("- result:")
    print(s)

main()