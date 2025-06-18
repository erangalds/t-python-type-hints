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

