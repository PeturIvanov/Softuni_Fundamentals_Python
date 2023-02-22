from math import sqrt
from math import floor


def find_closest_point(a1, b1, a2, b2):
    x0 = 0
    y0 = 0
    first_point_to_center = sqrt(((a1 - x0) ** 2) + ((b1 - y0) ** 2))
    second_point_to_center = sqrt(((a2 - x0) ** 2) + ((b2 - y0) ** 2))
    if first_point_to_center <= second_point_to_center:
        return floor(a1), floor(b1)
    elif first_point_to_center > second_point_to_center:
        return floor(x2), floor(y2)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
result = find_closest_point(x1, y1, x2, y2)
print(result)
