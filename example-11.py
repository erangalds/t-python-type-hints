from typing import Any

def process_anything(data: Any) -> Any:
    """Processes data of any type and returns data of any type."""
    print(f"Processing: {data} of type {type(data)}")
    return data

process_anything("hello")
process_anything(123)
process_anything([1, 2, 3])

