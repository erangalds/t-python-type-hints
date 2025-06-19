from typing import TypeVar, List, Generic

# Define a TypeVar (T is a common convention for generic types)
T = TypeVar('T')

# Generic function: operates on a list of any type T, returns an element of type T
def get_first_element(items: List[T]) -> T:
    if not items:
        raise ValueError("List cannot be empty")
    return items[0]

# Works with List[int]
first_int = get_first_element([1, 2, 3])
print(f"First int: {first_int}") # mypy knows first_int is int

# Works with List[str]
first_str = get_first_element(["a", "b", "c"])
print(f"First str: {first_str}") # mypy knows first_str is str

# Mypy error: Incompatible types
# first_float: float = get_first_element(["a", "b"])

# Generic Class: A simple Stack
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def is_empty(self) -> bool:
        return len(self._items) == 0

# Create a stack of integers
int_stack: Stack[int] = Stack()
int_stack.push(10)
int_stack.push(20)
print(int_stack.pop()) # Output: 20 (mypy knows it's an int)
# int_stack.push("hello") # Mypy error!

# Create a stack of strings
str_stack: Stack[str] = Stack()
str_stack.push("apple")
print(str_stack.pop()) # Output: apple (mypy knows it's a str)

