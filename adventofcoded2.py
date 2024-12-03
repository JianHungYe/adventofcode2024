
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
    res3 = all(abs(i - j) < 4 for i, j in zip(num1, num1[1:]))
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
            return count

    for x in range(len(num1)):
        temp = num1.copy()
        temp.pop(x)
        if (checksafe(temp)):
            count = count + 1
            break
    return count


def checksafe(temp):
    res1 = all(i < j for i, j in zip(temp, temp[1:]))
    res2 = all(i > j for i, j in zip(temp, temp[1:]))
    res3 = all(abs(i - j) < 4 for i, j in zip(temp, temp[1:]))
    if (res1 or res2):
        if (res3):
            return True
    return False

file_data = get_file_data("input.txt")
count = 0;
num1 = []
num2 =[]

for line in file_data:
    split(line)
    count = getanswer(count)
    num1 = []
print(count)

count = 0
for line in file_data:
    split(line)
    count = getanswer2(count)
    num1 = []
print(count)