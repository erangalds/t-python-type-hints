from typing import Literal

# Can only be 'red', 'green', or 'blue'
Color = Literal["red", "green", "blue"]

def set_light_color(color: Color) -> None:
    print(f"Setting light color to: {color}")

set_light_color("red")
# Lets run this code twice with mypy by uncommenting the below line
#
set_light_color("yellow") # Mypy error!

# Can only be 1, 2, 3
Number = Literal[1, 2, 3]

def process_number(num: Number) -> None:
    print(f"Processing number: {num}")

process_number(2)
# Lets run this code twice with mypy by uncommenting the below line
#
process_number(4) # Mypy error!

