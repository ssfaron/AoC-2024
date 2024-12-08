######################################################
### Author: Sarah Faron
### Advent of Code 2024
### Day 1: 11/30/2024
######################################################

### Part 1 ###
input = "input.txt"
locationList1 = []
locationList2 = []
distances = []

# Read in the input file
with open(input) as f:
    lines = f.readlines()

    for line in lines:
        locationList1.append(int(line.split(" ")[0]))
        locationList2.append(int(line.split(" ")[3].rstrip()))

# Find the min value in each column
# and find the absolute value of the difference between them
for i in range(0, len(locationList1)):
    min1 = min(locationList1)
    min2 = min(locationList2)
    distance = abs(min1-min2)

    # Remove the min values from each colum
    distances.append(distance)
    locationList1.remove(min1)
    locationList2.remove(min2)

# Sum the distances
print(sum(distances))


### Part 2 ###

similarityScore = []

# Read in the input file
with open(input) as f:
    lines = f.readlines()

    for line in lines:
        locationList1.append(int(line.split(" ")[0]))
        locationList2.append(int(line.split(" ")[3].rstrip()))

# For each value in the first column,
# find the quantity of that value in the second column
for i in range(0, len(locationList1)):
    val = locationList1[i]
    count = 0

    for i in range(0, len(locationList2)):
        if val == locationList2[i]:
            count = count + 1

    # Calculate the similarity score
    similarityScore.append(count*val)

# Sum the similarity scores
print(sum(similarityScore))