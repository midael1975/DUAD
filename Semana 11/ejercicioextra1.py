class Rectangle:
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Width and height cannot be negative.")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


try:
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))

    rect = Rectangle(width, height)

    print(f"Area: {rect.get_area()}")
    print(f"Perimeter: {rect.get_perimeter()}")

except ValueError as e:
    print("Error:", e)
    print("Please enter valid numeric values for width and height.")