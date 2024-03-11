from os.path import getsize

from pydantic import BaseModel

from .checksum import get_file_checksum


class File(BaseModel):
    filename: str
    checksum: str
    size: int
    parts: dict[int, str] = {}
    path: str | None = None


def get_file_info(path: str) -> File:
    return File(
        filename="example_file.txt",
        checksum=get_file_checksum(path),
        size=getsize(path),
        parts={},
        path=path,
    )


def file_to_bytes(file: File) -> bytes:
    if file.path is None:
        raise ValueError("File path is None")
    with open(file.path, "rb") as f:
        return f.read()
