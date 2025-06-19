from typing import TypeVar, Union

# Can only be str or bytes
StrOrBytes = TypeVar('StrOrBytes', str, bytes)

def concat_items(item1: StrOrBytes, item2: StrOrBytes) -> StrOrBytes:
    return item1 + item2

print(concat_items("hello", "world")) # Output: helloworld
print(concat_items(b"hello", b"world")) # Output: b'helloworld'
# print(concat_items("hello", b"world")) # Mypy error: Incompatible types in assignment

