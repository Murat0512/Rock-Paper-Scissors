import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle(radius={self.radius})"

# Example usage
if __name__ == "__main__":
    c = Circle(5)
    print(f"Area: {c.area()}")
    print(f"Circumference: {c.circumference()}")