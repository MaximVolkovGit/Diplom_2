import pytest
import requests
from helpers.helpers import Person
from data.urls import URL, Endpoints
import allure

@pytest.fixture
def create_new_user():
    with allure.step("Создать тестового пользователя"):
        payload = Person.create_data_correct_user()
        response = requests.post(URL.main_url + Endpoints.CREATE_USER, data=payload)
    
    yield payload, response
    
    with allure.step("Удалить тестового пользователя"):
        token = response.json()["accessToken"]
        requests.delete(URL.main_url + Endpoints.DELETE_USER, headers={"Authorization": token})