# importing the module
import copy
import doctest

change={"#":"L","L":"#"}
def solve_1(seats):
    update_count=0
    newstate=copy.deepcopy(seats)
    for row, x in enumerate(seats):
        for seat, _ in enumerate(x):
            if seat == ".":
                continue
            if update_2((row, seat), seats):
                update_count+=1
                newstate[row]=newstate[row][:seat]+change[seats[row][seat]]+newstate[row][seat+1:]

    return newstate, update_count

adjacent=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
def update(seat, seats):
    (seat_r,seat_c)=seat
    count_full=0
    for (place_r, place_c) in adjacent:
        (spot_r, spot_c)=(seat_r + place_r, seat_c + place_c)
        if (is_inbounds((spot_r,spot_c), seats)):
            char=seats[spot_r][spot_c]
            count_full+=int(char=="#")
    if seats[seat_r][seat_c] == "#":
        return count_full >= 4 
    if seats[seat_r][seat_c] == "L":
        return count_full == 0


adjacent=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
def update_2(seat, seats):
    (seat_r,seat_c)=seat
    count_full=0
    count_empty=0
    for (place_r, place_c) in adjacent:
        (spot_r, spot_c)=(seat_r + place_r, seat_c + place_c)
        while is_inbounds((spot_r, spot_c), seats):
            if seats[spot_r][spot_c] != ".":
                char=seats[spot_r][spot_c]

                count_full+=int(char=="#")
                count_empty+=int(char=="L")
                break
            (spot_r, spot_c)=(spot_r + place_r, spot_c + place_c)

    if seats[seat_r][seat_c] == "#":
        return count_full >= 5
    if seats[seat_r][seat_c] == "L":
        return count_full == 0

def is_inbounds(seat, seats):
    return seat[0]>=0 and seat[0]<len(seats) and seat[1]>=0 and seat[1]<len(seats[0])


def main():
    f=open("input", "r")
    lines=[line.strip() for line in f.readlines()]

    # Iterate upto convergence
    amount_of_updates_in_previous_iteration=1
    cur_board=lines
    while amount_of_updates_in_previous_iteration>0:
        (cur_board,amount_of_updates_in_previous_iteration)=solve_1(cur_board)
        print("---------------")
        for row in cur_board:
            print(row)

 
    # Count amount occupied
    amount=0
    for line in cur_board:
        for seat in line:
            amount+=int(seat=='#')
    print(amount)

main()