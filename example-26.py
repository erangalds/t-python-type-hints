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

