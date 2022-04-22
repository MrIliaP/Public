from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os


pf = PetFriends()



def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert  status == 200
    assert  len(result['pets']) > 0


def test_post_new_pet_with_valid_key(name='bob', animal_type='kot', age='7', pet_photo='images/lis.jpeg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_delete_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "bob", "kot", "7", "images/lis.jpeg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in my_pets.values()

def test_put_pet(name='dron', animal_type='dudos', age='5'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['name'] == name
    else:
        raise Exception('No pets')

def test_post_new_pet_simple_with_valid_key(name='bob', animal_type='kot', age='7'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_add_photo_of_pet(pet_photo='images/lis.jpeg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    if len(my_pets['pets']) > 0:
        status, result = pf.update_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)

        assert status == 200
        assert len(result['pet_photo']) > 0
    else:
        raise Exception('No pets')

    #3
def test_get_api_key_for_INvalid_user(email=invalid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result
    #4
def test_get_api_key_for_valid_user_invalid_password(email=valid_email, password=invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result
    #5
def test_add_wrong_format_photo_of_pet(pet_photo='images/wrong_format.HEIC'):
    """Метод загрузки фото неподходящего формата. Метод делает запрос к API сервера и возвращает статус запроса"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    if len(my_pets['pets']) > 0:
        status, result = pf.update_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)

        assert status == 500
    else:
        raise Exception('No pets')
    #6
def test_get_my_pets_with_valid_key(filter='my_pets'):
    """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
            со списком найденных питомцев, совпадающих с фильтром 'my_pets' - получить список
            собственных питомцев"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        assert  status == 200
        assert  len(result['pets']) > 0
    else:
        raise Exception('No My pets')
    #7
def test_delete_someones_pet():
    """Метод отправляет на сервер запрос на удаление питомца по указанному ID и возвращает
            статус запроса и результат в формате JSON с текстом уведомления о успешном удалении.
            На сегодняшний день тут есть баг - удаляется чужой питомец"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pets = pf.get_list_of_pets(auth_key, "")

    pet_id = pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, pets = pf.get_list_of_pets(auth_key, "")

    assert status == 200
    assert pet_id not in pets.values()
    #8
def test_add_photo_for_someones_pet(pet_photo='images/lis.jpeg'):
    """Метод отправляет запрос на сервер об обновлении данных чужого питомца по указанному ID и
            возвращает статус запроса"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, all_pets = pf.get_list_of_pets(auth_key, "")
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    status, result = pf.update_photo(auth_key, all_pets['pets'][0]['id'], pet_photo)

    assert status == 500
    #9
def test_change_someones_pet_data(name='dron', animal_type='dudos', age='5'):
    """Метод отправляет запрос на сервер о обновлении данных чужого питомуа по указанному ID и
            возвращает статус запроса и result в формате JSON с обновлённыи данными питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, all_pets = pf.get_list_of_pets(auth_key, "")

    status, result = pf.update_pet(auth_key, all_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    #10
def test_post_new_pet_with_valid_key_and_age_as_string(name='7', animal_type='6', age='bob', pet_photo='images/lis.jpeg'):
    """Метод отправляет (постит) на сервер данные о добавляемом питомце 'age' со значением 'string' и возвращает статус
            запроса на сервер и результат в формате JSON с данными добавленного питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['age'] == age
