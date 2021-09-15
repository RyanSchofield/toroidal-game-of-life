import os

clear = lambda: os.system('clear')


def init_empty_cells(width, height):
    """
    Create an empty list, append an empty list for every row (height) and append a
    0 to every sublist for each column (width). For any element cells[i][j], 
    i and j represent x and y coordinates respectively on the grid.

    type width: int
    type height: int
    rtype: int[][]

    """
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


def copy(cells):
    """
    Create an empty list. Append empty lists for every row (height) 
    of parameter cells. add cells[i][j] to l[i][j] by iterating through
    all i and j.

    type cells: int[][]
    rtype: int[][]
    """
    l = []
    for i in range(len(cells)):
        l.append([])
        for j in range(len(cells[i])):
            l[i].append(cells[i][j])
    return(l)



def is_valid(row, column, cells):
    """
    Check if a given 2D index is valid, comparing the given
    index to the width and height of parameter cells.

    type row: int
    type column: int
    type cells: int[][]
    rtype: bool
    """
    if row < 0 or column < 0:
        return(False)
    else:
        if row in range(len(cells)) and column in range(len(cells[row])):
            return(True)
        else:
            return(False)


def toggle_cell(row, column, cells):
    """
    Check if the element at given 2D index is 0 or 1, and flip accordingly.
    Return -1 if given index is invalid.

    type row: int
    type column: int
    type cells: int[][]
    """
    isValid = is_valid(row, column, cells)
    if isValid:
        if cells[row][column] == 0:
            cells[row][column] = 1
        elif cells[row][column] == 1:
            cells[row][column] = 0
        return(True)
    else:
        return(False)


 
def count_neighbors(cells, row, col):
    """
    Check every combination of i-1, i, and i+1 with j-1, j, and j+1 (exclude
    combination [i,j]), using modulus to simulate torus, and count for "1"s.
    Return -1 for invalid row or col.

    type cells: int[][]
    type row: int
    type column: int
    """
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





def update(cells):
    """
    Create an empty two dimensional list, append the counts of each element cells[i][j].
    Apply the rules of the game, checking each element of cells against
    corresponding element in the 2D list of counts. Return updated copy.

    type cells: int[][]
    rtype: int[][]
    """
    x = []
    c = copy(cells) # this is the return copy
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
    # Print the cells to the console
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
    """
    Parse the user input and return a list of coordinate pairs.

    type input_str: str
    rtype: int[][]
    """
    pairs = input_str.split(' ')
    for i in range(len(pairs)):
        pairs[i] = list(map(int, pairs[i].split(',')))
    return pairs


if __name__ == "__main__":
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