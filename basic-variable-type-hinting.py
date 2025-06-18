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

