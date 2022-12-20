from triangle import triangle_square, triangle_perim
from circle import circle_square, circle_perim
from rectangle import rectangle_square, rectangle_perim


def result_triangle():
    return {"triangle": {"square": triangle_square(3, 4, 5), "perimetr": triangle_perim(3, 4, 5)}}

def result_circle():
    return {"circle": {"square": circle_square(5), "perimetr": circle_perim(5)}}
def result_rectangle():
    return {"rectangle": {"square": rectangle_square(2, 3), "perimetr": rectangle_perim(2, 3)}}



print(result_triangle())
print(result_circle())
print(result_rectangle())