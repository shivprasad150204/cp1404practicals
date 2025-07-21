
class ProgrammingLanguage:
    """A programming language with typing, reflection, and year info."""

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if language uses dynamic typing."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
