import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('/Users/Dasha/Desktop/project/chromedriver')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


def test_login():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('pozhilenkov@gmail.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('12345')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
   #pytest.driver.find_element_by_css_selector('a[href="/my_pets"]').click()
   #assert  pytest.driver.find_element_by_tag_name('h2').text == "ilia"

def test_login_my_pets():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('pozhilenkov@gmail.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('12345')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
   # Go to My Pets web page
   pytest.driver.find_element_by_css_selector('a[href="/my_pets"]').click()
   assert  pytest.driver.find_element_by_tag_name('h2').text == "ilia"

#Code from module
def test_attributes():
   test_login()
   images = pytest.driver.find_elements_by_css_selector('.card-deck.card-img-top')
   names = pytest.driver.find_elements_by_css_selector('.card-deck.card-title')
   descriptions = pytest.driver.find_elements_by_css_selector('.card-deck.card-text')
   pytest.driver.save_screenshot('result.png')

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0


#1 test
def test_all_pets():
   #Number of pets on the list and in statistic are the same
   test_login_my_pets()
   pets_stat = pytest.driver.find_element_by_css_selector('html > body > div > div > div')
   pets_onpage = pytest.driver.find_elements_by_css_selector('tbody tr')
   assert (str(len(pets_onpage)) in pets_stat.text)
   if len(pets_onpage) > 0:
      print(f'There are {len(pets_onpage)} pets on your list')
   else:
      print('There is no pet on your list')

#2 test
def test_photo():
   #At least half of my pets have a photo
   test_login_my_pets()
   pets_onpage = len(pytest.driver.find_elements_by_css_selector('tbody tr'))
   pets_NO_img = len(pytest.driver.find_elements_by_css_selector('tbody tr img[src=""]'))
   pets_img = pets_onpage - pets_NO_img
   assert pets_img >= pets_onpage/2, "More than a half of pets with no image"


#3 test
def test_pets_have_name_age_breed():
   #Every pet has name, age, breed
   test_login_my_pets()
   pets_atr = pytest.driver.find_elements_by_css_selector('div tr td')
   pets_data = [pet.text for pet in pets_atr]
   assert '' not in pets_data, "Pets parameter is missing"
   #for i in range(len(pets_atr)):
   #   assert pets_atr[i].text != ''

#4 test
def test_pets_no_repeated_names():
   #Every pet has unique name
   test_login_my_pets()
   pets_atr = pytest.driver.find_elements_by_css_selector('div tr td')
   pets_data = [pet.text for pet in pets_atr]
   pet_names = pets_data[::4]
   unique_names = list(set(pet_names))
   pet_names.sort()
   unique_names.sort()
   assert pet_names == unique_names, 'There are repeated names'


#5 test
def test_no_repeated_pets():
   #Every pet is unique
   test_login_my_pets()
   pets_atr = pytest.driver.find_elements_by_css_selector('tbody tr')
   pets_data = [pet.text for pet in pets_atr]
   unique_pets = list(set(pets_data))
   pets_data.sort()
   unique_pets.sort()
   print(pets_data)
   print(unique_pets)
   assert pets_data == unique_pets, 'There are repeated pets'


#Yavnoe ozhidanie
def test_all_pets_yavnoe():
   # Number of pets on the list and in statistic are the same
   test_login()
   pytest.driver.get("https://petfriends.skillfactory.ru/my_pets")
   WebDriverWait(pytest.driver, 10).until((EC.presence_of_element_located(By.ID, "all_my_pets")))

   pets_stat = pytest.driver.find_element_by_css_selector('html > body > div > div > div')
   pets_onpage = pytest.driver.find_elements_by_css_selector('tbody tr')
   assert (str(len(pets_onpage)) in pets_stat.text)
   if len(pets_onpage) > 0:
      print(f'There are {len(pets_onpage)} pets on your list')
   else:
      print('There is no pet on your list')


#NEyavnoe ozhidanie
def test_pets_have_name_age_breed_neyavnoe():
   #Every pet has name, age, breed
   test_login()
   pytest.driver.implicitly_wait(10)
   pytest.driver.get("https://petfriends.skillfactory.ru/my_pets")
   tag_img = pytest.driver.find_element_by_tag_name("img")
   tag_name_age = pytest.driver.find_elements_by_tag_name("td")
   pets_atr = pytest.driver.find_elements_by_css_selector('div tr td')
   pets_data = [pet.text for pet in pets_atr]
   assert '' not in pets_data, "Pets parameter is missing"
