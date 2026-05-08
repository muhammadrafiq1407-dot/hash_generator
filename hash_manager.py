from hash_algorithm import HashAlgorithm


class HashManager:
    def __init__(self, algorithm: HashAlgorithm):
        self.algorithm: HashAlgorithm = algorithm

    def set_algorithm(self, algo: HashAlgorithm) -> None:
        self.algorithm = algo
        print(f"[HashManager] Algoritma aktif diganti ke: {algo.name}")

    def generate_hash(self, text: str) -> str:
        return self.algorithm.hash(text)

    def get_info(self) -> str:
        return f"Algoritma aktif: {self.algorithm.name} ({self.algorithm.__class__.__name__})"