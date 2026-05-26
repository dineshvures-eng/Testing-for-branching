class Greeter:
    def __init__(self, name: str):
        self.name = name

    def greet(self) -> str:
        return f"Hello, {Dinesh}!"


if __name__ == "__main__":
    print(Greeter("Alice").greet())
