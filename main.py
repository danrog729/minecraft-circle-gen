import math

def valid_float_input(message):
    number = 0.0
    valid = False
    while not valid:
        string = input(message)
        try:
            number = float(string)
            valid = True
        except:
            print("Not a valid number.")
    return number

def generate_2d_array(rows, columns):
    array = [[0 for column in range(0,columns,1)] for row in range(0,rows,1)]
    return array

def print_array_formatted(array):
    for row in range(0,len(array),1):
        for column in range(0, len(array[row]), 1):
            if array[row][column] == 16:
                print("██",end="")
            elif (array[row][column] == 0 or array[row][column] == 15):
                print("[]", end = "")
            else:
                print("██", end = "")
            topLeft = array[row][column] >= 8
            topRight = array[row][column] % 8 >= 4
            bottomLeft = array[row][column] % 4 >= 2
            bottomRight = array[row][column] % 2 >= 1

            # if (topLeft and topRight and bottomLeft and bottomRight):
            #     print("[]",end="")
            # else:
            #     if (topLeft and bottomLeft):
            #         print("█",end="")
            #     else:
            #         if topLeft:
            #             print("▀",end="")
            #         elif bottomLeft:
            #             print("▄",end="")
            #         else:
            #             print("[",end="")

            #     if (topRight and bottomRight):
            #         print("█",end="")
            #     else:
            #         if topRight:
            #             print("▀",end="")
            #         elif bottomRight:
            #             print("▄",end="")
            #         else:
            #             print("]",end="")
        print()

def print_array(array):
    for row in range(0,len(array),1):
        for column in range(0, len(array[row]), 1):
            if array[row][column] < 10:
                print("0",end="")
            print(array[row][column],end="")
        print()

while True:
    radius = valid_float_input("Circle radius: ")
    xOffset = valid_float_input("X coordinate of centre: ")
    yOffset = valid_float_input("Y coordinate of centre: ")
    offset = (xOffset - int(xOffset), yOffset - int(yOffset))

    print("Circle with radius " + str(radius) + " with block offset (" + str(offset[0]) + ", " + str(offset[1]) + ")")

    grid = generate_2d_array(math.ceil(radius * 2 + 2)+1, math.ceil(radius * 2 + 2)+1)

    for row in range(0,len(grid),1):
        for column in range(0,len(grid[row]),1):
            #check top left corner
            if (row-int(radius+1)-yOffset)**2 + (column-int(radius+1)-xOffset)**2 <= radius**2:
                grid[row][column] += 8
            #check top right corner
            if (row-int(radius+1)-yOffset)**2 + (column+1-int(radius+1)-xOffset)**2 <= radius**2:
                grid[row][column] += 4
            #check bottom left corner
            if (row+1-int(radius+1)-yOffset)**2 + (column-int(radius+1)-xOffset)**2 <= radius**2:
                grid[row][column] += 2
            #check bottom right corner
            if (row+1-int(radius+1)-yOffset)**2 + (column+1-int(radius+1)-xOffset)**2 <= radius**2:
                grid[row][column] += 1

    centreDimension = int(radius+1)
    grid[centreDimension][centreDimension] = 16

    print_array_formatted(grid)