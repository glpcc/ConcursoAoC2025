lines = [line.strip() for line in open("input.txt").readlines()]

starting_pos = lines[0].find("S")

tot = 0
searching_pos = {starting_pos}
for i in range(len(lines)-1):
    new_search_pos = set()
    for pos in searching_pos:
        if lines[i+1][pos] == '^':
            tot += 1
            new_search_pos.add(pos-1)
            new_search_pos.add(pos+1)
        else:
            new_search_pos.add(pos)
    searching_pos = new_search_pos

print(tot)