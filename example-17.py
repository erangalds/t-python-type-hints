from typing import TypedDict, List, Optional, NotRequired

# User with email as an optional. But the key should be present. 
# The email key can have either a string or None.
class User(TypedDict):
    name: str
    age: int
    email: Optional[str] # Optional key
    is_active: bool
    roles: List[str]

# Another User definition.
# Email key is not required but if key is present then it should be a string or None.
class User2(TypedDict):
    name: str
    age: int
    email: NotRequired[Optional[str]]
    is_active: bool
    roles: List[str]

# Another User definition
# Email key is not required, but if present, it should be a string.
class User3(TypedDict):
    name: str
    age: int
    email: NotRequired[str]
    is_active: bool
    roles: List[str]

def register_user(user_data: User) -> None:
    print(f"Registering user: {user_data['name']}")
    if user_data.get('email'):
        print(f"Email: {user_data['email']}")
    print(f"Roles: {', '.join(user_data['roles'])}")

# Revising the Register User function accordingly
def register_user2(user_data: User2) -> None:
    print(f"Registering user: {user_data['name']}")
    if user_data.get('email'):
        print(f"Email: {user_data['email']}")
    print(f"Roles: {', '.join(user_data['roles'])}")
# Revising the Register User function accordingly
def register_user3(user_data: User3) -> None:
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

# Valid usage (email is not available hence setting to None)
another_user: User = {
    "name": "David",
    "age": 40,
    "email": None,
    "is_active": False,
    "roles": ["admin", "editor"]
}
register_user(another_user)

# Valid usage (email if present is a string, if not present then None)
another_user2_1: User2 = {
    "name": "David",
    "age": 40,
    "is_active": False,
    "roles": ["admin", "editor"]
}
register_user2(another_user2_1)

another_user2_2: User2 = {
    "name": "David",
    "age": 40,
    "email": None,
    "is_active": False,
    "roles": ["admin", "editor"]
}
register_user2(another_user2_2)

another_user2_3: User2 = {
    "name": "David",
    "age": 40,
    "email": "david@example.com",
    "is_active": False,
    "roles": ["admin", "editor"]
}
register_user2(another_user2_3)


# Valid usage (email if present is a string, but can't be a None)
another_user3_1: User3 = {
    "name": "David",
    "age": 40,
    "is_active": False,
    "roles": ["admin", "editor"]
}
register_user3(another_user3_1)

another_user3_2: User3 = {
    "name": "David",
    "age": 40,
    "email": "david@example.com",
    "is_active": False,
    "roles": ["admin", "editor"]
}
register_user3(another_user3_2)

# Run the above code twice with mypy by uncommenting the below line
#
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

