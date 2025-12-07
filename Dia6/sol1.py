
rows = []

with open("input.txt") as fl:
    for line in fl.readlines():
        temp = line.strip().split(' ')
        temp = [i for i in temp if i.isdigit() or i == '*' or i == '+']
        rows.append(temp)

tot = 0
for i in range(len(rows[0])):
    opp = rows[-1][i]
    val = 1 if opp == '*' else 0
    for j in range(len(rows) - 1):
        if opp == '*':
            val *= int(rows[j][i])
        else:
            val += int(rows[j][i])
    tot += val
print(tot)
