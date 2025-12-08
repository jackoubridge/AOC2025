import math

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return False
    parent[root_y] = root_x
    return True

with open('input.txt') as file:
    junction_boxes = [tuple(map(int, line.strip().split(','))) for line in file]

n = len(junction_boxes)
parent = list(range(n))

pairs = []
for i in range(n):
    for j in range(i + 1, n):
        x1, y1, z1 = junction_boxes[i]
        x2, y2, z2 = junction_boxes[j]
        distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
        pairs.append((distance, i, j))

pairs.sort(key=lambda x: x[0])

for _, i, j in pairs[:1000]:
    union(i, j)

circuit_sizes = {}
for i in range(n):
    root = find(i)
    circuit_sizes[root] = circuit_sizes.get(root, 0) + 1

largest_sizes = sorted(circuit_sizes.values(), reverse=True)[:3]

print(largest_sizes[0] * largest_sizes[1] * largest_sizes[2])

for _, i, j in pairs:
    if union(i, j):
        if len(set(find(x) for x in range(n))) == 1:
            last = (i, j)
            break

print(junction_boxes[i][0] * junction_boxes[j][0])