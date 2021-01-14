import pytest


some_string = "any words in this string"

    #Тест на перевод строки в верхний регистр
def test_title():
    assert some_string.upper() == "ANY WORDS IN THIS STRING"

    #Тест на разденелие строки по разделителю
def test_separator():
    assert some_string.split(" ") == ["any","words","in","this","string"]

    #Тест на замену значения в строке
def test_replace():
    assert some_string.replace("this","that") == "any words in that string"

    #Тест на смену регистра для всех символов строки на противоположный
def test_swapcase():
    new_string = "Hi This Is A New String"
    assert new_string.swapcase() == "hI tHIS iS a nEW sTRING"

    #Тест на подсчёт вхождений заданного значения в строку
@pytest.mark.parametrize("given_substring,expected_count",[("any",1),("i",3)])
def test_string(given_substring,expected_count):
    assert some_string.count(given_substring) == expected_count
