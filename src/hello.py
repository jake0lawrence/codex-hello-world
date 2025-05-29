"""A simple greeting module."""


def greet(name: str = "World") -> str:
    """Return a capitalized greeting for the provided name."""
    return f"Hello, {name.title()}!"


if __name__ == "__main__":  # pragma: no cover
    print(greet("Jake"))
