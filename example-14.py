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

