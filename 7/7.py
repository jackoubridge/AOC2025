class Puzzle:
    def __init__(self, input):
        self.input = input
        self.splitters = set()

    def isSplitterDown(self, row, col):
        found = -1
        for i in range(row + 1, len(self.input)):
            if self.input[i][col] == "^":
                self.splitters.add((i, col))
                found = i
                break
        return found

timeline_cache = {}

def explore(row_, col_):
    if col_ < 0 or col_ >= len(input[0]):
        return 0

    if (row_, col_) in timeline_cache:
        return timeline_cache[(row_, col_)]

    out = puzzle.isSplitterDown(row_, col_)

    if out > 0:
        total = explore(out, col_ - 1) + explore(out, col_ + 1)
    else:
        total = 1

    timeline_cache[(row_, col_)] = total
    return total

with open('input.txt') as file:
    input = [line.strip() for line in file]

puzzle = Puzzle(input)

start_col = input[0].index("S")
total_timelines = explore(0, start_col)

print(len(puzzle.splitters))
print(total_timelines)