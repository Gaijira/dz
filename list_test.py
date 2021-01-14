import pytest

city_list = ["Moscow", "Omsk", "Tomsk"]


# Тест1 на добавление в конец листа
def test_append():
    city_list.append("Norilsk")
    assert city_list == ["Moscow", "Omsk", "Tomsk", "Norilsk"]

    # Тест2 на добавление в указанную позицию в листе
@pytest.mark.parametrize("city,new_city_list", [("Minsk",["Minsk", "Moscow", "Omsk", "Tomsk"]),
                                                ("Dzerzhinsk",["Dzerzhinsk","Minsk", "Moscow", "Omsk", "Tomsk"])])
def test_insert(city, new_city_list):
    city_list.insert(0, city)
    assert city_list == new_city_list

    # Тест3 на очистку листа
def test_clear():
    city_list.clear()
    assert city_list == []

    # Тест4 на подсчёт кол-ва элементов в листе с заданным значением
def test_count():
    assert city_list.count("Moscow") == 1

    # Тест5 на удаление элемента из листа
def test_remove():
    city_list.remove("Omsk")
    assert city_list == ["Moscow", "Tomsk"]