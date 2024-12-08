######################################################
### Author: Sarah Faron
### Advent of Code 2024
### Day 2: 12/01/2024
######################################################

### Part 1 ###
input = "sample.txt"
reports = []
safe = 0
unsafe = 0

# Read in the input file
with open(input) as f:
    lines = f.readlines()

    for line in lines:
        report = line.split(" ")
        report[-1] = report[-1].rstrip()
        reports.append(report)

for report in reports:

    if int(report[1]) > int(report[0]):
        reportType = "increasing"
    elif int(report[1]) < int(report[0]):
        reportType = "decreasing"

    for i in range(0, len(report)-1):
        if reportType == "increasing":
            diff = int(report[i+1]) - int(report[i])
            if diff < 4 and diff > 0 and int(report[i+1]) > int(report[i]):
                if i != len(report)-2:
                    continue
                else:
                    safe = safe + 1
            else:
                unsafe = unsafe + 1
                break
        elif reportType == "decreasing":
            diff = int(report[i]) - int(report[i+1])
            if diff < 4 and diff > 0 and int(report[i+1]) < int(report[i]):
                if i != len(report)-2:
                    continue
                else:
                    safe = safe + 1
            else:
                unsafe = unsafe + 1
                break


print("hi")
# for i in range(0, len(locationList1)):
#     min1 = min(locationList1)
#     min2 = min(locationList2)
#     distance = abs(min1-min2)

#     distances.append(distance)
#     locationList1.remove(min1)
#     locationList2.remove(min2)

# print(sum(distances))


# ### Part 2 ###

# similarityScore = []

# # Read in the input file
# with open(input) as f:
#     lines = f.readlines()

#     for line in lines:
#         locationList1.append(int(line.split(" ")[0]))
#         locationList2.append(int(line.split(" ")[3].rstrip()))

# for i in range(0, len(locationList1)):
#     val = locationList1[i]
#     count = 0

#     for i in range(0, len(locationList2)):
#         if val == locationList2[i]:
#             count = count + 1

#     similarityScore.append(count*val)

# print(sum(similarityScore))