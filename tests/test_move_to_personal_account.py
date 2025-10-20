import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.locators import Locators
from utils.urls import main_site, profile_site, login_site


class TestCheckPageProfile:
    def test_transition_to_profile(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        # Ждём появления "Булок"
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.inscription_bread))

        # Переходим в личный кабинет
        driver.find_element(*Locators.button_personal_area).click()

        # Ждём перехода на страницу профиля
        WebDriverWait(driver, 15).until(EC.url_to_be(profile_site))

        assert driver.current_url == profile_site


class TestTransitionByConstructor:
    def test_check_transition_by_constructor(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        # Переходим в личный кабинет
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(Locators.button_personal_area)
        ).click()

        # Ждём перехода на страницу профиля
        WebDriverWait(driver, 15).until(EC.url_to_be(profile_site))

        # Переходим в конструктор
        driver.find_element(*Locators.button_constructor).click()

        # Ждём главную страницу
        WebDriverWait(driver, 15).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site


class TestTransitionByLogo:
    def test_transition_by_logo(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        # Переходим в личный кабинет
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.button_personal_area)).click()

        # Ждём перехода на страницу профиля
        WebDriverWait(driver, 15).until(EC.url_to_be(profile_site))

        # Кликаем по логотипу
        driver.find_element(*Locators.logo).click()

        # Ждём перехода на главную страницу
        WebDriverWait(driver, 15).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site


class TestButtonCheckExit:
    def test_check_logging_out(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        # Переходим в личный кабинет
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(Locators.button_personal_area)
        ).click()

        # Ждём перехода на страницу профиля
        WebDriverWait(driver, 15).until(EC.url_to_be(profile_site))

        # Ждём загрузки профиля
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.inscription_profile))

        # Кликаем по кнопке "Выход"
        driver.find_element(*Locators.button_exit).click()

        # Ждём возврата на страницу логина
        WebDriverWait(driver, 15).until(EC.url_to_be(login_site))

        assert driver.current_url == login_site
        