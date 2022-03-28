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


def test_with_decimals():
    output = run_c(['BYN', '258.9'])
    assert output[0] == "Enter the name of the currency you want to convert from (USD, EUR, BYN, KZT): "
    assert output[1] == "Enter the amount to be converted: "
    #assert re.fullmatch("Total in rubles ([0-9]+.)?[0-9]+ RUB.", output[2])
    assert True == ("Total in rubles " in output[2])


def test_with_integer():
    output = run_c(['USD', '3900'])
    assert output[0] == "Enter the name of the currency you want to convert from (USD, EUR, BYN, KZT): "
    assert output[1] == "Enter the amount to be converted: "
    #assert re.fullmatch("Total in rubles ([0-9]+.)?[0-9]+ RUB.", output[2])
    assert True == ("Total in rubles " in output[2])

def test_wrong_comma():
    output = run_c(['EUR', '3900,99'])
    assert output[0] == "Enter the name of the currency you want to convert from (USD, EUR, BYN, KZT): "
    assert output[1] == "Enter the amount to be converted: "
    assert output[2] == "!Wrong amount!"


def test_wrong_o():
    output = run_c(['EUR', '39OO.99'])  # вместо 0 буква O
    assert output[0] == "Enter the name of the currency you want to convert from (USD, EUR, BYN, KZT): "
    assert output[1] == "Enter the amount to be converted: "
    assert output[2] == "!Wrong amount!"



def test_wrong_name_currency():
    output = run_c(['EURO', '39.99'])  # вместо EUR - EURO
    assert output[0] == "Enter the name of the currency you want to convert from (USD, EUR, BYN, KZT): "
    assert output[1] == "!Wrong format!"
