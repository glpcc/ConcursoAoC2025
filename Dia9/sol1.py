points = [l.split(',') for l in open('input.txt').readlines()]

points = [(int(x), int(y)) for x, y in points]

max_area = 0
for i, (x0, y0) in enumerate(points):
    for j, (x1, y1) in enumerate(points):
        if i != j:
            if x0 == x1 and y0 == y1:
                continue
            area = (abs(x1 - x0)+ 1) * (abs(y1 - y0) + 1)
            if area > max_area:
                max_area = area
print(max_area)