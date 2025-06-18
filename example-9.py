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

