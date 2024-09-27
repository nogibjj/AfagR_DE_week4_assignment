from main import multiply


def test_multiply():
    """testing for multiply function"""
    assert multiply(5, 4) == "Multiply 5 by 4, result is 20."


if __name__ == "__main__":
    test_multiply()
