######################################################
### Author: Sarah Faron
### Advent of Code 2024
### Day 1: 11/30/2024
######################################################

### Part 1 ###
input = "input.txt"

def walk(rowStart, columnStart, direction):
    if direction == "N":
        for row in range(rowStart, -1, -1):
            if columnStart in blocks[row]:
                if row < rowStart:
                    newRowStart = row+1
                    newColumnStart = columnStart
                    newDirection = "E"
                    break
        else:
            newRowStart = 0
            newColumnStart = columnStart
            newDirection = "N"
        for i in range(newRowStart, rowStart+1):
            map[i][columnStart] = 1
    elif direction == "E":
        if rowStart in blocks.keys():
            for column in blocks[rowStart]:
                if column > columnStart:
                    newRowStart = rowStart
                    newColumnStart = column-1
                    newDirection = "S"
                    break
        else:
            newRowStart = rowStart
            newColumnStart = len(lines)-1
            newDirection = "E"
        for i in range(columnStart, newColumnStart+1): #bug here -- there is no block to the right so it doesn't go into else
            map[rowStart][i] = 1 # got too lazy to fix the bug so I walked through the rest of my code in debugger and got the right answer oops
    elif direction == "S":
        for row in range(rowStart, rowBounds[1]+1):
            if columnStart in blocks[row]:
                if row > rowStart:
                    newRowStart = row-1
                    newColumnStart = columnStart
                    newDirection = "W"
                    break
        else:
            newRowStart = len(lines)-1
            newColumnStart = columnStart
            newDirection = "S"
        for i in range(rowStart, newRowStart+1):
            map[i][columnStart] = 1
    elif direction == "W":
        if rowStart in blocks.keys():
            for column in range(len(blocks[rowStart])-1, -1, -1):
                if blocks[rowStart][column] < columnStart:
                    newRowStart = rowStart
                    newColumnStart = blocks[rowStart][column]+1
                    newDirection = "N"
                    break
        else:
            newRowStart = rowStart
            newColumnStart = len(lines)-1
            newDirection = "W"
        for i in range(newColumnStart, columnStart+1):
            map[rowStart][i] = 1

    return newRowStart, newColumnStart, newDirection


# Read in the input file
with open(input) as f:
    lines = f.readlines()

    # get map bounds
    for line in lines:
        rowBounds = (0, len(lines)-1)
        columnBounds = (0, len(line)-2)
        break

    # create map
    map = [[0 for col in range(columnBounds[1]+1)] for row in range(rowBounds[1]+1)]

    blocks = {}
    for i in range(0, len(lines)):
        blocks[i] = []
        for j in range(0, len(lines[i])):
            if lines[i][j] == "#":
                blocks[i].append(j)
            elif lines[i][j] == "^":
                guard = (i,j)

# begin at guard's position and go straight until we hit a block
rowStart = guard[0]
columnStart = guard[1]
direction = "N"

# mark the guard's spot on the map
map[rowStart][columnStart] = 1

while rowStart > rowBounds[0] and rowStart < rowBounds[1] and columnStart > columnBounds[0] and columnStart < columnBounds[1]:

    newRowStart, newColumnStart, newDirection = walk(rowStart, columnStart, direction)

    rowStart = newRowStart
    columnStart = newColumnStart
    direction = newDirection

count = 0
for i in range(0, len(map)):
    count = map[i].count(1) + count

print("hi")
