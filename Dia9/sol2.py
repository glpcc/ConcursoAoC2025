points = [l.split(',') for l in open('input.txt').readlines()]

points = [(int(x), int(y)) for x, y in points]

print("Points:", points)
vertical_lines = []
horizontal_lines = []
for (x0,y0), (x1,y1) in zip(points[:-1], points[1:]):
    if x0 == x1:
        vertical_lines.append((x0, min(y0,y1), max(y0,y1)))
    elif y0 == y1:
        horizontal_lines.append((y0, min(x0,x1), max(x0,x1)))

# Add last line
(x0,y0), (x1,y1) = points[-1], points[0]
print((x0,y0), (x1,y1))
if x0 == x1:
    vertical_lines.append((x0, min(y0,y1), max(y0,y1)))
elif y0 == y1:
    horizontal_lines.append((y0, min(x0,x1), max(x0,x1)))

range_x = (min(x for x, y in points), max(x for x, y in points))
range_y = (min(y for x, y in points), max(y for x, y in points))
print(vertical_lines)
print(horizontal_lines)



def is_inside(x, y):
    # Check if point is on the boundary
    # Check vertical lines
    for x_line, y_start, y_end in vertical_lines:
        if x_line == x and y_start <= y <= y_end:
            return True
    # Check horizontal lines
    for y_line, x_start, x_end in horizontal_lines:
        if y_line == y and x_start <= x <= x_end:
            return True
    
    # Ray casting algorithm: cast a ray from (x,y) to the right
    # Count how many times it crosses the polygon boundary
    crossings = 0
    for x_line, y_start, y_end in vertical_lines:
        # Check if the vertical line is to the right of the point
        if x_line > x:
            # Only count if y is strictly between endpoints
            if y_start < y <= y_end:
                crossings += 1
    return crossings % 2 == 1

# To test
max_area = 0
for p1 in points:
    for p2 in points:
        if p1 == p2:
            continue
        # Check all 4 corners are inside
        corners = [
            (min(p1[0], p2[0]), min(p1[1], p2[1])),
            (min(p1[0], p2[0]), max(p1[1], p2[1])),
            (max(p1[0], p2[0]), min(p1[1], p2[1])),
            (max(p1[0], p2[0]), max(p1[1], p2[1])),
        ]
        all_inside = all(is_inside(x, y) for x, y in corners)
        
        # Check if any polygon edges intersect the rectangle
        intersects = False
        rect_x1, rect_x2 = min(p1[0], p2[0]), max(p1[0], p2[0])
        rect_y1, rect_y2 = min(p1[1], p2[1]), max(p1[1], p2[1])
        
        # Check if any vertical line of the polygon crosses through the rectangle interior
        for x_line, y_start, y_end in vertical_lines:
            # Vertical line crosses horizontally through the rectangle interior (not on boundary)
            if rect_x1 < x_line < rect_x2:
                # Check if it intersects vertically (crosses through, not just touches)
                if y_start < rect_y2 and y_end > rect_y1:
                    intersects = True
                    break
        
        # Check if any horizontal line of the polygon crosses through the rectangle interior
        if not intersects:
            for y_line, x_start, x_end in horizontal_lines:
                # Horizontal line crosses vertically through the rectangle interior (not on boundary)
                if rect_y1 < y_line < rect_y2:
                    # Check if it intersects horizontally (crosses through, not just touches)
                    if x_start < rect_x2 and x_end > rect_x1:
                        intersects = True
                        break
            
        if all_inside and not intersects:
            area = (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)
            if area > max_area:
                max_area = area
print(max_area)