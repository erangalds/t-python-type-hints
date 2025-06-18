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

