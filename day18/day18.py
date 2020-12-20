# importing the module
import doctest
import regex as re

###
### Better solution using graph representation
###
def new_node(operator, left, right):
    return (operator, left, right)

def calc_min_level_of_nesting(problem):
    min_lon=float('inf')
    lon=0
    for i in problem[::-1]:
        if i == ")":
            lon+=1
        elif i == '(':
            lon-=1
        elif lon < min_lon:
            min_lon = lon
    return min_lon

def to_graph(problem, operators):
    # Remove brackets
    if calc_min_level_of_nesting(problem)==1:
        problem=problem[1:-1]

    for operator in operators:
        lon=0
        for i in range(len(problem)-1,-1,-1):
            if problem[i] == ")":
                lon+=1
            if problem[i] == "(":
                lon-=1
            if problem[i] in operator and lon==0:
                return new_node(problem[i], to_graph(problem[0:i], operators), to_graph(problem[i+1:], operators))
    if problem.isdigit():
        return problem

def evaluate(graph):
    if graph[0].isdigit():
        return int(graph)
    left = evaluate(graph[1])
    right = evaluate(graph[2])
    return left * right if graph[0] == '*' else left+right

# invoking the testmod function
doctest.testmod(name='solve_1', verbose=True)

def main():
    f=open("input", "r")
    lines=[line.strip().replace(" ", "") for line in f.readlines()]

    ## Solve part one
    s=0
    for line in lines:
        s += evaluate(to_graph(line, [("*", "+")]))
    print("result part one:")
    print(s)
    
    ## Solve part two
    s=0
    for line in lines:
        s += evaluate(to_graph(line, ("*","+")))
    print("result part two:")
    print(s)
    

main()