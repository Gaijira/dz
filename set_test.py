import pytest


colors = set()

    #Тест на добавление элемента в множество

def test_set_add():
    colors.add("black")
    assert "black" in colors

    #Тест на удаление элемента из множества
@pytest.mark.parametrize("added_color,expected_color",[("white","black")])
def test_remove(added_color,expected_color):
    colors.add(added_color)
    colors.remove(added_color)
    assert colors == {expected_color}

    #Тест на очистку множества
def test_clear():
    colors.add("yellow")
    colors.clear()
    assert colors == set()

    #Тест на удаление случайного элемента из множества
def test_pop():
    colors.add("green")
    colors.pop()
    assert len(colors) == 1

    #Тест  на удаление указанного элемента из множества
def test_discard():
    colors.add("brown")
    colors.discard("brown")
    assert colors == set()