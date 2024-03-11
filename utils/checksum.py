from hashlib import blake2b


def get_file_checksum(path_to_file: str, chunk_size: int = 1024) -> str:
    with open(path_to_file, "rb") as f:
        checksum = blake2b()
        chunk = f.read(chunk_size)
        while chunk:
            checksum.update(chunk)
            chunk = f.read(chunk_size)
        return checksum.hexdigest()
