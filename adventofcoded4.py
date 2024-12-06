import re
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

file_data = get_file_data("input.txt")
count = 0
# build a 2D List based on the file_data
grid = []
for line in file_data:
    row = []
    for letter in line:
        row.append(letter)
    grid.append(row)

def part1(count):
    for row in grid:
        rowstring = ""
        for x in row:
            rowstring = rowstring + x
        xmasrow = re.findall("(XMAS)", rowstring) + re.findall("(SAMX)", rowstring)

        count = count + len(xmasrow)
    for y in range(len(grid[0])):
        columnstring = ""
        for x in range(len(grid)):
            columnstring=columnstring+grid[x][y]

        xmascolumn = re.findall("(XMAS)", columnstring) + re.findall("(SAMX)", columnstring)
        count = count + len(xmascolumn)
    xmasdiagonal = [[] for _ in range(len(grid[0]) + len(grid) -1)]
    xmasdiagonal2 = [[] for _ in range(len(grid[0]) + len(grid) - 1)]
    min = -len(grid)+1
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            xmasdiagonal[i+j].append(grid[j][i])
            xmasdiagonal2[i - j - min].append(grid[j][i])
    for diag in xmasdiagonal:
        diagstring = ""
        for letter in diag:
            diagstring += letter
        diagxmas = re.findall("(XMAS)", diagstring) + re.findall("(SAMX)", diagstring)
        count += len(diagxmas)
    for diag in xmasdiagonal2:
        diagstring2 = ""
        for letter in diag:
            diagstring2 += letter
        diagxmas2 = re.findall("(XMAS)", diagstring2) + re.findall("(SAMX)", diagstring2)
        count += len(diagxmas2)


    return count

def part2():
    count2 = 0
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if (grid[i][j] == "A"):
                try:
                    if (grid[i - 1][j - 1] == "M" and grid[i - 1][j + 1] == "M"):
                        if (grid[i + 1][j - 1] == "S" and grid[i + 1][j + 1] == "S"):
                            count2 += 1
                    elif (grid[i - 1][j - 1] == "S" and grid[i - 1][j + 1] == "S"):
                        if (grid[i + 1][j - 1] == "M" and grid[i + 1][j + 1] == "M"):
                            count2 += 1
                    elif (grid[i - 1][j - 1] == "M" and grid[i - 1][j + 1] == "S"):
                        if (grid[i + 1][j - 1] == "M" and grid[i + 1][j + 1] == "S"):
                            count2 += 1
                    elif (grid[i - 1][j - 1] == "S" and grid[i - 1][j + 1] == "M"):
                        if (grid[i + 1][j - 1] == "S" and grid[i + 1][j + 1] == "M"):
                            count2 += 1
                except:
                    donothing = 1
    return count2



count = part1(count)
print(count)
print(part2())