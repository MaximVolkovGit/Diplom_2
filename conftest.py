import pytest
import requests
from helpers.helpers import Person
from data.urls import URL, Endpoints
import allure

@pytest.fixture
def create_new_user():
    with allure.step("Создать тестового пользователя"):
        payload = Person.create_data_correct_user()
        with allure.step("Отправить POST запрос для создания пользователя"):
            response = requests.post(URL.main_url + Endpoints.CREATE_USER, data=payload)
    
    yield payload, response
    
    with allure.step("Удалить тестового пользователя"):
        # Проверяем, что пользователь был успешно создан и есть токен
        if response.status_code == 200 and response.json().get("success"):
            token = response.json()["accessToken"]
            with allure.step("Отправить DELETE запрос для удаления пользователя"):
                requests.delete(URL.main_url + Endpoints.DELETE_USER, headers={"Authorization": token})