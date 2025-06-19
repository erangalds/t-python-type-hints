How it Works (with Examples):

All elements are truthy:

python
my_list1 = [True, 1, "hello", [1, 2]]
print(all(my_list1))  # Output: True
# True is truthy
# 1 is truthy
# "hello" is truthy
# [1, 2] (a non-empty list) is truthy
One or more elements are falsy:

python
my_list2 = [True, 0, "hello"] # 0 is falsy
print(all(my_list2))  # Output: False

my_list3 = ["apple", "", "banana"] # "" (empty string) is falsy
print(all(my_list3))  # Output: False

my_list4 = [1, 2, None, 4] # None is falsy
print(all(my_list4))  # Output: False
Empty iterable:

python
empty_list = []
print(all(empty_list))  # Output: True

empty_tuple = ()
print(all(empty_tuple)) # Output: True
Short-circuiting behavior:

python
def check_value(x):
    print(f"Checking {x}")
    return bool(x)

# The function will only be called for 1 and then 0.
# It stops at 0 because 0 is falsy. "hello" won't be checked.
result = all(check_value(i) for i in [1, 0, "hello"])
print(f"Result: {result}")
# Output:
# Checking 1
# Checking 0
# Result: False
Common Use Cases:

Validating conditions:

python
conditions = [
    is_user_active,
    has_user_permission,
    is_data_valid
]
if all(conditions):
    print("All conditions met. Proceeding...")
else:
    print("Some conditions failed.")
Checking properties of items in a collection:

python
numbers = [2, 4, 6, 8, 10]
# Check if all numbers are even
if all(num % 2 == 0 for num in numbers):
    print("All numbers are even.")

strings = ["hello", "world", "python"]
# Check if all strings have length > 3
if all(len(s) > 3 for s in strings):
    print("All strings are longer than 3 characters.")
(The (expression for item in iterable) syntax creates a generator expression, which is memory-efficient for all() as it generates items one by one.)

Form validation (simple example):

python
form_fields = {
    "username": "testuser",
    "password": "password123",
    "email": "" # Empty email
}
# Check if all required fields (values) are filled
if all(form_fields.values()):
    print("Form is valid (all fields filled).")
else:
    print("Form is invalid (some fields are empty).") # This will be printed
In essence, all() is a concise and Pythonic way to determine if an entire collection of items meets a "truthy" criterion.

Context Sources (12)

