import math


figure = input()

if figure == "square":
    a = float(input())
    sq_area = a*a
    print(f"{sq_area:.3f}")
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    rec_area = a*b
    print(f"{rec_area:.3f}")
elif figure == "circle":
    a = float(input())
    circle_area = a*a*math.pi
    print(f"{circle_area:.3f}")
elif figure == "triangle":
    a = float(input())
    b = float(input())
    triangle_area = 0.5*a*b
    print(f"{triangle_area:.3f}")