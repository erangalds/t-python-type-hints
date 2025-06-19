from typing import cast, List, Union

def process_data(data: Union[List[int], List[str]]) -> None:
    if isinstance(data, list):
        # Mypy might not know that `data` is now List[int] or List[str]
        # within this block, if the Union was more complex.
        # `cast` helps the type checker here.
        if all(isinstance(x, int) for x in data):
            # Tell mypy that `data` is definitely a List[int] here
            int_list = cast(List[int], data)
            print(f"Processing integers: {sum(int_list)}")
        elif all(isinstance(x, str) for x in data):
            str_list = cast(List[str], data)
            print(f"Processing strings: {' '.join(str_list)}")
    else:
        print("Unexpected data type.")

process_data([1, 2, 3])
process_data(["hello", "world"])

# Be careful: cast can lie to the type checker!
# my_string: str = cast(str, 123) # Mypy won't complain here
# print(my_string.upper()) # This would cause a runtime error

