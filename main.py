from hash_algorithm import HashAlgorithm
from md5_hash import MD5Hash
from sha1_hash import SHA1Hash
from sha256_hash import SHA256Hash
from sha512_hash import SHA512Hash
from hash_manager import HashManager


def demo_abstraction():
    print("=" * 60)
    print("DEMO 1 — ABSTRACTION")
    print("=" * 60)

    try:
        algo = HashAlgorithm("test")  # akan error
    except TypeError as e:
        print("HashAlgorithm tidak bisa diinstansiasi langsung.")
        print("Error:", e)


def demo_subtyping():
    print("\n" + "=" * 60)
    print("DEMO 2 — SUBTYPING")
    print("=" * 60)

    algo: HashAlgorithm = SHA256Hash()

    text = "Hello, OOP Python!"
    print("Teks input :", text)
    print("Tipe objek :", type(algo).__name__)
    print("Algoritma  :", algo.name)
    print("Hash       :", algo.hash(text))


def demo_polymorphism():
    print("\n" + "=" * 60)
    print("DEMO 3 — POLYMORPHISM")
    print("=" * 60)

    text = "Hello, OOP Python!"

    algorithms: list[HashAlgorithm] = [
        MD5Hash(),
        SHA1Hash(),
        SHA256Hash(),
        SHA512Hash()
    ]

    for algorithm in algorithms:
        result = algorithm.hash(text)
        print(f"{algorithm.name:<8} -> {result}")


def demo_hash_manager():
    print("\n" + "=" * 60)
    print("DEMO 4 — HASH MANAGER")
    print("=" * 60)

    text = "Belajar OOP Python itu seru!"
    manager = HashManager(MD5Hash())

    print(manager.get_info())
    print("Hash:", manager.generate_hash(text))
    print()

    manager.set_algorithm(SHA1Hash())
    print(manager.get_info())
    print("Hash:", manager.generate_hash(text))
    print()

    manager.set_algorithm(SHA256Hash())
    print(manager.get_info())
    print("Hash:", manager.generate_hash(text))
    print()

    manager.set_algorithm(SHA512Hash())
    print(manager.get_info())
    print("Hash:", manager.generate_hash(text))


if __name__ == "__main__":
    demo_abstraction()
    demo_subtyping()
    demo_polymorphism()
    demo_hash_manager()