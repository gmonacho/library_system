import abc
from src.domain.utils import Id


class IdFactory(abc.ABC):
    @abc.abstractmethod
    def generate(self) -> Id:
        pass
