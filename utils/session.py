from random import choice
from string import ascii_letters, digits

from pydantic import BaseModel

all_chars: str = f"{ascii_letters}{digits}"


def get_random_char() -> str:
    return choice(all_chars)


def generate_session_id() -> str:
    session_id: list[str] = [get_random_char() for _ in range(32)]
    return "".join(session_id)


class Session(BaseModel):
    session_id: str | None = None
    filename: str
    checksum: str
    size: int
    parts: dict[int, str] = {}
