from typing import Annotated,Callable, Dict, Any
from typing import List, Union # Use built-in generics in 3.9+

# Example for FastAPI (though FastAPI has its own `Depends`, `Query`, etc.)
# This is a general example of Annotated usage.

def process_item(
    item_id: Annotated[int, "Item ID from URL", {"min_value": 1}],
    tags: Annotated[List[str], "List of tags", "Must have at least one tag"]
) -> None:
    print(f"Processing item {item_id} with tags: {tags}")

# The annotations "Item ID from URL", {"min_value": 1}, etc.,
# are accessible at runtime via `typing.get_args` and `typing.get_origin`.
import typing

def get_annotations(func: Callable) -> Dict[str, Any]:
    hints = typing.get_type_hints(func, include_extras=True)
    annotated_args = {}
    for param_name, param_type in hints.items():
        if typing.get_origin(param_type) is Annotated:
            base_type, *metadata = typing.get_args(param_type)
            annotated_args[param_name] = {
                "base_type": base_type,
                "metadata": metadata
            }
    return annotated_args

print(get_annotations(process_item))
# Output will show the base types and the metadata
# {
#     'item_id': {'base_type': <class 'int'>, 'metadata': ['Item ID from URL', {'min_value': 1}]},
#     'tags': {'base_type': typing.List[str], 'metadata': ['List of tags', 'Must have at least one tag']}
# }

