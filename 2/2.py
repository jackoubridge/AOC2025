with open('input.txt') as file:
    for line in file:
        inputs = line.split(",")

# Part 1
count = 0

for input in inputs:
    dash = input.find("-")
    left = int(input[:dash])
    right = int(input[dash+1:])

    for num in range(left, right+1):
        id = str(num)
        if (len(id) % 2 == 0):
            half = int(len(id) / 2)
            if (id[:half] == id[half:]):
                count += num
print(count)

# Part 2
count = 0

for input in inputs:
    dash = input.find("-")
    left = int(input[:dash])
    right = int(input[dash+1:])

    for num in range(left, right+1):
        id = str(num)
        for k in range(2, len(id)+1):
            if (len(id) % k == 0):
                part_len = len(id) // k
                chunks = [id[i * part_len:(i + 1) * part_len] for i in range(k)]
                if(chunks.count(chunks[0]) == len(chunks)):
                    count += num
                    break

print(count)