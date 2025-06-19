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

