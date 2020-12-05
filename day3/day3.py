def slope(c, r):
    f=open("input", "r")
    lines=f.readlines()
    
    trees_encountered, row, col = 0, 0, 0
    while row < len(lines):
        trees_encountered+=int(lines[row][col%(len(lines[0])-1)] == "#")
        row+=r
        col+=c

    return trees_encountered

print(slope(3,1))
m=1
for i in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
    m*=slope(*i)
print(m)
