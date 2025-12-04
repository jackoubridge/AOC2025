# Part 1
jolts = 0

with open('input.txt') as file:
    for line in file:
        input = list(line)
        if input[-1] == '\n':
            input = input[:-1]
        input = [int(x) for x in input]

        first_num = -1
        first_index = 0

        for i in range(len(input)-1):
            if input[i] > first_num:
                first_num = input[i]
                first_index = i

        jolts += int(str(input[first_index]) + str(max(input[first_index+1:])))

print(jolts)

# Part 2
jolts = 0

with open('input.txt') as file:
    for line in file:
        input = list(line)
        if input[-1] == '\n':
            input = input[:-1]
        nums = [int(x) for x in input]
        
        output = []

        for x in range(12):
            remaining = 11-x

            largest = -1
            largest_index = -1
            for i in range(len(nums)-remaining):
                if nums[i] > largest:
                    largest = nums[i]
                    largest_index = i

            nums = nums[largest_index+1:]
            output.append(largest)

        out = int(''.join([str(x) for x in output]))
        jolts += out

print(jolts)