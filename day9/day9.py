preamb_len=25

def find_incorrect_number(number, numbers):
    for index,nr in enumerate(numbers):
        for nr_2 in numbers[index+1:]:
            if nr + nr_2 == number:
                return 0
    return number

# Original solution
def find_summing_set(number, numbers):
    for startindex, _ in enumerate(numbers):
        for endindex in range(startindex+1, len(numbers)):
            if sum(numbers[startindex: endindex]) == number:
                return numbers[startindex: endindex]
    return (0)

# Molto più veloce!
# Dynamic programming solution
def find_summing_set_dynamic(number, numbers):
    size = len(numbers)
    dp_matrix = [[-1+int(x==y) for x in range(size)] for y in range(size)]
    for startindex in range(0,size):
        for endindex in range(startindex+1,size):
            dp_matrix[startindex][endindex] = dp_matrix[startindex][endindex-1] + numbers[endindex]
            if dp_matrix[startindex][endindex] == number:
                return numbers[startindex: endindex]
    return (0)


def main():
    f=open("input", "r")
    lines=[int(l.strip()) for l in f.readlines()]
    for i, line in enumerate(lines[preamb_len:]):
        incorrect_nr = find_incorrect_number(line, lines[i:i+preamb_len])
        if incorrect_nr:
            print("incorrect number found: " + str(incorrect_nr))
            summing_set = find_summing_set_dynamic(incorrect_nr, lines[0:i+preamb_len])
            print("weakness: "+str(max(summing_set) + min(summing_set)))
main()