import pytest

books = {}

    #Тест на добавление элемента в словарь
def test_update():
    books.update({"Idiot":345})
    assert "Idiot" in books

    #Тест на получение элемента словаря по ключу
def test_get():
    books.update({"War and peace": 3000})
    assert 3000 == books.get("War and peace")

    #Тест на очистку словаря
def test_clear():
    books.update({"Dreamcatcher": 250})
    assert None == books.clear()

    #Тест на удаление элемента в словаре
def test_pop():
    books.update({"Dreamcatcher": 250})
    assert 250 == books.pop("Dreamcatcher")

    #Тест на возврат значения ключа и создание нового при его отсутствии
@pytest.mark.parametrize("expected,given_key",[(None,"Johns"),(250,"Dreamcatcher")])
def test_setdefault(given_key,expected):
    books.update({"Dreamcatcher": 250})
    assert books.setdefault(given_key) == expected











