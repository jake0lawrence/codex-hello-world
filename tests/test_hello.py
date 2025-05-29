from hello import greet


def test_greet_default(capsys):
    result = greet()
    captured = capsys.readouterr()
    assert captured.out.strip() == "hello, World!"
    assert result == "hello world"


def test_greet_custom(capsys):
    result = greet("Alice")
    captured = capsys.readouterr()
    assert captured.out.strip() == "hello, Alice!"
    assert result == "hello alice"


def test_greet_case_insensitive(capsys):
    result = greet("ALIce")
    captured = capsys.readouterr()
    assert captured.out.strip() == "hello, ALIce!"
    assert result == "hello alice"
