'''
Gaby Furness 9/22
square rectangle component
v1 - calculate area and perimeter for square and rectangle function
'''

def program_start():
    t


answer_area_rectangle = 0
answer_perimeter_rectangle = 0


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
            rectangle_perimeter()


        else:
            print("incorrect. the correct answer is ", rectangle_area_calc)
            answer_rectangle_area == "incorrect."
            answer_area_rectangle == +1
            rectangle_perimeter()


def rectangle_perimeter():
    while answer_perimeter_rectangle == 0:
        length = float(input("input the length of the rectangle: "))
        height = float(input("input the height of the rectangle: "))
        rectangle_perimeter_calc = length * 2 + height * 2
        rectangle_perimeter_int = int(rectangle_perimeter_calc)
        # (f'__Perimeter__\n P = (L×2)+(H×2)\n A = {length}×2+{height}×2 \n A = {length * 2 + height * 2}')
        answer_rectangle_perimeter = int(input("input the answer for the perimeter: "))

        if answer_rectangle_perimeter == rectangle_perimeter_int:
            print("correct, well done!")
            answer_rectangle_perimeter == "correct"
            answer_perimeter_rectangle == answer_perimeter_rectangle + 1
            print("thanks for playing")
            quit()



        else:
            print("incorrect. The correct answer is ", rectangle_perimeter_int)
            answer_rectangle_perimeter == "incorrect"
            answer_perimeter_rectangle == answer_perimeter_rectangle + 1
            print("thanks for playing")
            quit()




print("welcome to my rectangle area and perimeter calculator")
rectangle_area()
