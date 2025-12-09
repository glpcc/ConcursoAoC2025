import math

points = [line.strip().split(',') for line in open("input.txt").readlines()]

points = [tuple([int(i) for i in point]) for point in points]



def calculate_distance(p1,p2):
    return math.sqrt(math.pow((p1[0]-p2[0]),2) + math.pow((p1[1]-p2[1]),2) + math.pow((p1[2]-p2[2]),2))

def distance_matrix(points):
    dmatrix = [[-1 for j in range(len(points))] for i in range(len(points))]
    for i,p1 in enumerate(points):
        for j,p2 in enumerate(points):
            dmatrix[i][j] = calculate_distance(p1,p2)
    
    return dmatrix

def pop_closest_pair(dmatrix,points):
    mind = math.inf
    min_pos = (0,0)
    for j,line in enumerate(dmatrix):
        for i,d in enumerate(line):
            if d < mind and i != j:
                min_pos = (j,i)
                mind = d
    # Pop the closest distance
    dmatrix[min_pos[0]][min_pos[1]] = math.inf
    dmatrix[min_pos[1]][min_pos[0]] = math.inf

    return dmatrix,points[min_pos[0]],points[min_pos[1]]

def calculate_graph_size(startp, connections):
    seen_points = set()
    size = 0
    points_to_see = [startp]
    while len(points_to_see) > 0:
        currentp = points_to_see.pop(0)
        if currentp in seen_points:
            continue
        else:
            seen_points.add(currentp)
        size += 1
        for conp in connections[currentp]:
            points_to_see.append(conp)
    return size, seen_points

dmatrix = distance_matrix(points)
connections = {p:[] for p in points}
num_steps = 1000
print(len(points))
for _ in range(num_steps):
    print(f"Step: {_}")
    dmatrix,p1,p2 = pop_closest_pair(dmatrix,points)
    connections[p1].append(p2)
    connections[p2].append(p1)

print(connections)
# Calculate numgraphs
graphs = []
not_seen_points = set(points)
for p in connections:
    if p in not_seen_points:
        size, seenp = calculate_graph_size(p,connections)
        graphs.append(size)
        not_seen_points -= seenp
    else:
        continue

graphs = sorted(graphs,reverse=True)
maxi = 3
print(graphs)
tot = 1
for i in graphs[:maxi]:
    tot *= i
print(tot)