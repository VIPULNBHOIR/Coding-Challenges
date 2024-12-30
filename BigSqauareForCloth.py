pts = int(input().strip())
points = [(0,)*2 for _ in range(pts)]

for i in range(pts):
    x, y = map(int, input().split())
    points[i] = (x,y)

points_set = set(points)
min_pt_req = 3
count = 1

for i in range(0, pts - 1):
    x1 , y1 = points[i][0], points[i][1]
    for j in range(i + 1, pts):
        x2 , y2 = points[j][0], points[j][1]
        count = 2

        dx, dy = x2 - x1, y2 - y1

        if dx == dy:
            if (x1, x2) in points_set:
                count += 1
            if (x2, x1) in points_set:
                count += 1

            min_pt_req = min(min_pt_req, 4 - count)

        elif x1 == x2:
            if (x1 + dy, y1) in points_set:
                count += 1
            if (x2 + dy, y2) in points_set:
                count += 1
            min_pt_req = min(min_pt_req, 4 - count)
            count = 2

            if (x1 - dy, y1) in points_set:
                count += 1
            if (x2 - dy, y2) in points_set:
                count += 1

            min_pt_req = min(min_pt_req, 4 - count)

        elif y1 == y2:
            if (x1, y1 + dx) in points_set:
                count += 1

            if (x2, y2 + dx) in points_set:
                count += 1

            min_pt_req = min(min_pt_req, 4 - count)
            count = 2
            
            if (x1, y1 - dx) in points_set:
                count += 1
            if (x2, y2 - dx) in points_set:
                count += 1

            min_pt_req = min(min_pt_req, 4 - count)

        else:
            min_pt_req = min(min_pt_req, 4 - count)

print(min_pt_req)
