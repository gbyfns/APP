'''
Gaby Furness 9/22
program to calculate cost of serving sizes for recipes
base component
v1 - set up the skeleton of the program, test the functions are called as required
'''

# ---------- functions go below this line ----------

# function to check for integers
def int_checker():
    print("placeholder")

# function to check string is within list
def string_checker(list_of_allowable):
    print("placeholder")

# square function
def square_area():
    while answer_area_square == 0:

        length = float(input("input the length of the square: "))
        height = float(input("input the height of the square: "))
        square_area_calc = length * height
        answer_square_area = int(input("input the answer for the area: "))

        if answer_square_area == square_area_calc:
            print("correct, well done!")

            answer_square_area == "correct!"
            answer_area_square == +1
            shape_answer_list.append(square_area_calc)
            square_perimeter()


        else:
            print("incorrect. the correct answer is ", square_area_calc)

            answer_square_area == "incorrect."
            answer_area_square == +1
            shape_answer_list.append(square_area_calc)
            square_perimeter()


def square_perimeter():
    while answer_perimeter_square == 0:

        length = float(input("input the length of the square: "))
        height = float(input("input the height of the square: "))
        square_perimeter_calc = length * 2 + height * 2
        square_perimeter_int = int(square_perimeter_calc)
        answer_square_perimeter = int(input("input the answer for the perimeter: "))

        if answer_square_perimeter == square_perimeter_int:
            print("correct, well done!")

            answer_square_perimeter == "correct"
            answer_perimeter_square == answer_perimeter_square + 1


            print("thanks for playing")
            shape_answer_list.append(square_perimeter_int)
            quit()



        else:
            print("incorrect. The correct answer is ", square_perimeter_int)

            answer_square_perimeter == "incorrect"
            answer_perimeter_square == answer_perimeter_square + 1
            shape_answer_list.append(square_perimeter_int)

            print("thanks for playing")
            quit()


# rectangle function
def rectangle_area():
    while answer_area_rectangle == 0:

        length = float(input("input the length of the rectangle: "))
        height = float(input("input the height of the rectangle: "))
        rectangle_area_calc = length * height
        answer_rectangle_area = int(input("input the answer for the area: "))

        if answer_rectangle_area == rectangle_area_calc:
            print("correct, well done!")

            answer_rectangle_area == "correct!"
            answer_area_rectangle == +1
            shape_answer_list.append(rectangle_area_calc)
            rectangle_perimeter()


        else:
            print("incorrect. the correct answer is ", rectangle_area_calc)

            answer_rectangle_area == "incorrect."
            answer_area_rectangle == +1
            shape_answer_list.append(rectangle_area_calc)
            rectangle_perimeter()


def rectangle_perimeter():
    while answer_perimeter_rectangle == 0:

        length = float(input("input the length of the rectangle: "))
        height = float(input("input the height of the rectangle: "))
        rectangle_perimeter_calc = length * 2 + height * 2
        rectangle_perimeter_int = int(rectangle_perimeter_calc)
        answer_rectangle_perimeter = int(input("input the answer for the perimeter: "))

        if answer_rectangle_perimeter == rectangle_perimeter_int:
            print("correct, well done!")

            answer_rectangle_perimeter == "correct"
            answer_perimeter_rectangle == answer_perimeter_rectangle + 1

            print("thanks for playing")
            shape_answer_list.append(rectangle_perimeter_int)
            quit()



        else:
            print("incorrect. The correct answer is ", rectangle_perimeter_int)

            answer_rectangle_perimeter == "incorrect"
            answer_perimeter_rectangle == answer_perimeter_rectangle + 1

            print("thanks for playing")
            shape_answer_list.append(rectangle_perimeter_int)
            quit()

# paralellogram function
def parallelogram():
    print("parallelogram function")

# circle function
def circle():
    print("circle function")

# triangle function
def triangle():
    print("triangle function")

#  ----------- lists and constants go here -----------

shape_list = [
    ["circle", "c", "circ", "cicrle"],
    ["square", "s", "squa", "sqaure", "sq"],
    ["rectangle", "r", "rec", "rectnagle", "rect"],
    ["triangle", "trinagle", "tri"],
    ["parallelogram", "p", "para", "par"],
    ["trapezium", "tra", "trapezuim"],
]
shape_answer_list = []
answer_area_rectangle = 0
answer_perimeter_rectangle = 0
answer_area_square = 0
answer_perimeter_square = 0

#  -------------- main routine goes here --------------

if __name__ == "__main__":

    #set local variables within the main routine
    min_num = 0
    max_num = 5

    # ** introduction to game **
    print("--- AREA AND PERIMETER GAME ---")
    print("***")
    print("--- welcome to my area and perimeter game ---")
    print("")
for shape_choice in shape_list:
    shape = input("""** Please choose a shape (circle, square, rectangle, 
**  triangle, parallelogram, or trapezium): """)
    if shape in shape_list:
        continue
    else:
        break
    # check operand for legitimacy
    # string check - send the list of shape_list

    # ask user if they wish to use negatives?
    # yes/no list and answer sent to string checker

    # ask user for low and high numbers.
    # int checker to check it's an integer, loop until suitable integer

    # ask user for number of questions to be asked
    # int checker to check on the integer

        # print("go to random generator, send min_num and max_num (1 and 5)")
        # print("then randomly go to each of the operand functions")


# loop until number of questions is asked
for shape in shape_list:
    print("************************************************************************")
    if shape == "square":
        print("************************************************************************")
        square_area()
    elif shape == "rectangle":
        print("************************************************************************")
        rectangle_area()

