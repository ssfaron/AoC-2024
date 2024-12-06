######################################################
### Author: Sarah Faron
### Advent of Code 2024
### Day 1: 11/30/2024
######################################################

### Part 1 ###
input = "sample.txt"
count = 0

def walk(rowStart, columnStart, direction):
    if direction == "N":
        for i in blocks:
            if columnStart == blocks[i] and i < rowStart:
                newRowStart = i+1
                newColumnStart = columnStart
                newDirection = "E"
                break
        else:
            newRowStart = -1
            newColumnStart = columnStart
            newDirection = "N"
    elif direction == "E":
        for i in blocks:
            if i in blocks and blocks[i] > columnStart:
                newRowStart = rowStart
                newColumnStart = blocks[i]-1
                newDirection = "S"
                break
        else:
            newRowStart = rowStart
            newColumnStart = len(lines)
            newDirection = "E"
    elif direction == "S":
        for i in blocks:
            if columnStart == blocks[i] and i > rowStart:
                newRowStart = i-1
                newColumnStart = columnStart
                newDirection = "W"
                break
        else:
            newRowStart = len(lines)
            newColumnStart = columnStart
            newDirection = "S"
    elif direction == "W":
        for i in blocks:
            if i in blocks and blocks[i] < columnStart:
                newRowStart = rowStart
                newColumnStart = blocks[i]+1
                newDirection = "S"
                break
        else:
            newRowStart = rowStart
            newColumnStart = len(lines)
            newDirection = "W"

    return newRowStart, newColumnStart, newDirection


# Read in the input file
with open(input) as f:
    lines = f.readlines()

    blocks = {}
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if lines[i][j] == "#":
                blocks[i] = j
            elif lines[i][j] == "^":
                guard = (i,j)

# map bounds
rowBounds = (0,9)
columnBounds = (0,9)

# begin at guard's position and go straight until we hit a block
rowStart = guard[0]
columnStart = guard[1]
direction = "N"

while rowStart > rowBounds[0] and rowStart < rowBounds[1] and columnStart > columnBounds[0] and columnStart < columnBounds[1]:

    newRowStart, newColumnStart, newDirection = walk(rowStart, columnStart, direction)

    rowStart = newRowStart
    columnStart = newColumnStart
    direction = newDirection


print("hi")
