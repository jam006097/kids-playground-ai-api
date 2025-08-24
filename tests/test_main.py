from src.ai_api.main import greet


def test_greet():
    """
    greet関数が期待される挨拶文を返すことをテストする。
    """
    assert greet("World") == "Hello, World!"
