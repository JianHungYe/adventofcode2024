import re
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("input.txt")

def part1():
    inlineMul = []
    mul = []
    inlineNum = []
    num = []
    sum = 0
    for line in file_data:
        inlineMul = re.findall("mul\([0-9]+,[0-9]+\)", line)
        for i in inlineMul:
            mul.append(i)
    for i in mul:
        inlineNum = re.findall("[0-9]+", i)
        for j in inlineNum:
            num.append(j)
    i = 0
    while (i < len(num) - 1):
        product = int(num[i]) * int(num[i + 1])
        i += 2
        sum = sum + product
    print(sum)


def part2():
    alllines= ""
    inlineMul = []
    mul = []
    inlineNum = []
    num = []
    sum = 0
    for line in file_data:
        alllines = alllines + line

    mul = re.findall("mul\([0-9]+,[0-9]+\)", re.sub(r"don't\(\)(.*?)do\(\)", "",alllines))
    for i in mul:
        inlineNum = re.findall("[0-9]+", i)
        for j in inlineNum:
            num.append(j)
    i = 0
    while (i < len(num) - 1):
        product = int(num[i]) * int(num[i + 1])
        i += 2
        sum = sum + product
    print(sum)


part1()
part2()
