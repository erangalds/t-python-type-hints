class Circle:
    pi: float = 3.14159  # Class variable
    radius: float

    def __init__(self, radius: float):
        self.radius: float = radius

    def area(self) -> float:
        return self.pi * (self.radius ** 2)

c = Circle(10.0)
print(f"Circle area: {c.area()}")

