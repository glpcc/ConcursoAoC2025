import math
import numpy as np
import time

points = [line.strip().split(',') for line in open("input.txt").readlines()]

points = [tuple([int(i) for i in point]) for point in points]




def distance_matrix(points):
    npoints = np.array(points)
    dmatrix = np.linalg.norm(npoints[:, np.newaxis] - npoints[np.newaxis, :], axis=2)
    # Mask diagonal to avoid self-distances
    np.fill_diagonal(dmatrix, math.inf)
    return dmatrix

def pop_closest_pair(dmatrix,points):
    # Find minimum distance and its position
    min_pos = np.unravel_index(np.argmin(dmatrix), dmatrix.shape)
    # Set distances to infinity
    dmatrix[min_pos[0]][min_pos[1]] = math.inf
    dmatrix[min_pos[1]][min_pos[0]] = math.inf

    return dmatrix,points[min_pos[0]],points[min_pos[1]]



dmatrix = distance_matrix(points)
print(dmatrix.shape)
graphs =[{p} for p in points]
print(graphs)
while len(graphs) > 1:
    #print([len(i) for i in graphs])
    dmatrix,p1,p2 = pop_closest_pair(dmatrix,points)
    indexp1 = -1
    indexp2 = -1
    for i,g in enumerate(graphs):
        if p1 in g:
            indexp1 = i
        if p2 in g:
            indexp2 = i
    #print(indexp1,indexp2)
    if indexp1 == indexp2:
        continue
    else:
        newg = graphs[indexp1] | graphs[indexp2]
        if indexp1 > indexp2:
            graphs.pop(indexp1)
            graphs.pop(indexp2)
        else:
            graphs.pop(indexp2)
            graphs.pop(indexp1)
        graphs.append(newg)
print(p1,p2)
print(p1[0]*p2[0])