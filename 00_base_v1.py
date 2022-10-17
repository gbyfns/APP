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
def square():
    print("square function")

# rectangle function
def rectangle():
    print("rectangle function")

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

answer_list = []
yes_no_list = [["yes", "y"],["no","n"]]
operands = ["+","-","*", "/", "all"]

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
    operand = input("""please choose an operand (circle, square, rectangle, triangle or parallelogram): """).lower()

    # check operand for legitimacy
    # string check - send the list of shape_list

    # ask user if they wish to use negatives?
    # yes/no list and answer sent to string checker

    # ask user for low and high numbers.
    # int checker to check it's an integer, loop until suitable integer

    # ask user for number of questions to be asked
    # int checker to check on the integer
    num_questions = 1

    # loop until number of questions is asked
    for questions in (0, num_questions):
        print("placeholder")
        if operand == "circle":
            print("go to circle")
            circle()
        elif operand == "square":
            print("got to square")
            square()
        elif operand == "rectangle":
            print("go to rectangle")
            rectangle()
        elif operand == "triangle":
            print("go to triangle")
            triangle()
        elif operand == "parallelogram":
            print("go to parallelogram")
            parallelogram()

        # print("go to random generator, send min_num and max_num (1 and 5)")
        # print("then randomly go to each of the operand functions")
