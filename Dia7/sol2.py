lines = [line.strip() for line in open("input2.txt").readlines()]

starting_pos = lines[0].find("S")

tot = 0
searching_pos = {starting_pos:1}
for i in range(len(lines)-1):
    new_search_pos = dict()
    for pos in searching_pos:
        if lines[i+1][pos] == '^':
            if (pos-1) not in new_search_pos:
                new_search_pos[pos-1] = searching_pos[pos]
            else:
                new_search_pos[pos-1] += searching_pos[pos]

            if (pos+1) not in new_search_pos:
                new_search_pos[pos+1] = searching_pos[pos]
            else:
                new_search_pos[pos+1] += searching_pos[pos]
        else:
            if pos not in new_search_pos:
                new_search_pos[pos] = searching_pos[pos]
            else:
                new_search_pos[pos] += searching_pos[pos]
    searching_pos = new_search_pos

for val in searching_pos.values():
    tot += val
print(tot)