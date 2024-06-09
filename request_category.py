from typing import Final

class RequestCategory:
    id: Final[int]
    name: Final[str]

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return f"RequestCategory [ID: {self.id}, Name: {self.name}]"
