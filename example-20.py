from typing import List, Protocol, runtime_checkable

# Define a protocol for objects that can be drawn
@runtime_checkable # Allows `isinstance` checks at runtime (optional, but useful)
class Drawable(Protocol):
    def draw(self) -> None:
        ... # ... indicates an abstract method that must be implemented

class Circle:
    def draw(self) -> None:
        print("Drawing a circle.")

class Square:
    def draw(self) -> None:
        print("Drawing a square.")

class Text:
    def render(self) -> None: # Doesn't implement 'draw'
        print("Rendering text.")

def render_scene(elements: List[Drawable]) -> None:
    """Renders a list of drawable elements."""
    for element in elements:
        element.draw()

render_scene([Circle(), Square()])

# mypy will flag this because Text does not implement the `draw` method
# render_scene([Circle(), Text()])

# With @runtime_checkable, you can do runtime checks:
my_circle = Circle()
my_text = Text()

print(isinstance(my_circle, Drawable)) # Output: True
print(isinstance(my_text, Drawable))   # Output: False

