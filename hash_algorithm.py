from abc import ABC, abstractmethod


class HashAlgorithm(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def hash(self, text: str) -> str:
        pass

    def __str__(self) -> str:
        return f"HashAlgorithm(name='{self.name}')"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"