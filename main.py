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

radius = valid_float_input("Circle radius: ")
xOffset = valid_float_input("X coordinate of centre: ")
yOffset = valid_float_input("Y coordinate of centre: ")
offset = (xOffset - int(xOffset), yOffset - int(yOffset))

print("Circle with radius " + str(radius) + " at offset (" + str(offset[0]) + ", " + str(offset[1]) + ")")