"""Band class for the Musician/Guitar association example."""
from typing import List
from musician import Musician

class Band:
    """A Band 'has' Musicians (aggregation)."""
    def __init__(self, name: str):
        self.name = name
        self.musicians: List[Musician] = []

    def add(self, musician: Musician) -> None:
        """Add a Musician to the band."""
        self.musicians.append(musician)

    def __str__(self) -> str:
        return f"{self.name} ({', '.join(str(m) for m in self.musicians)})"

    def play(self) -> str:
        """Return performance lines, one per Musician."""
        lines = []
        for m in self.musicians:
            lines.append(m.play())
        return "\n".join(lines)
