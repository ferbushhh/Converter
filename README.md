![master](https://github.com/ferbushhh/Converter/actions/workflows/python-app.yml/badge.svg?branch=master)

# Задание №1
## Конвертер в рубль из других валют

Был разработан скрипт на python, который конвертирует из валют "USD", "EUR", "BYN", "KZT" в российский рубль.

### Алгоритм работы скрипта

1. Вводится название валюты
   1. Проверка на корректность
    
2. Вводится сумма
   1. Проверка суммы на корректность (если дробное, то должна быть точка, а не запятая)
    
3. Находит на веб-странице актуальный курс необходимой валюты

4. Высчитывает и выводит результат

### Пример работы:
```
Enter the name of the currency you want to convert from (USD, EUR, BYN, KZT): KZT
Enter the amount to be converted: 190.560
Total in rubles 33.80572512 RUB.
```
### Запуск скрипта в docker

```
docker build .
docker images
docker run -it <IMAGE>
```
![alt tag](1.png)

