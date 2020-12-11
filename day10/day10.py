def count_possibilities_dp(adapters):
    dp_array = [1] + [0 for _ in range(adapters[-1])]
    print(len(dp_array))
    for i, e in enumerate(adapters):
        for i in range(max(0 ,e-3), e):
            dp_array[e] += dp_array[i]
    print(dp_array)


def main():
    f=open("input", "r")
    lines = sorted([0] + [int(line.strip()) for line in f.readlines()])
    lines.append(lines[-1]+3)
    print(lines)

    ones=0
    threes=1
    for ind, i in enumerate(lines[:-1]):
        if lines[ind+1] - i == 1:
            # print("one: {} {}".format(i, lines[ind+1]))
            ones+=1
        elif lines[ind+1] - i == 3:
            # print("threes " + str())
            threes+=1
    print(ones)
    print(threes)
    print(ones*threes)

    print(count_possibilities_dp(lines))



main()