# Area calculator

import math

# Check if a string can be converted to a valid measurement for a shape
# (only made up of digits and maybe one period)
def valid_input(s):
    for c in s:
        if c not in "1234567890.":
            return False
    if s.count(".") > 1:
        return False
    if len(s) == 0:
        return False
    return True

# Calculate the area of a triangle based on user-defined numbers
def triangle():
    # Initialize variables for input
    base = ""
    height = ""
    # Repeatedly ask for input until valid
    while not (valid_input(base) and valid_input(height)):
        base = input("Base: ")
        height = input("Height: ")
        if valid_input(base) and valid_input(height):
            return float(height) * float(base) / 2
        else:
            print("Invalid input. Try again.")

# Calculate the area of a rectangle based on user-defined numbers
def rectangle():
    length = input("Length: ")
    width = input("Width: ")
    if valid_input(length) and valid_input(width):
        return float(length) * float(width)
    else:
        print("Invalid input. Try again.")
    
# Calculate the area of a square based on user-defined numbers
def square():
    side = input("Side length: ")
    if valid_input(side):
        return float(side) ** 2
    else:
        print("Invalid input. Try again.")

# Calculate the area of a circle based on user-defined numbers
def circle():
    radius = input("Radius: ")
    if valid_input(radius):
        return (float(radius) ** 2) * math.pi
    else:
        print("Invalid input. Try again.")
    

# Main function that presents a menu of shapes to choose
def start():
    print("Which shape would you like to find the area of?\
          \n\n1) Triangle\
            \n2) Rectangle\
            \n3) Square\
            \n4) Circle\
            \n5) Quit")
    
    area = 0
    # Initialize variable to hold response
    choice = ""

    # Repeatedly ask for choice until it's valid
    while not (choice == "1" or choice == "2" or choice == "3" or choice == "4" 
               or choice == "5"):
        choice = input("Enter a number: ")
        if choice == "1":
            area = triangle()
            print(f"The area is {area}.")
        elif choice == "2":
            area = rectangle()
            print(f"The area is {area}.")
        elif choice == "3":
            area = square()
            print(f"The area is {area}.")
        elif choice == "4":
            area = circle()
            print(f"The area is {area}.")
        elif choice == "5":
            return False
        else:
            print("Please enter the number of an option listed above.")
    return True

# MAIN LOOP

run = True
again = "Y"
print("==================\
            \nArea Calculator 📐\
            \n==================\n")

# Keep showing the menu after each calculation, if the user confirms
while run and again.upper() == "Y":
    # Start the main program
    # Will return False if they pressed 5 to quit
    run = start()
    # Don't ask to go again if they pressed 5 to quit
    if run:
        again = input("Do you want to calculate another area? (Y/N) ")