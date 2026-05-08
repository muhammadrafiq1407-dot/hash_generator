import hashlib
from hash_algorithm import HashAlgorithm


class SHA256Hash(HashAlgorithm):

    def __init__(self):
        super().__init__(name="SHA-256")

    def hash(self, text: str) -> str:
        return hashlib.sha256(text.encode()).hexdigest()