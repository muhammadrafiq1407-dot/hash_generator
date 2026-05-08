import hashlib
from hash_algorithm import HashAlgorithm


class MD5Hash(HashAlgorithm):
    def __init__(self):
        super().__init__(name="MD5")

    def hash(self, text: str) -> str:
        return hashlib.md5(text.encode()).hexdigest()