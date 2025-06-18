from typing import List, Tuple, Dict, Union # Use built-in generics in 3.9+

# Example 1: TypeAlias (from Python 3.10)
from typing import TypeAlias
# Defining the alias 
Vector = List[float] # Or `list[float]` in 3.9+

def scale_vector(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# Example 2: `type` statement (from Python 3.12)
type Point = Tuple[int, int] # Or `tuple[int, int]` in 3.9+
type UserDict = Dict[str, Union[str, int, bool]] # Or `dict[str, str | int | bool]` in 3.9+

def get_distance(p1: Point, p2: Point) -> float:
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def process_user_data(user: UserDict) -> str:
    return f"User: {user['name']}, Age: {user['age']}"

# Old way (before 3.10 for TypeAlias, before 3.12 for `type` statement)
# Position = Tuple[float, float, float]
# def get_position() -> Position:
#     return (1.0, 2.0, 3.0)

