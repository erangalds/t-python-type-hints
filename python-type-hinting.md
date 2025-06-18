# Python Type Hinting: A Comprehensive Training Tutorial

## Table of Contents

1. **Introduction: Why Type Hints?**
    
    - What are Type Hints?
    - Benefits of Type Hinting
    - How Python Remains Dynamically Typed
    - Tools for Static Type Checking (`mypy`)
2. **Beginner Concepts: The Basics of Annotations**
    
    - Basic Built-in Types (`int`, `str`, `bool`, `float`)
    - Type Annotating Variables
    - Type Annotating Function Parameters
    - Type Annotating Function Return Values
    - `None` and `Optional`
    - `Union` for Multiple Types
    - Type Comments (for older Python versions)
3. **Intermediate Concepts: Collections and Custom Types**
    
    - `List`, `Tuple`, `Dict`, `Set`
    - Type Aliases (`TypeAlias` or `type`)
    - `Any` (The Escape Hatch)
    - Custom Classes as Types
    - Class Attributes
    - `Callable` for Functions
    - `Literal` for Specific Values
    - `Final` for Immutable Variables
    - `TypedDict` for Structured Dictionaries
4. **Advanced Concepts: Power-User Type Hinting**
    
    - `TypeVar` and Generics
    - `Protocol` for Structural Subtyping (Duck Typing)
    - `NewType` for Distinct Types
    - `cast()` for Runtime Type Information
    - `overload` for Multiple Signatures
    - `NoReturn` for Functions That Never Return
    - `Annotated` for Adding Metadata
    - Positional-Only and Keyword-Only Arguments
5. **Best Practices and Common Pitfalls**
    
    - Don't Over-Annotate
    - Be Precise But Practical
    - The Importance of `mypy` (Static Type Checkers)
    - Gradual Typing
    - Runtime vs. Static Checking
6. **Hands-on Exercises**
    

---

## 1. Introduction: Why Type Hints?

### What are Type Hints?

What I learnt is that, Type hints (also known as type annotations) are a syntax added to Python (starting with PEP 484 in Python 3.5) that allows you to specify the expected types of variables, function parameters, and return values.

**Example 1:**

```python
# Without type hints
def add(a, b):
    return a + b

# With type hints
def add_with_hints(a: int, b: int) -> int:
    return a + b

print(f'Without Type Hinting: {add(2,3)}')
print(f'With Type Hinting: {add(2,3)}')
```

### Benefits of Type Hinting

1. **Improved Readability and Documentation:**
    - Makes code easier to understand by explicitly stating what types of data a function expects and returns.
    - Acts as a form of "living documentation" that stays in sync with your code.
2. **Enhanced Development Experience (IDE Support):**
    - IDEs (like VS Code, PyCharm) use type hints for better auto-completion, intelligent suggestions, and immediate error detection.
    - Example: If you hint a variable as `str`, your IDE will suggest string methods.
3. **Early Error Detection (Static Analysis):**
    - Tools like `mypy` can analyze your code _before_ you run it, catching type-related bugs that would otherwise only appear at runtime. This saves debugging time.
    - Example: Calling `len(123)` (an `int`) would be flagged by `mypy` if `123` was hinted as an `int`.
4. **Easier Refactoring:**
    - When you change a function's signature, type checkers can help identify all the places in your codebase that need to be updated.
5. **Better Code Quality and Maintainability:**
    - Encourages more thoughtful design and consistency in data handling.
    - Reduces the likelihood of unexpected type errors in production.

### How Python Remains Dynamically Typed

It's crucial to understand that **Python remains a dynamically typed language**. WHat I learnt is taht Type hints are **not enforced at runtime**by the Python interpreter itself. They are simply annotations that can be used by external tools.

**Example 2:**
```python
def greet(name: str) -> str:
    return f"Hello, {name}"

# This will run without a TypeError at runtime,
# even though the type hint says 'name' should be a string.
# A static type checker would flag this.
result = greet(123)
print(result) # Output: "Hello, 123" (runtime behavior)
```

### Tools for Static Type Checking (`mypy`)

To get the most out of type hints, you need a static type checker. The most popular one which I found is `mypy`. I was able to install it as below. 

**Installation:**

```bash
pip install mypy
```

**Usage:** Run `mypy` on your Python file(s):

Bash

```
mypy your_module.py
```

**Example 3:**
Let me put the greet() function I wrote above into a .py file and use *mypy* to evaluate it. 

```bash
cat basic-mypy-usage-example.py
mypy basic-mypy-usage-example.py
```


## 2. Beginner Concepts: The Basics of Annotations

### Basic Built-in Types

What I found is that we can use the standard built-in types directly:

- `int`
- `str`
- `float`
- `bool`
- `bytes`
- `None` (special case, covered below)

### Type Annotating Variables

You can annotate variables during declaration:

**Example 4:**
Let me put below python code into another simple .py file. 

```python
# Basic types
age: int = 30
name: str = "Alice"
price: float = 99.99
is_active: bool = True

# Variable without an initial value
# This is useful for clarity, though `mypy` can often infer
# if you assign later.
country: str
country = "Sri Lanka"

# Bad practice: changing type after assignment (mypy will flag)
greeting: str = "Hello"
greeting = 123 # Mypy error!
```

Then let me try to check this file with *mypy*

```bash
cat basic-variable-type-hinting.py
mypy basic-variable-type-hinting.py
```
### Type Annotating Function Parameters

The biggest benefit of python type hinting for me is using it on python functions. We can place the type hints for the function parameters with a colon `:` after the parameter name, separated by a colon `:`. Also to show the function return type we can use a -> with the return type before the colon `:`.

Let me show try simple example

**Example 5:**

```python
# Function with type hints
# input parameter person_name is a string
# return type is None   
def say_hello(person_name: str) -> None:
    """Greets a person by name."""
    print(f"Hello, {person_name}!")
# input parameters length and width are both float
# return type is float  
def calculate_area(length: float, width: float) -> float:
    """Calculates the area of a rectangle."""
    return length * width

# Calling the functions
say_hello("Bob")
area = calculate_area(5.5, 3.2)
print(f"Area: {area}")
```

What I learnt is that, the code becomes very easy to understand by someone else. This surely reduces the chance of making errors in the code.

### Type Annotating Function Return Values

Place the type hint after the parameter list, separated by `->`.

- If a function doesn't explicitly return a value, its return type is `None`.

**Example 6:**

```python
# Function with type hints
# input parameter first and last both are strings
# return type is a string
def get_full_name(first: str, last: str) -> str:
    """Returns the full name."""
    return f"{first} {last}"
# Input parameter message is a string
# Return type is None
def print_message(message: str) -> None:
    """Prints a message. Returns nothing."""
    print(message)

# Functions returning None
# input event_date is a string
# Since the return type is not explicitly specified, it's None
def log_event(event_data: str):
    """Logs an event. No explicit return type, implies None."""
    print(f"Logging: {event_data}")

# mypy would infer `None` for `log_event` even without `-> None`
# but it's good practice to mention the return type for clarity.
```

Chekcing with *mypy*

```bash
cat example-6.py
mypy example-6.py
```


### `None` and `Optional`

- In Python, `None` is its own special type.
- If a variable or parameter **might be `None`** in addition to another type, you use `Optional` from the `typing` module. This `typing` module is not standard, we have to manually import it in our code.

**Example 7:**

```python
from typing import Optional

def get_user_email(user_id: int) -> Optional[str]:
    """
    Returns user email if found, otherwise None.
    """
    if user_id == 1:
        return "alice@example.com"
    return None

user_email = get_user_email(1)
if user_email: # Recommended way to check for None
    print(f"User email: {user_email.upper()}")
else:
    print("User not found.")

user_email_2 = get_user_email(2)
# mypy will warn if you try to call .upper() on user_email_2 directly
# without a None check, because it knows Optional[str] might be None.
#
# Run mypy again after uncommenting below
# print(user_email_2.upper()) # Mypy error!
```
Let me try to run the above code twice, once without the `.upper()` for the `user_email_2` and with that part of the code.

```bash
cat example-7.py
mypy example-7.py
```

**Note:** `Optional[X]` is simply a shorthand for `Union[X, None]`.

### `Union` for Multiple Types

I came across another very interesting type hint, which is `Union`. Use `Union` when a variable, parameter, or return value could be one of several distinct types.

**Example 8:**

```python
from typing import Union

def process_input(value: Union[str, int]) -> Union[str, int]:
    """
    Processes input which can be a string or an integer.
    Returns processed string or integer.
    """
    if isinstance(value, int):
        return value * 2
    else: # It must be a string
        return value.upper()

print(process_input(10))     # Output: 20
print(process_input("hello")) # Output: HELLO

# Python 3.10+ simplified Union syntax (PEP 604)
def process_input_310_plus(value: str | int) -> str | int:
    """Same as above, using the new pipe syntax."""
    if isinstance(value, int):
        return value * 2
    else:
        return value.upper()
```

**Recommendation:** For Python 3.10+, use the `|` (pipe) operator for `Union` as it's cleaner and more readable.


## 3. Intermediate Concepts: Collections and Custom Types

### `List`, `Tuple`, `Dict`, `Set`

Now let me tell you about more complex data types. Let me start what I learnt about the python collection types. 

For collection types, you need to specify the types of the elements they contain.

**Example 9:**

```python
from typing import List, Tuple, Dict, Set
from typing import Union

# List of integers
numbers: List[int] = [1, 2, 3]

# List of strings
names: List[str] = ["Alice", "Bob", "Charlie"]

# List with both strings and integers
values: List[Union[str, int]] = ["hello", 123]

# Tuple with specific types at each position (fixed size)
user_data: Tuple[str, int, bool] = ("Alice", 30, True)

# Tuple with all elements of the same type (variable size)
# (Used less often than List for homogenous collections)
coordinates: Tuple[float, ...] = (10.5, 20.0, 30.1)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Math": 90, "Science": 85}

# Dictionary with string keys and string or integer values
user_info: Dict[str, Union[str, int]] = {"name": "Alice", "age": 30}

# Set of strings
tags: Set[str] = {"python", "programming", "types"}

# Nested types
data: Dict[str, List[int]] = {"even": [2, 4], "odd": [1, 3]}

# Python 3.9+ simplified generic types (PEP 585)
# You can use `list[int]` instead of `List[int]` etc.
# This is now the preferred way.
new_numbers: list[int] = [1, 2, 3]
new_scores: dict[str, int] = {"Math": 90, "Science": 85}

# Same above in python 3.9+
# List with both strings and integers
values2: list[str | int] = ["hello", 123]

# Dictionary with string keys and string or integer values
user_info2: Dict[str, str | int] = {"name": "Alice", "age": 30}

```

**Recommendation:** For Python 3.9+, use the built-in generics (e.g., `list[int]`) as they are simpler and don't require `from typing import ...`.

### Type Aliases (`TypeAlias` or `type`)

Now, writing these type hints, becomes a little tedious when the variable type becoems a little complex. Specially when that has to be reused multiple time. I was wondering whether there is a workaround to that. Then I got to know about the type aliases to give meaningful names to complex or frequently used type hints, improving readability.

**Example 10:**

```python
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
```

**Recommendation:** Use the `type` statement (Python 3.12+) or `TypeAlias` (Python 3.10+) for aliases as they are explicit and clearer.

### `Any` (The Escape Hatch)

Of course we can use `Union` or the equivalent `|` character with latest versions of python to specify varaibles which can be of multiple types. But sometimes when that list gets a little bigger, the code becomes a little messy. For that I found another workaround with another type hint called `Any`.

`Any` means a variable can be of _any_ type. Use it sparingly, as it defeats the purpose of type hints. It's useful for:

- Dealing with code that is inherently dynamic.
- When integrating with untyped libraries.
- As a temporary placeholder when you're gradually adding type hints.

**Example 11:**

```python
from typing import Any

def process_anything(data: Any) -> Any:
    """Processes data of any type and returns data of any type."""
    print(f"Processing: {data} of type {type(data)}")
    return data

process_anything("hello")
process_anything(123)
process_anything([1, 2, 3])
```

**Caution:** `mypy` will perform no type checking for `Any` types, allowing anything.

### Custom Classes as Types
Now that's not all. We can take this to a even complex levels. We can use our own custom classes as types.

**Example 12:**

```python
# We define a custom class called Dog
class Dog:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    def bark(self) -> str:
        return f"{self.name} says Woof!"

# We use that custom class as a type hint
def get_dog_info(dog: Dog) -> str:
    """Returns information about a dog."""
    return f"Name: {dog.name}, Age: {dog.age}, Bark: {dog.bark()}"

my_dog = Dog("Buddy", 5)
print(get_dog_info(my_dog))
```

### Class Attributes

You can type hint class attributes, including instance variables and class variables.

**Example 13:**

```python
class Circle:
    pi: float = 3.14159  # Class variable
    radius: float

    def __init__(self, radius: float):
        self.radius: float = radius

    def area(self) -> float:
        return self.pi * (self.radius ** 2)

c = Circle(10.0)
print(f"Circle area: {c.area()}")
```

### `Callable` for Functions

Use `Callable` to hint a function (or any callable object) as a parameter or return value. You specify the argument types as a list and the return type.

**Example 14:**

```python
from typing import Callable, List, Any 

# A function that takes an int and returns a str
def format_number(num: int) -> str:
    return f"Number: {num}"

def apply_formatter(numbers: List[int], formatter: Callable[[int], str]) -> List[str]:
    """Applies a formatter function to each number in a list."""
    return [formatter(n) for n in numbers]

numbers_list = [10, 20, 30]
formatted_strings = apply_formatter(numbers_list, format_number)
print(formatted_strings) # Output: ['Number: 10', 'Number: 20', 'Number: 30']

# Callable with no arguments and no return value
def log_action(action: Callable[[], None]) -> None:
    print("Performing action...")
    action()
    print("Action complete.")

def send_notification():
    print("Sending notification...")

log_action(send_notification)

# Callable with arbitrary arguments (use `...`)
def execute_callback(callback: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    """Executes a callback with arbitrary arguments."""
    return callback(*args, **kwargs)

def sum_two(a: int, b: int) -> int:
    return a + b

print(execute_callback(sum_two, 5, 7)) # Output: 12
```

### `Literal` for Specific Values

`Literal` allows you to specify that a variable or parameter can only take a specific set of exact values (string literals, numbers, booleans, `None`).

**Example 15:**

```python
from typing import Literal

# Can only be 'red', 'green', or 'blue'
Color = Literal["red", "green", "blue"]

def set_light_color(color: Color) -> None:
    print(f"Setting light color to: {color}")

set_light_color("red")
# Lets run this code twice with mypy by uncommenting the below line
#
# set_light_color("yellow") # Mypy error!

# Can only be 1, 2, 3
Number = Literal[1, 2, 3]

def process_number(num: Number) -> None:
    print(f"Processing number: {num}")

process_number(2)
# Lets run this code twice with mypy by uncommenting the below line
#
# process_number(4) # Mypy error!
```

### `Final` for Immutable Variables

`Final` indicates that a variable (or class attribute) should not be reassigned after its initial definition. This is a hint to static checkers, not runtime enforcement.

**Example 16:**

```python
from typing import Final

MAX_CONNECTIONS: Final[int] = 100
# Run this code twice with mypy by uncommenting the below line
#   
# MAX_CONNECTIONS = 200 # Mypy error: Cannot assign to final name "MAX_CONNECTIONS"

class Config:
    DEBUG_MODE: Final[bool] = True

    def set_debug(self, value: bool) -> None:
        # self.DEBUG_MODE = value # Mypy error: Cannot assign to final attribute
        pass
```

### `TypedDict` for Structured Dictionaries

`TypedDict` allows you to define a dictionary type with a fixed set of string keys and specific value types for each key. This is incredibly useful for defining structured data.

**Example 17:**

```python
from typing import TypedDict, List, Optional

class User(TypedDict):
    name: str
    age: int
    email: Optional[str] # Optional key
    is_active: bool
    roles: List[str]

def register_user(user_data: User) -> None:
    print(f"Registering user: {user_data['name']}")
    if user_data.get('email'):
        print(f"Email: {user_data['email']}")
    print(f"Roles: {', '.join(user_data['roles'])}")

# Valid usage
new_user: User = {
    "name": "Charlie",
    "age": 25,
    "email": "charlie@example.com",
    "is_active": True,
    "roles": ["viewer"]
}
register_user(new_user)

# Valid usage (email is Optional)
another_user: User = {
    "name": "David",
    "age": 40,
    "is_active": False,
    "roles": ["admin", "editor"]
}
register_user(another_user)

# Mypy error: missing required key 'is_active'
# invalid_user: User = {"name": "Eve", "age": 30}
# register_user(invalid_user)

# Mypy error: 'age' has wrong type
# invalid_user_type: User = {
#     "name": "Frank",
#     "age": "thirty",
#     "is_active": True,
#     "roles": []
# }
# register_user(invalid_user_type)

# You can also set `total=False` to make all keys optional by default
class OptionalUser(TypedDict, total=False):
    name: str
    age: int
    email: str

def update_user(user_update: OptionalUser) -> None:
    print(f"Updating user with: {user_update}")

update_user({"name": "Grace"})
update_user({"email": "grace@example.com", "age": 35})
```

---

## 4. Advanced Concepts: Power-User Type Hinting

### `TypeVar` and Generics

Generics allow you to write functions or classes that operate on types that are not known until runtime, while still maintaining type safety. `TypeVar` defines a type variable that acts as a placeholder for a specific type.

Python

```
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
```

**Constrained `TypeVar`:** You can constrain a `TypeVar` to a specific set of types.

Python

```
from typing import TypeVar, Union

# Can only be str or bytes
StrOrBytes = TypeVar('StrOrBytes', str, bytes)

def concat_items(item1: StrOrBytes, item2: StrOrBytes) -> StrOrBytes:
    return item1 + item2

print(concat_items("hello", "world")) # Output: helloworld
print(concat_items(b"hello", b"world")) # Output: b'helloworld'
# print(concat_items("hello", b"world")) # Mypy error: Incompatible types in assignment
```

### `Protocol` for Structural Subtyping (Duck Typing)

Protocols allow you to define a "shape" or "interface" that a class must conform to, regardless of its inheritance hierarchy. This is very powerful for Python's duck-typing philosophy ("If it walks like a duck and quacks like a duck, it's a duck").

Python

```
from typing import Protocol, runtime_checkable

# Define a protocol for objects that can be drawn
@runtime_checkable # Allows `isinstance` checks at runtime (optional, but useful)
class Drawable(Protocol):
    def draw(self) -> None:
        ... # ... indicates an abstract method that must be implemented

class Circle:
    def draw(self) -> None:
        print("Drawing a circle.")

class Square:
    def draw(self) -> None:
        print("Drawing a square.")

class Text:
    def render(self) -> None: # Doesn't implement 'draw'
        print("Rendering text.")

def render_scene(elements: List[Drawable]) -> None:
    """Renders a list of drawable elements."""
    for element in elements:
        element.draw()

render_scene([Circle(), Square()])

# mypy will flag this because Text does not implement the `draw` method
# render_scene([Circle(), Text()])

# With @runtime_checkable, you can do runtime checks:
my_circle = Circle()
my_text = Text()

print(isinstance(my_circle, Drawable)) # Output: True
print(isinstance(my_text, Drawable))   # Output: False
```

### `NewType` for Distinct Types

`NewType` creates distinct types that are _subtypes_ of an existing type. This improves code clarity and helps catch bugs where you might accidentally mix up semantically different values that happen to have the same underlying type (e.g., a User ID and an Order ID, both represented as `int`).

Python

```
from typing import NewType

UserId = NewType('UserId', int)
ProductId = NewType('ProductId', int)

def get_user_data(user_id: UserId) -> str:
    return f"Fetching data for user ID: {user_id}"

def get_product_info(product_id: ProductId) -> str:
    return f"Fetching info for product ID: {product_id}"

user_id_val = UserId(123)
product_id_val = ProductId(456)

print(get_user_data(user_id_val))
print(get_product_info(product_id_val))

# mypy will flag this, even though both are ints at runtime
# print(get_user_data(product_id_val)) # Mypy error!

# At runtime, NewType instances are just their underlying type:
print(type(user_id_val)) # Output: <class 'int'>
```

`NewType` adds a layer of semantic safety _at the type-checking level_ without runtime overhead.

### `cast()` for Runtime Type Information

`cast()` is a function from `typing` that tells the type checker to treat an expression as if it has a certain type, even if the static checker might not be able to infer it. It does **nothing at runtime**; it's purely for the type checker.

Python

```
from typing import cast, List, Union

def process_data(data: Union[List[int], List[str]]) -> None:
    if isinstance(data, list):
        # Mypy might not know that `data` is now List[int] or List[str]
        # within this block, if the Union was more complex.
        # `cast` helps the type checker here.
        if all(isinstance(x, int) for x in data):
            # Tell mypy that `data` is definitely a List[int] here
            int_list = cast(List[int], data)
            print(f"Processing integers: {sum(int_list)}")
        elif all(isinstance(x, str) for x in data):
            str_list = cast(List[str], data)
            print(f"Processing strings: {' '.join(str_list)}")
    else:
        print("Unexpected data type.")

process_data([1, 2, 3])
process_data(["hello", "world"])

# Be careful: cast can lie to the type checker!
# my_string: str = cast(str, 123) # Mypy won't complain here
# print(my_string.upper()) # This would cause a runtime error
```

Use `cast()` only when you have a good reason to override the type checker's inference, and you are certain about the type at that point in the code.

### `overload` for Multiple Signatures

`@overload` allows you to define multiple distinct type signatures for a single function implementation. This is useful when a function can accept different types of arguments and return different types based on those inputs.

Python

```
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
```

The `@overload` decorated functions only provide type information; the last function definition is the actual runtime implementation.

### `NoReturn` for Functions That Never Return

`NoReturn` indicates that a function will never return normally (e.g., it always raises an exception or enters an infinite loop).

Python

```
from typing import NoReturn

def exit_program(error_code: int) -> NoReturn:
    """Exits the program with a given error code."""
    raise SystemExit(error_code)

def infinite_loop() -> NoReturn:
    """Runs an infinite loop."""
    while True:
        pass

# mypy knows that code after calling these won't be reached
# if you call `exit_program(1)`, mypy assumes the rest of the function is unreachable.
```

### `Annotated` for Adding Metadata

`Annotated` (Python 3.9+) allows you to attach context-specific metadata to types. This metadata is ignored by `mypy` but can be used by other tools (like FastAPI for validation, or Pydantic).

Python

```
from typing import Annotated
from typing import List, Union # Use built-in generics in 3.9+

# Example for FastAPI (though FastAPI has its own `Depends`, `Query`, etc.)
# This is a general example of Annotated usage.

def process_item(
    item_id: Annotated[int, "Item ID from URL", {"min_value": 1}],
    tags: Annotated[List[str], "List of tags", "Must have at least one tag"]
) -> None:
    print(f"Processing item {item_id} with tags: {tags}")

# The annotations "Item ID from URL", {"min_value": 1}, etc.,
# are accessible at runtime via `typing.get_args` and `typing.get_origin`.
import typing

def get_annotations(func: Callable) -> Dict[str, Any]:
    hints = typing.get_type_hints(func, include_extras=True)
    annotated_args = {}
    for param_name, param_type in hints.items():
        if typing.get_origin(param_type) is Annotated:
            base_type, *metadata = typing.get_args(param_type)
            annotated_args[param_name] = {
                "base_type": base_type,
                "metadata": metadata
            }
    return annotated_args

print(get_annotations(process_item))
# Output will show the base types and the metadata
# {
#     'item_id': {'base_type': <class 'int'>, 'metadata': ['Item ID from URL', {'min_value': 1}]},
#     'tags': {'base_type': typing.List[str], 'metadata': ['List of tags', 'Must have at least one tag']}
# }
```

### Positional-Only and Keyword-Only Arguments

Introduced in Python 3.8 (positional-only `/`) and available for type hinting from 3.8.

Python

```
def create_user(
    name: str,
    age: int, /, # All arguments before / are positional-only
    email: str,
    *,           # All arguments after * are keyword-only
    is_admin: bool = False
) -> None:
    print(f"User: {name}, Age: {age}, Email: {email}, Admin: {is_admin}")

# Valid calls:
create_user("Alice", 30, email="alice@example.com")
create_user("Bob", 25, email="bob@example.com", is_admin=True)

# Invalid calls (mypy will warn):
# create_user(name="Charlie", age=35, email="charlie@example.com") # 'name' and 'age' cannot be keyword args
# create_user("David", 40, "david@example.com", True) # 'is_admin' must be keyword arg
```

---

## 5. Best Practices and Common Pitfalls

### Don't Over-Annotate

- **Obvious types:** Don't annotate every single variable if its type is immediately clear from its assignment (e.g., `x = 10` is clearly an `int`). Focus on function signatures and complex data structures.
- **Small scripts:** For quick one-off scripts, full type hinting might be overkill. However, for anything that grows or is shared, it's beneficial.

### Be Precise But Practical

- Strive for precision, but don't get bogged down in overly complex types if the readability cost outweighs the benefits.
- Sometimes `Any` is the pragmatic choice for a small, isolated piece of dynamic code, especially when dealing with external libraries.

### The Importance of `mypy` (Static Type Checkers)

- Type hints are **comments to the type checker**. Without running a type checker like `mypy`, your type hints are just documentation that isn't actively validated.
- Integrate `mypy` into your CI/CD pipeline.
- Consider running `mypy --strict` for new projects or modules to enforce stricter type checking.

### Gradual Typing

- You don't have to type hint your entire codebase at once. Start with new code, critical functions, or areas prone to type-related bugs.
- Use `Any` as a temporary placeholder for parts of the code you haven't fully typed yet.

### Runtime vs. Static Checking

- **Static checking** (by tools like `mypy`) happens _before_ runtime. It helps catch errors early.
- **Runtime behavior** is unaffected by type hints. Python will still execute code even if it violates type hints. If you need runtime type enforcement, consider libraries like `Pydantic` (which FastAPI leverages heavily). Pydantic uses type hints to _enforce_ types and perform data validation at runtime, which is different from `mypy`'s static analysis.

---

## 6. Hands-on Exercises

To make this training truly effective, have your team work through these exercises. Encourage them to run `mypy` after each exercise to see the type checker in action.

**Setup:**

1. Ensure `mypy` is installed (`pip install mypy`).
2. Have them create a file named `exercises.py`.

---

**Exercise 1: Basic Function Type Hinting**

- **Task:** Write a function `greet_user` that takes a `name` (string) and an optional `age` (integer) and prints a greeting. If `age` is provided, include it in the greeting.
- **Expected `mypy` behavior:** No errors.
- **Hint:** Use `Optional`.

Python

```
# exercises.py
# ... (your solution here) ...
```

---

**Exercise 2: Collections and Type Aliases**

- **Task:**
    1. Define a `type` alias called `ProductInfo` for a dictionary that contains `name` (string), `price` (float), and `in_stock` (boolean).
    2. Create a function `calculate_total_price` that takes a `list` of `ProductInfo` dictionaries and calculates the total price of all products.
- **Expected `mypy` behavior:** No errors.
- **Hint:** Use `TypedDict` for `ProductInfo`.

Python

```
# exercises.py
# ... (your solution here) ...
```

---

**Exercise 3: Generics and `TypeVar`**

- **Task:**
    1. Create a generic function `reverse_list` that takes a `list` of any type `T` and returns a new list with the elements in reverse order.
    2. Test it with a list of `int` and a list of `str`.
    3. Try to pass a list of mixed types (e.g., `[1, "a"]`) and see what `mypy` does (it might infer `list[Any]` which is okay, or complain if your `TypeVar` is constrained).
- **Expected `mypy` behavior:** No errors for the `int` and `str` lists.
- **Hint:** Use `TypeVar` and `List[T]`.

Python

```
# exercises.py
# ... (your solution here) ...
```

---

**Exercise 4: Protocol (Duck Typing)**

- **Task:**
    1. Define a `Protocol` called `Loggable` that requires a `log` method which takes a `message` (string) and returns `None`.
    2. Create two classes, `FileLogger` and `DatabaseLogger`, both implementing the `Loggable` protocol.
    3. Write a function `process_logs` that accepts a `list` of `Loggable` objects and calls their `log` method with a generic message.
- **Expected `mypy` behavior:** No errors.
- **Hint:** Use `@runtime_checkable` (optional but good practice for `isinstance` checks).

Python

```
# exercises.py
# ... (your solution here) ...
```

---

**Exercise 5: `NewType` and Type Safety**

- **Task:**
    1. Define two `NewType`s: `EmailAddress` (based on `str`) and `PhoneNumber` (based on `str`).
    2. Write a function `send_contact_info` that takes an `EmailAddress` and a `PhoneNumber`.
    3. Attempt to call `send_contact_info` with a raw string for one of the arguments and observe `mypy`'s error.
- **Expected `mypy` behavior:** An error when passing a raw `str` where `EmailAddress` or `PhoneNumber` is expected.

Python

```
# exercises.py
# ... (your solution here) ...
```

---

This comprehensive tutorial should equip your team with a solid understanding of Python type hinting, from the fundamental concepts to more advanced patterns, and highlight the importance of using a static type checker like `mypy`.