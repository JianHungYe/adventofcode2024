
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def split(line):
    linesplit = line.split(" ")
    for i in linesplit:
        num1.append(int(i))
def getanswer(count):
    res1 = all(i < j for i, j in zip(num1, num1[1:]))
    res2 = all(i > j for i, j in zip(num1, num1[1:]))
    res3 = all(abs(i -j) < 4 for i, j in zip(num1, num1[1:]))
    if (res1 or res2):
        if (res3):
            count = count + 1
    return count

def getanswer2(count):
    res1 = all(i < j for i, j in zip(num1, num1[1:]))
    res2 = all(i > j for i, j in zip(num1, num1[1:]))
    res3 = all(abs(i - j) < 4 for i, j in zip(num1, num1[1:]))
    if (res1 or res2):
        if (res3):
            count = count + 1
            return count;
    if (not res1 or not res2):
        for i in num1

file_data = get_file_data("input.txt")
count = 0;
num1 = []

for line in file_data:
    split(line)
    count = getanswer(count)
    num1 = []
print(count)

for line in file_date:
    split(line)
    prev count