######################################################
### Author: Sarah Faron
### Advent of Code 2024
### Day 4: 12/03/2024
######################################################

### Part 1 ###
input = "sample.txt"

def checkForM(i, j):
    grid = []
    if i == 0:
        grid.append(lines[i][j-1]) # 0 = left
        grid.append(lines[i][j+1]) # 1 = right
        grid.append(lines[i+1][j-1]) # 2 = down left
        grid.append(lines[i+1][j]) # 3 = down
        grid.append(lines[i+1][j+1]) # 4 = down right
    if i > 0 and i < len(lines)-1:
        grid.append(lines[i-1][j-1]) # 0 = up left
        grid.append(lines[i-1][j]) # 1 = up
        grid.append(lines[i-1][j+1]) # 2 = up right
        grid.append(lines[i][j-1]) # 3 = left
        grid.append(lines[i][j+1]) # 4 = right
        grid.append(lines[i+1][j-1]) # 5 = down left
        grid.append(lines[i+1][j]) # 6 = down
        grid.append(lines[i+1][j+1]) # 7 = down right
    if i == len(lines)-1:
        grid.append(lines[i-1][j-1]) # 2 = up left
        grid.append(lines[i-1][j]) # 3 = up
        if j < len(lines)-1:
            grid.append(lines[i-1][j+1]) # 4 = up right
        else:
            grid.append(0)
        grid.append(lines[i][j-1]) # 0 = left
        if j < len(lines)-1:
            grid.append(lines[i][j+1]) # 1 = right
        else:
            grid.append(0)

    for idx in range(0, len(grid)):
        if grid[idx] == "M":
            result = True
            position = idx

            return result, position

    result = False
    position = -1
    return result, position
######################################################
def checkForLetter(i, j, position, letter):
    locIf0 = [j-1, j+1, j-1, j, j+1]
    locIfNot0 = [j-1, j, j+1, j-1, j+1, j-1, j, j+1]
    locEnd = [j-1, j, j+1, j-1, j+1]

    grid = []
    if i == 0:
        grid.append(lines[i][locIf0[position]-1]) # 0 = left
        grid.append(lines[i][locIf0[position]+1]) # 1 = right
        grid.append(lines[i+1][locIf0[position]-1]) # 2 = down left
        grid.append(lines[i+1][locIf0[position]]) # 3 = down
        grid.append(lines[i+1][locIf0[position]+1]) # 4 = down right
    if i > 0 and i < len(lines)-1:
        grid.append(lines[i-1][locIfNot0[position]-1]) # 0 = up left
        grid.append(lines[i-1][locIfNot0[position]]) # 1 = up
        grid.append(lines[i-1][locIfNot0[position]+1]) # 2 = up right
        grid.append(lines[i][locIfNot0[position]-1]) # 3 = left
        grid.append(lines[i][locIfNot0[position]+1]) # 4 = right
        grid.append(lines[i+1][locIfNot0[position]-1]) # 5 = down left
        grid.append(lines[i+1][locIfNot0[position]]) # 6 = down
        grid.append(lines[i+1][locIfNot0[position]+1]) # 7 = down right
    if i == len(lines)-1:
        grid.append(lines[i-1][locEnd[position]-1]) # 2 = up left
        grid.append(lines[i-1][locEnd[position]]) # 3 = up
        grid.append(lines[i-1][locEnd[position]+1]) # 4 = up right
        grid.append(lines[i][locEnd[position]-1]) # 0 = left
        grid.append(lines[i][locEnd[position]+1]) # 1 = right

    for idx in range(0, len(grid)):
        if grid[idx] == letter:
            result = True
            position = idx

            return result, position

    result = False
    position = -1
    return result, position


######################################################

# Read in the input file
with open(input) as f:
    lines = f.readlines()

for i in range(0, len(lines)):
    lines[i].rstrip()

count = 0
for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        if lines[i][j] == "X":
            result, position = checkForM(i,j)
            if result == True:
                result2, position2 = checkForLetter(i,j,position, "A")
                if result == True:
                    result3, position3 = checkForLetter(i,j,position, "S")
                    if result3 == True:
                        count = count + 1

print(count)
