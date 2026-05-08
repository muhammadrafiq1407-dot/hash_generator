import hashlib
from hash_algorithm import HashAlgorithm


class SHA512Hash(HashAlgorithm):
    def __init__(self):
        super().__init__(name="SHA-512")

    def hash(self, text: str) -> str:
        return hashlib.sha512(text.encode()).hexdigest()