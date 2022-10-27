'''
Gaby Furness 10/22
parallelogram function
v1 - calculate area and perimeter for parallelogram
'''

def program_start():
    t


answer_area_parallelogram = 0
answer_perimeter_parallelogram = 0


def parallelogram_area():
    while answer_area_parallelogram == 0:

        base = float(input("enter base: "))
        height = float(input("enter height: "))
        sloped_side = float(input("enter sloped side length: "))
        parallelogram_area_calc = base * height
        answer_parallelogram_area = int(input("enter the answer for the area: "))

        if answer_parallelogram_area == parallelogram_area_calc:
            print("correct answer, good job!")

            answer_parallelogram_area == "correct"
            answer_area_parallelogram == +1
            parallelogram_perimeter()


        else:
            print("incorrect answer. the correct answer is ", parallelogram_area_calc)

            answer_parallelogram_area == "incorrect"
            answer_area_parallelogram == +1
            parallelogram_perimeter()


def parallelogram_perimeter():
    while answer_perimeter_parallelogram == 0:
        base = float(input("enter base: "))
        height = float(input("enter height: "))
        sloped_side = float(input("enter sloped side length: "))
        parallelogram_perimeter_calc = base + height + base + height
        parallelogram_perimeter_int = int(parallelogram_perimeter_calc)
        answer_parallelogram_perimeter = int(input("enter the answer for the perimeter: "))

        if answer_parallelogram_perimeter == parallelogram_perimeter_int:
            print("correct answer, good job!")

            answer_parallelogram_perimeter == "correct"
            answer_perimeter_parallelogram == answer_perimeter_parallelogram + 1

            print("thank you for playing")
            end()



        else:
            print("incorrect answer. the correct answer is ", parallelogram_perimeter_int)
            answer_parallelogram_perimeter == "incorrect"
            answer_perimeter_parallelogram == answer_perimeter_parallelogram + 1
            print("thank you for playing")
            end()



ending_parallelogram = 0


def end():
    while ending_parallelogram == 0:
        ending_parallelogram == ending_parallelogram + 1


print("parallelogram area and perimeter calculator")
parallelogram_area()
