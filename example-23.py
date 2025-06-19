from typing import overload, Union

# Overload 1: if 'arg' is int, return int
@overload
def process_value(arg: int) -> int:
    ... # '...' indicates no implementation here, only signature

# Overload 2: if 'arg' is str, return str
@overload
def process_value(arg: str) -> str:
    ...

# Overload 3: if 'arg' is a list of int, return float
@overload
def process_value(arg: list[int]) -> float:
    ...

# The actual implementation (must be type-compatible with all overloads)
# This one is executed at runtime.
def process_value(arg: Union[int, str, list[int]]) -> Union[int, str, float]:
    if isinstance(arg, int):
        return arg * 2
    elif isinstance(arg, str):
        return arg.upper()
    elif isinstance(arg, list) and all(isinstance(x, int) for x in arg):
        return sum(arg) / len(arg) if arg else 0.0
    else:
        raise TypeError("Unsupported argument type")

# Mypy will use the correct overload signature:
x: int = process_value(10)      # mypy knows x is int
y: str = process_value("hello") # mypy knows y is str
z: float = process_value([1, 2, 3]) # mypy knows z is float

# Mypy error: No overload matches this call
# result = process_value(True)
# result = process_value([1, "a"])

