import pytest
import allure
import requests

from helpers.helpers import Person
from data.urls import URL, Endpoints

class TestCreateUser:

    @allure.title('Проверка создания уникального пользователя')
    @allure.description('''
                        1. Отправляем запрос на создание пользователя;
                        2. Проверяем ответ;
                        3. Удаляем пользователя.
                        ''')
    def test_create_unique_user_is_created(self, create_new_user):
        response = create_new_user
        assert response[1].json().get("success") == True and response[1].status_code == 200
    

    @allure.title('Проверка создания пользователя, который уже зарегистрирован')
    @allure.description('''
                        1. Отправляем запрос на создание пользователя;
                        2. Получаем данные для регистрации;
                        3. Отправляем повторный запрос на создание пользователя;
                        4. Проверяем ответ;
                        5. Удаляем пользователя.
                        ''')
    def test_create_double_user_is_not_created(self, create_new_user):
        response = create_new_user
        payload = response[0]
        response_double_register = requests.post(URL.main_url + Endpoints.CREATE_USER, data=payload)
        assert response_double_register.status_code == 403 and (
            response_double_register.json().get("message") == 'User already exists'
            )
    
    @allure.title('Проверка создания пользователя без одного обязательного поля')
    @allure.description('''
                        1. Отправляем запрос на создание пользователя без одного поля;
                        2. Проверяем ответ.
                        ''')
    @pytest.mark.parametrize('payload', [
        Person.create_user_without_email(),
        Person.create_user_without_name(),
        Person.create_user_without_password()
    ])
    def test_create_user_no_required_fields_is_not_created(self, payload):
        response = requests.post(URL.main_url + Endpoints.CREATE_USER, data=payload)
        assert response.status_code == 403 and response.json().get("success") == False