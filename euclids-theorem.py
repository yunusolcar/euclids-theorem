points_list = [(2, 3), (5, 7), (1, 9)]
distances = []

def euclideanDistance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

for i in range(len(points_list)):
    for j in range(i + 1, len(points_list)):
        distance = euclideanDistance(points_list[i], points_list[j])
        distances.append(distance)

min_distance = min(distances)
print("Minimum mesafe:", min_distance)