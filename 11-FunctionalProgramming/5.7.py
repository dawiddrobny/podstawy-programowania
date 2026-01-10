scores = [(17, 15, 16, 17, 15),
          (16, 18, 19, 17, 19),
          (19, 15, 15, 19, 18),
          (18, 17, 19, 15, 16)]

def calculate_score(points):
    return sum(points) - min(points) - max(points)

total_points = list(map(calculate_score, scores))
print(total_points)
