from faker import Faker


class Person:
        
    """Создать пользователя со всеми валидными данными"""
    @staticmethod
    def create_data_correct_user():
        faker = Faker('ru_RU')
        data = {
            "email": faker.email(),
            "password": faker.password(),
            "name": faker.first_name()
        }
        return data

    """Создать пользователя без майла"""
    @staticmethod
    def create_user_without_email():
        faker = Faker('ru_RU')
        data = {
            "password": faker.password(),
            "name": faker.first_name()
        }
        return data

    """Создать пользователя без пароля"""
    @staticmethod
    def create_user_without_password():
        faker = Faker('ru_RU')
        data = {
            "email": faker.email(),
            "name": faker.first_name()
        }
        return data

    """Создать пользователя без имени"""
    @staticmethod
    def create_user_without_name():
        faker = Faker('ru_RU')
        data = {
            "email": faker.email(),
            "password": faker.password(),
        }
        return data
    
class Ingredients:
    
    """Валидные ингредиенты для бургера"""
    correct_ingredients_data = {"ingredients": ["61c0c5a71d1f82001bdaaa6d",
                                                "61c0c5a71d1f82001bdaaa72", 
                                                "61c0c5a71d1f82001bdaaa72"]}

    """Некорректные ингредиенты для бургера"""
    incorrect_ingredients_data_hash = {"ingredients": ["abc112345", 
                                                       "3254xyz"]}

    """Для бургера без ингредиентов"""
    incorrect_ingredients_data_without_filling = {"ingredients": []}    