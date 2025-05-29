# BAD CODE on purpose 🚨
def greet(name: str = "World") -> str:
    """Print a greeting and return it in lowercase."""

    print(f"hello, {name}!")
    return "hello " + name.lower()


if __name__ == "__main__":
    print(greet("Jake"))
