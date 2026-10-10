import math

def square(side):
    return math.ceil(side *side)

num_square = int(input("Введите длину стороны квадрата = "))
print(f"Площадь равна: {square(num_square)}")