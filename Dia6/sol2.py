
with open("input.txt") as fl:
    lines = fl.readlines()
    rows = [[] for i in range(len(lines))]
    temps = ["" for i in range(len(lines))]
    print([len(l) for l in lines])
    for i in range(len(lines[0])):
        if all(lines[j][i] == ' ' for j in range(len(lines))):
            for j in range(len(lines)):
                rows[j].append(temps[j])
                temps[j] = ""
        else:
            for j in range(len(lines)):
                #print(j,i)
                temps[j] += lines[j][i]

print(rows[0])

tot = 0
for i in range(len(rows[0])):
    opp = rows[-1][i].strip()
    val = 1 if opp == '*' else 0
    for z in range(len(rows[0][i])-1,-1,-1):
        num = ""
        for j in range(len(rows) - 1):
            num += rows[j][i][z]
        
        if opp == '*':
            val *= int(num)
        else:
            val += int(num)
    tot += val
print(tot)
