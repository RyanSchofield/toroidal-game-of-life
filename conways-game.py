import os


clear = lambda: os.system('clear')


#create an empty list, append an empty list for every row (height) and append a
# 0 for every column (width) to every empty sublist. Throughout this project,
# for any element cells[i][j], i and j represent x and y coordinates
# respectively on the grid.
def init_empty_cells(width, height):
    cells = []
    if width <= 0 or height <= 0:
        return(cells)
    else:
        for i in range(height):
            cells.append([])
        for i in cells:
            for j in range(width):
                i.append(0)
        return(cells)

#create an empty list. Append empty lists for every row (height) 
# of parameter cells. add cells[i][j] to l[i][j] by iterating through
# all i and j. Use two for-loops to do this. This method of iterating
# through cells will occur frequently throughout this project.
def copy(cells):
    l = []
    for i in range(len(cells)):
        l.append([])
        for j in range(len(cells[i])):
            l[i].append(cells[i][j])
    return(l)

#check if a given 2D index is valid by using if statements, comparing the given
# index to the width and height of parameter cells. If index is negative,
# return False.
def is_valid(row, column, cells):
    if row < 0 or column < 0:
        return(False)
    else:
        if row in range(len(cells)) and column in range(len(cells[row])):
            return(True)
        else:
            return(False)

#Use if statements to check if the element at given 2D index is 0 or 1,
# and flip accordingly. Use the is_valid function to return -1 if given
# index is invalid.
def toggle_cell(row, column, cells):
    isValid = is_valid(row, column, cells)
    if isValid:
        if cells[row][column] == 0:
            cells[row][column] = 1
        elif cells[row][column] == 1:
            cells[row][column] = 0
        return(True)
    else:
        return(False)


#check every combination of i-1, i, and i+1 with j-1, j, and j+1 (exclude
# combination [i,j]), counting for "1"s using an initially empty counting
# variable. Use if statements to do this. if is_valid returns False, return -1.
# use modulus of height and width to check cells that are next to each other on
# toroidal surface, even if they do not appear to be on 2D grid.
def count_neighbors(cells, row, col):
    isValid = is_valid(row, col, cells)
    count = 0
    if not isValid:
        return(-1)
    else:
        if cells[(row - 1) % len(cells)][(col - 1) % len(cells[0])] == 1:
            count += 1
        if cells[row][(col - 1) % len(cells[0])] == 1:
            count += 1
        if cells[(row + 1) % len(cells)][(col - 1) % len(cells[0])] == 1:
            count += 1
        if cells[(row - 1) % len(cells)][col] == 1:
            count += 1
        if cells[(row + 1) % len(cells)][col] == 1:
            count += 1
        if cells[(row - 1) % len(cells)][(col + 1) % len(cells[0])] == 1:
            count += 1
        if cells[row][(col + 1) % len(cells[0])] == 1:
            count += 1
        if cells[(row + 1) % len(cells)][(col + 1) % len(cells[0])] == 1:
            count += 1
        return(count)




#create an empty two dimensional list of appropriate size using
# method above. append the counts of each element cells[i][j]
# using the count function, with two for-loops similar to above.
# apply the rules of the game using if statements, checking each
# element of a copy of cells against corresponding element in the
# 2D list of counts. change elements individually according to rules,
# and return the updated copy.
def update(cells):
    x = []
    c = copy(cells) # remember to make a copy
    for i in range(len(cells)):
        x.append([])
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            x[i].append(count_neighbors(cells, i, j))
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            if x[i][j] == 0 or x[i][j] == 1:
                if c[i][j] == 1:
                    c[i][j] = 0
            elif x[i][j] > 3 and cells[i][j] == 1:
                c[i][j] = 0
            elif x[i][j] == 3 and cells[i][j] == 0:
                c[i][j] = 1
    return(c)

def print_cells(cells):
    num_rows = len(cells)
    num_columns = len(cells[0])
    print(" ", end="")
    for i in range(num_columns):
        print("_", end="")
    print("")
    for i in range(num_rows):
        print("|", end="")
        for j in range(num_columns):
            
            if cells[i][j]:
                print("@", end="")
            else:
                print(" ", end="")
        print("|")
        
    print(" ", end="")
    for i in range(num_columns):
        print("-", end="")
    print("")




def get_coordinates(input_str):
    pairs = input_str.split(' ')
    for i in range(len(pairs)):
        pairs[i] = list(map(int, pairs[i].split(',')))
    return pairs

#print_cells(init_empty_cells(5,5))
#print(get_coordinates("52,17 13,12"))
size = int(input("how big is the torus?\n"))
new_cells = init_empty_cells(size, size)
while True:
    clear()
    print_cells(new_cells)
    user_input = input("Specify coordinates or press enter to update:\n")
    if user_input == "":
        new_cells = update(new_cells)
    elif user_input == "quit":
        break
    else:
        for pair in get_coordinates(user_input):
            toggle_cell(pair[0] - 1, pair[1] - 1, new_cells)