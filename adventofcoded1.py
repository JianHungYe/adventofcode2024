def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def split(line):
    line_split = line.split(" ")
    for line in line_split:
        num1.append(int(line))


def getanswerp1():
    distance = 0
    for line in file_data:
        min1 = min(num1)
        min2 = min(num2)
        distance = distance +abs(min1 - min2)
        num1.remove(min1)
        num2.remove(min2)
    print(distance)

def getanswerp2():
    total = 0

    for num in num1:
        match = 0
        for nu in num2:
            if num == nu:
                match += 1
        total = total + num * match
    print(total)


file_data = get_file_data("input.txt")
count = 0
num1 = []
num2=[]

for line in file_data:
    split(line)

getanswerp1()
getanswerp2()