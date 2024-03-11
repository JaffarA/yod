from os.path import getsize

import pytest

from utils import get_file_checksum, get_file_info


class TestFileOperations:
    def test_get_file_info(self):
        file_path: str = "/Users/jafjaf/Projects/yod/example_file.txt"
        file = get_file_info(file_path)
        assert file.filename == "example_file.txt"
        assert file.checksum == get_file_checksum(file_path)
        assert file.size == getsize(file_path)
        assert file.path == file_path
