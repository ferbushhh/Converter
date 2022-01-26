import re
import main


def test(data):
    output = []

    def _input(item):
        output.append(item)
        return data.pop(0)

    main.input = _input
    main.print = lambda item: output.append(item)
    main.main()
    return output


def correctTestFirst():
    outputFirst = test(['BYN', '258.9'])
    assert outputFirst[0] == "Enter the name of the currency you want to convert from (USD, EUR, BYN, KZT): "
    assert outputFirst[1] == "Enter the amount to be converted: "
    assert re.fullmatch("Total in rubles ([0-9]+.)?[0-9]+ RUB.", outputFirst[2])


def correstTestSecond():
    outputFirst = test(['USD', '3900'])
    assert outputFirst[0] == "Enter the name of the currency you want to convert from (USD, EUR, BYN, KZT): "
    assert outputFirst[1] == "Enter the amount to be converted: "
    assert re.fullmatch("Total in rubles ([0-9]+.)?[0-9]+ RUB.", outputFirst[2])


def wrongTestFirst():
    outputFirst = test(['EUR', '3900,99'])
    assert outputFirst[0] == "Enter the name of the currency you want to convert from (USD, EUR, BYN, KZT): "
    assert outputFirst[1] == "Enter the amount to be converted: "
    assert outputFirst[2] == "!Wrong amount!"


def wrongTestSecond():
    outputFirst = test(['EUR', '39OO.99'])  # вместо 0 буква O
    assert outputFirst[0] == "Enter the name of the currency you want to convert from (USD, EUR, BYN, KZT): "
    assert outputFirst[1] == "Enter the amount to be converted: "
    assert outputFirst[2] == "!Wrong amount!"



def wrongTestThird():
    outputFirst = test(['EURO', '39.99'])  # вместо EUR - EURO
    assert outputFirst[0] == "Enter the name of the currency you want to convert from (USD, EUR, BYN, KZT): "
    assert outputFirst[1] == "!Wrong format!"
