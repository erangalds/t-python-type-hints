# We define a custom class called Dog
class Dog:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    def bark(self) -> str:
        return f"{self.name} says Woof!"
# We use that custom class as a type hint
def get_dog_info(dog: Dog) -> str:
    """Returns information about a dog."""
    return f"Name: {dog.name}, Age: {dog.age}, Bark: {dog.bark()}"

my_dog = Dog("Buddy", 5)
print(get_dog_info(my_dog))

