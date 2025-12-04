import numpy as np

grid = []
count = 0
neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

with open('input.txt') as file:
    for line in file:
        if(line[-1] == '\n'):
            line = line[:-1]
        grid.append(list(line))

# Part 1
for i in range(len(grid)):
    for j in range(len(grid[i])):
        tempCount = 0
        
        if grid[i][j] != "@":
            continue
        
        for ver, hor in neighbours:
            ni, nj = i + ver, j + hor
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[i]):
                if grid[ni][nj] == "@":
                    tempCount += 1
        if tempCount < 4:
            count += 1

print(count)

# Part 2
count = 0

removed = []

while(True):

    for (x, y) in removed:
        grid[x][y] = "."

    removed = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            tempCount = 0
            
            if grid[i][j] != "@":
                continue
            
            for ver, hor in neighbours:
                ni, nj = i + ver, j + hor
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[i]):
                    if grid[ni][nj] == "@":
                        tempCount += 1

            if tempCount < 4:
                removed.append((i, j))
                count += 1

    if len(removed) == 0:
        break

print(count)