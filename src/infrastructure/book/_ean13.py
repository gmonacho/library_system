import barcodenumber
from src.domain.utils import Id


class Ean13(Id):
    def __init__(self, code: str) -> None:
        if not barcodenumber.check_code_ean13(code):
            raise ValueError(f"Ean13 `{code}` is invalid")
        self._code = code

    def __str__(self) -> str:
        return self._code
