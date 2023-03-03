class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = self.diameter / 2

    def calculate_circumference(self):
        p = Circle.__pi * self.diameter
        return p

    def calculate_area(self):
        a = Circle.__pi * self.radius ** 2
        return a

    def calculate_area_of_sector(self, angle):
        k = angle / 360 * Circle.__pi * self.radius ** 2
        return k
