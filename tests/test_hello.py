from pathlib import Path
import sys

# Allow importing hello module from src
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from hello import greet


def test_greet_default():
    assert greet() == "Hello, World!"


def test_greet_custom():
    assert greet("Alice") == "Hello, Alice!"
