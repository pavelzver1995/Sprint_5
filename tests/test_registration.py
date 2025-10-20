import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.locators import Locators
from utils.generator import EmailPasswordGenerator
from utils.data import Credential
from utils.urls import main_site, register_site

class TestCheckNewRegister:
    def test_registration(self, register_new_account):
        driver, email, password = register_new_account
        driver.maximize_window()

        # Ищем поле "email" и заполняем его
        driver.find_element(*Locators.field_email).send_keys(email)

        # Ищем поле "Пароль" и заполняем его
        driver.find_element(*Locators.field_password).send_keys(password)

        # Находим надпись "войти" и жмем
        driver.find_element(*Locators.button_entrance).click()

        # Ждем перехода на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        # Проверяем что мы авторизовались созданным аккаунтом перейдя на главную страницу
        assert driver.current_url == main_site


class TestCheckingCreationExistingAccount:
    def test_existing_account(self, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()

        driver.find_element(*Locators.inscription_login).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.field_name))

        # Заполняем поля существующими данными
        driver.find_element(*Locators.field_name).send_keys(Credential.name)
        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver.find_element(*Locators.field_password).send_keys(Credential.password)

        # Жмем на зарегистрироваться
        driver.find_element(*Locators.button_login).click()

        # Проверяем что остались на странице регистрации
        WebDriverWait(driver, 10).until(EC.url_to_be(register_site))
        assert driver.current_url == register_site                                             


class TestCheckRegisterNoName:
    def test_registration_no_name(self, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()
                
        # Кликаем по надписи "Зарегистрироваться"
        driver.find_element(*Locators.inscription_login).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.field_email))

        # Генерация email и password
        generator = EmailPasswordGenerator()
        email, password = generator.generate()

        # Ищем поле "email" и заполняем его
        driver.find_element(*Locators.field_email).send_keys(email)

        # Ищем поле "Пароль" и заполняем его
        driver.find_element(*Locators.field_password).send_keys(password)

        # Жмем на кнопку зарегаться
        driver.find_element(*Locators.button_login).click()

        # Проверяем что мы на странице регистрации
        assert driver.current_url == register_site


class TestCheckingErrorPassword:
    def test_error_password(self, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()

        driver.find_element(*Locators.inscription_login).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.field_name))

        # Находим поле "Имя" и заполняем его
        driver.find_element(*Locators.field_name).send_keys(Credential.name)

        # Находим поле "email" и заполняем его
        driver.find_element(*Locators.field_email).send_keys(Credential.email)

        # Находим поле "Пароль" и заполняем его
        driver.find_element(*Locators.field_password).send_keys("456")

        # Жмем на зарегаться
        driver.find_element(*Locators.button_login).click()

        # Ждем ошибку регистрации
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_error_password))


class TestCheckingNoPassword:
    def test_no_password(self, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()

        # Ждем и прокручиваем к кнопке "Зарегистрироваться"
        register_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.inscription_login)
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", register_link)
        time.sleep(1)
        register_link.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.field_name))

        # Находим поле "Имя" и заполняем его
        driver.find_element(*Locators.field_name).send_keys(Credential.name)

        # Находим поле "email" и заполняем его
        driver.find_element(*Locators.field_email).send_keys(Credential.email)

        # Жмем на зарегистрироваться
        driver.find_element(*Locators.button_login).click()

        # Проверка текущего URL, должны остаться на странице регистрации
        assert driver.current_url == register_site
        