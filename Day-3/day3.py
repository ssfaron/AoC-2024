######################################################
### Author: Sarah Faron
### Advent of Code 2024
### Day 3: 12/02/2024
######################################################

# ### Part 1 ###
# input = "input.txt"
# mults = []


# # Read in the input file
# with open(input) as f:
#     lines = f.readlines()

#     for line in lines:
#         for i in range(0, len(line)):
#             if line[i] == "m":
#                 if line[i+1] == "u":
#                     if line[i+2] == "l":
#                         if line[i+3] == "(":

#                             firstNum = []
#                             for j in range(1,5):
#                                 if line[i+3+j].isdigit():
#                                     firstNum.append(line[i+3+j])
#                                 else:
#                                     j = j-1
#                                     break

#                             if line[i+3+j+1] == ",":

#                                 secondNum = []
#                                 for k in range(1,5):
#                                     if line[i+3+j+1+k].isdigit():
#                                         secondNum.append(line[i+3+j+1+k])
#                                     else:
#                                         k = k-1
#                                         break

#                                 if line[i+3+j+1+k+1] == ")":

#                                     firstNumber = int(''.join(firstNum))
#                                     secondNumber = int(''.join(secondNum))
#                                     mult = firstNumber*secondNumber
#                                     mults.append(mult)


# print(sum(mults))


### Part 2 ###
input = "input.txt"
mults = []
status = "enabled"

# Read in the input file
with open(input) as f:
    lines = f.readlines()

    for line in lines:
        for i in range(0, len(line)):
            if line[i] == "m" and status == "enabled":
                if line[i+1] == "u":
                    if line[i+2] == "l":
                        if line[i+3] == "(":

                            firstNum = []
                            for j in range(1,5):
                                if line[i+3+j].isdigit():
                                    firstNum.append(line[i+3+j])
                                else:
                                    j = j-1
                                    break

                            if line[i+3+j+1] == ",":

                                secondNum = []
                                for k in range(1,5):
                                    if line[i+3+j+1+k].isdigit():
                                        secondNum.append(line[i+3+j+1+k])
                                    else:
                                        k = k-1
                                        break

                                if line[i+3+j+1+k+1] == ")":

                                    firstNumber = int(''.join(firstNum))
                                    secondNumber = int(''.join(secondNum))
                                    mult = firstNumber*secondNumber
                                    mults.append(mult)
            elif line[i] == "d":
                if line[i:i+7] == "don't()":
                    status = "disabled"
                elif line[i:i+4] == "do()":
                    status = "enabled"


print(sum(mults))



print("hi")