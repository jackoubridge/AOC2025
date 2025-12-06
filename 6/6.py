import math

with open('input.txt') as file:
    input = [line for line in file]

indices = []

for i in range(len(input[4])):
    if input[4][i] == "*":
        indices.append(("*", i))
    elif input[4][i] == "+":
        indices.append(("+", i))
        
def processNums(operation, nums):
    if operation == "*":
        return math.prod(nums)
    else:
        return sum(nums)

# Part 1
output = 0
for i in range(len(indices)):
    nums = []
    if i == len(indices) - 1:
        end = len(input[4])
    else:
        end = indices[i+1][1]
    nums = [int(input[0][indices[i][1]:end]), int(input[1][indices[i][1]:end]), 
            int(input[2][indices[i][1]:end]), int(input[3][indices[i][1]:end])]

    output += processNums(indices[i][0], nums)

print(output)

# Part 2
output = 0

for i in range(len(indices)):
    nums = []
    if i == len(indices) - 1:
        end = len(input[4]) + 1
    else:
        end = indices[i+1][1]
    
    for j in range(indices[i][1], end-1):
        nums.append(int(input[0][j] + input[1][j] + input[2][j] + input[3][j]))
    
    output += processNums(indices[i][0], nums)

print(output)
    