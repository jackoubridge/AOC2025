# Part 1
start = False
fresh = []
count = 0

with open('input.txt') as file:
    for line in file:

        if line == "\n":
            start = True
            continue
            
        if start == False:
            if line[-1] == "\n":
                line = line[:-1]
            dash = line.index("-")
            first = int(line[:dash])
            second = int(line[dash+1:])
            fresh.append((first, second))
        else:
            spoiled = True
            for (f, l) in fresh:
                if (int(line) <= l and int(line) >= f):
                    spoiled = False
                    break
            
            if spoiled == False:
                count += 1
                    
print(count)

# Part 2
start = False
fresh = []
allfresh = set()
count = 0

with open('input.txt') as file:
    for line in file:

        if line == "\n":
            start = True
            continue
            
        if start == False:
            if line[-1] == "\n":
                line = line[:-1]
            dash = line.index("-")
            first = int(line[:dash])
            second = int(line[dash+1:])
            fresh.append((first, second))

fresh = sorted(fresh, key=lambda x: x[0])

merged = []
for start, end in fresh:
    if not merged or start > merged[-1][1] + 1:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

        
for x in merged:
    count += x[1] - x[0] + 1

print(count)
