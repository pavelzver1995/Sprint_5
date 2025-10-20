import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import Locators
from utils.data import Credential
from utils.urls import login_site, main_site

class TestButtonCheckExit:

    def test_check_loging_out(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        # Ждем загрузки "булок"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_bread))

        # Кликаем по кнопке "личный кабинет"
        driver.find_element(*Locators.button_personal_area).click()

        # Ждем загрузки надписи "профиль"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_profile))

        # Кликаем по кнопке "выход"
        driver.find_element(*Locators.button_exit).click()

        # Ждём перехода на страницу логина
        WebDriverWait(driver, 10).until(EC.url_to_be(login_site))
                                                                         
        #Проверяем URL
        assert driver.current_url == login_site


class TestBigMainButton:

    def test_check_entrance_by_big_button(self, start_from_site_not_login):
        driver = start_from_site_not_login
        driver.maximize_window()

        # Ждем и кликаем кнопку "Войти в аккаунт" с перепоиском
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.entrance_on_the_main)
        )
        button.click()

        # Ищем поля и проходим авторизацию
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.field_email))
        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver.find_element(*Locators.field_password).send_keys(Credential.password)
        
        # Кликаем на кнопку "Войти"
        driver.find_element(*Locators.button_entrance).click()

        # Ждем перехода на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        # Проверяем что мы на основной странице сайта
        assert driver.current_url == main_site


class TestCheckRegister:

    def test_login_password_recovery(self, start_from_recovery_page):
        driver = start_from_recovery_page
        driver.maximize_window()

        # Ждем загрузки "булок"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_bread))

        # Проверяем что мы на основной странице сайта
        assert driver.current_url == main_site

class TestCheckEntranceFromRecoveryPage:

    def test_button_inscription_login(self, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()

        # Жмем кнопку "зарегистрироваться"
        driver.find_element(*Locators.inscription_login).click()

        # Жмем кнопку "войти"
        driver.find_element(*Locators.inscription_button_entrance).click()

        # Ищем поля и проходим авторизацию
        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver.find_element(*Locators.field_password).send_keys(Credential.password)
        driver.find_element(*Locators.button_entrance).click()

        # Ждем перехода на главную
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        # Проверяем что мы на основной странице сайта
        assert driver.current_url == main_site
        