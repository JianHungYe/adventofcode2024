import re
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

file_data = get_file_data("input2")
rules = []
numbers = []
wrongnumbers = []

def part1():
    for line in file_data:
        if (re.match("[0-9]+\|[0-9]+", line)):
            rule = (line.split("|"))
            rules.append(rule)
        else:
            list = line.split(",")
            numbers.append(list)
    numbers.pop(0)

    for j in range(len(numbers)):
        number = numbers[j]
        for rule in rules:
            index1 = -1
            index2 = -1
            for i in range(len(number)):
                if int(number[i]) == int(rule[0]):
                    index1 = i
                if int(number[i]) == int(rule[1]):
                    index2 = i

            if (index1 > index2 and index2 != -1 and index1 != -1):
                # print(f"{rule} failed: num {int(number[index1])} at {index1}, num {int(number[index2])} at {index2}")
                wrongnumbers.append(numbers[j])
                numbers.pop(j)
                numbers.insert(j, [0])
                break


    count = 0
    for number in numbers:
        middleIndex = int(len(number)/2 - .5)
        count += int(number[middleIndex])
    return count


def part2():
    count = 0
    for wnumber in wrongnumbers:
        rule_found = []
        for rule in rules:
            found1 = False
            found2 = False
            for num in wnumber:
                if int(num) == int(rule[0]):
                    found1 = True
                if int(num) == int(rule[1]):
                    found2 = True
            if (found2 and found1):
                rule_found.append(rule)

        middleIndex = int(len(wnumber) / 2)
        for num in wnumber:
            index = 0
            for fRule in rule_found:
                if int(fRule[1]) == int(num):
                    index+=1
            if index == middleIndex:
                count+=int(num)
    return count





print(part1())
print(part2())