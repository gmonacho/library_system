import abc
from typing import Self, SupportsInt


class Id(abc.ABC):
    @abc.abstractmethod
    def __str__(self) -> str:
        pass

    @abc.abstractmethod
    def from_string(self) -> Self:
        pass


class Quantity(int):
    def __init__(self, x: SupportsInt):
        self._x = int(x)
        if self._x < 0:
            raise ValueError(f"{x} is a invalid Quantity")
