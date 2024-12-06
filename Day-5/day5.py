######################################################
### Author: Sarah Faron
### Advent of Code 2024
### Day 5: 12/04/2024
######################################################

import math

### Part 1 ###
input = "input.txt"

# Read in the input file
with open(input) as f:
    lines = f.readlines()

    rules = {}
    updates = []

    for i in range(0, len(lines)):
        if "|" in lines[i]:
            rules[i] = lines[i].rstrip()
        elif "," in lines[i]:
            updates.append(lines[i].rstrip())

validUpdate = {}
for i in range(0, len(updates)):
    updates[i] = updates[i].split(",")

    for page in updates[i]:
        for j in range(0, len(rules)):

            # check that rules are satisfied for each set of updates
            if page in rules[j]:
                firstPage = rules[j].split("|")[0]
                secondPage = rules[j].split("|")[1]

                if firstPage in updates[i] and secondPage in updates[i]:

                    firstIndx = updates[i].index(firstPage)
                    secondIndx = updates[i].index(secondPage)

                    # if the update is valid, mark it
                    if firstIndx < secondIndx:
                        validUpdate[i] = True
                    # if the update is invalid, mark it and discontinue investigating this update
                    else:
                        validUpdate[i] = False
                        break

        if validUpdate[i] == False:
            break

# Find the middle page in each update that was validated
middlePages = []
for i in range(0, len(validUpdate)):
    if validUpdate[i] == True:
       if len(updates[i])%2 == 1:
            middlePage = updates[i][math.floor(len(updates[i])/2)]
            middlePages.append(int(middlePage))

# Sum the values of the middle page numbers
print(sum(middlePages))


### Part 2 ###
incorrects = []
validUpdate2 = {}

# Create a list of only invalid updates
for i in range(0, len(validUpdate)):
    if validUpdate[i] == False:
        incorrects.append(updates[i])

for i in range(0, len(incorrects)):

    for page in incorrects[i]:
        for j in range(0, len(rules)):

            # check that rules are satisfied
            if page in rules[j]:
                firstPage = rules[j].split("|")[0]
                secondPage = rules[j].split("|")[1]

                if firstPage in incorrects[i] and secondPage in incorrects[i]:

                    firstIndx = incorrects[i].index(firstPage)
                    secondIndx = incorrects[i].index(secondPage)

                    # if rule is satisfied, no action
                    if firstIndx < secondIndx:
                        validUpdate2[i] = True
                    # if rule is not satisfied, move the updated page so that the rule is satisfied
                    else:
                        validUpdate2[i] = False

                        incorrects[i].pop(firstIndx)
                        incorrects[i].insert(secondIndx, firstPage)

                        # fixing this rule does not guarantee I'm not violating a rule already "validated"
                        # need to recheck the rules after changing the order of the list
                        # could do this in a function

# Find the middle page of all newly validated updates
middlePages2 = []
for i in range(0, len(validUpdate2)):
    if validUpdate2[i] == True:
       if len(incorrects[i])%2 == 1:
            middlePage = incorrects[i][math.floor(len(incorrects[i])/2)]
            middlePages2.append(int(middlePage))

# Sum the values of these middle pages
print(sum(middlePages2))
#4792 too low

print("hi")
