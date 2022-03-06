import re
import main


def run_c(test_input):
    data = test_input
    output = []

    def _input(item):
        output.append(item)
        return data.pop(0)

    main.input = _input
    main.print = lambda item: output.append(item)
    main.main()
    return output


<<<<<<< HEAD
def test_with_decimals():
=======
def correctTestFirst():
>>>>>>> 2c353c5 (update tests.py)
    outputFirst = run_c(['BYN', '258.9'])
    assert outputFirst[0] == "Enter the name of the currency you want to convert from (USD, EUR, BYN, KZT): "
    assert outputFirst[1] == "Enter the amount to be converted: "
    assert outputFirst[2] == "Total in rubles 8844.748919999998 RUB."


<<<<<<< HEAD

def test_with_integer():
=======
def correstTestSecond():
>>>>>>> 2c353c5 (update tests.py)
    outputFirst = run_c(['USD', '3900'])
    assert outputFirst[0] == "Enter the name of the currency you want to convert from (USD, EUR, BYN, KZT): "
    assert outputFirst[1] == "Enter the amount to be converted: "
    assert outputFirst[2] == "Total in rubles 412668.36 RUB."


<<<<<<< HEAD
def test_wrong_comma():
=======
def wrongTestFirst():
>>>>>>> 2c353c5 (update tests.py)
    outputFirst = run_c(['EUR', '3900,99'])
    assert outputFirst[0] == "Enter the name of the currency you want to convert from (USD, EUR, BYN, KZT): "
    assert outputFirst[1] == "Enter the amount to be converted: "
    assert outputFirst[2] == "!Wrong amount!"


<<<<<<< HEAD
def test_wrong_o():
=======
def wrongTestSecond():
>>>>>>> 2c353c5 (update tests.py)
    outputFirst = run_c(['EUR', '39OO.99'])  # вместо 0 буква O
    assert outputFirst[0] == "Enter the name of the currency you want to convert from (USD, EUR, BYN, KZT): "
    assert outputFirst[1] == "Enter the amount to be converted: "
    assert outputFirst[2] == "!Wrong amount!"



<<<<<<< HEAD
def test_wrong_name_currency():
=======
def wrongTestThird():
>>>>>>> 2c353c5 (update tests.py)
    outputFirst = run_c(['EURO', '39.99'])  # вместо EUR - EURO
    assert outputFirst[0] == "Enter the name of the currency you want to convert from (USD, EUR, BYN, KZT): "
    assert outputFirst[1] == "!Wrong format!"
