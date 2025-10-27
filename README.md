# Дипломный проект. Задание 2: Автотесты для API

Тестирование эндпоинтов API для сервиса  "Stellar Burger".

## Файлы:
- allure_results - каталог с отчетом о тестировании
- data/urls - файл с URL сервиса и ручками
- helpers/helpers.py - файл с методами создания тестовых данных
- tests/test_create_order.py - файл с проверками создания заказов 
- tests/test_create_user.py - файл с проверками создания пользователя
- tests/test_login.py - файл с проверками авторизации пользователя
- requirements.txt - файл с внешними зависимостями
- conftest.py - файл с фикстурой

Перед работой с репозиторием требуется установить зависимости 
```
pip install -r requirements.txt
```
Запустить все тесты
```
pytest tests --alluredir=allure_results
```
Посмотреть отчет о тестировании
```
allure serve allure_results
```