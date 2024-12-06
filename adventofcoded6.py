import re
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("input2")

grid = []
for line in file_data:
    row = []
    for letter in line:
        row.append(letter)
    grid.append(row)
beenhere = [];
sRow = 0
sCol = 0
for i in range(len(grid[0])):
    for j in range(len(grid)):
        if (grid[i][j] == "^"):
            sRow = i
            sCol = j
            grid[i].pop(j)
            grid[i].insert(j, ".")
            beenhere.append([i,j])
            break
cRow = sRow
cCol = sCol
state = "up"
guardPresent = True
while guardPresent:
    if state == "up":
        try:
            next = grid[cRow+1][cCol]
        except:
            guardPresent = True
            break
        if next == ".":
            cRow = cRow + 1
            print(f"{state} type: {next} row: {cRow} col: {cCol}")
            if (beenhere.count([cRow, cCol]) == 0):
                beenhere.append([cRow, cCol])
        elif next == "#":
            state = "right"
    if state == "right":

        try:
            next = grid[cRow][cCol + 1]
        except:
            guardPresent = True

        if next == ".":

            cCol +=1
            print(f"{state} type: {next} row: {cRow} col: {cCol}")
            if (beenhere.count([cRow, cCol]) == 0):
                beenhere.append([cRow, cCol]);
        elif next == "#":
            state = "down"
    if state == "down":
        try:
            next = grid[cRow - 1][cCol]
        except:
            guardPresent = True

        if next == ".":
            cRow -=1
            print(f"{state} type: {next} row: {cRow} col: {cCol}")
            if (beenhere.count([cRow, cCol]) == 0):
                beenhere.append([cRow, cCol]);
        elif next == "#":
            state = "left"
    if state == "left":
        try:
            next = grid[cRow][cCol - 1]
        except:
            guardPresent = True

        if next == ".":
            cCol -= 1
            print(f"{state} type: {next} row: {cRow} col: {cCol}")
            if (beenhere.count([cRow, cCol]) == 0):
                beenhere.append([cRow, cCol])
        elif next == "#":
            state = "up"


print(len(beenhere) + 1)
