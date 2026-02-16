from hexlet_pytest.reversed import reverse
from pathlib import Path

def get_test_data_path(filename):
    return Path(__file__).parent / "data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


# тестируем функцию process(), которая как-то обрабатывает файл
def test_process():
    before = read_file("before.txt")
    expected = read_file("after.txt")
    actual = reverse(before)

    assert actual == expected