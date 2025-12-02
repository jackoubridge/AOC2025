# Part 1
inputs = []
current = 50
count = 0

with open('input.txt') as file:
    for input in file:

        if current == 0:
            count += 1

        if input[0] == "L":
            num = int(input[1:]) * -1
        else:
            num = int(input[1:])

        current = (current + num) % 100

print(count)

#Part 2
inputs = []
current = 50
count = 0

with open('input.txt') as file:
    for input in file:
        if input[0] == "L":
            increment = -1
        else:
            increment = 1

        for _ in range(int(input[1:])):
            current += increment
            if (current) == 0:
                count += 1
            elif (current < 0):
                current = 99
            elif (current > 99):
                current = 0
                count += 1

print(count)