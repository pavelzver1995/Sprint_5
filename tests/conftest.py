import pytest
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from utils.locators import Locators
from utils.data import Credential
from utils.generator import EmailPasswordGenerator
from utils.urls import login_site, main_site, profile_site, register_site


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def start_from_login_page(driver):
    login_page = login_site
    driver.get(login_page)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.field_email))

    driver.find_element(*Locators.field_email).send_keys(Credential.email)
    driver.find_element(*Locators.field_password).send_keys(Credential.password)
    driver.find_element(*Locators.button_entrance).click()

    # Улучшенное ожидание - проверяем несколько условий
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))
    except TimeoutException:
        # Если не перешли по URL, проверяем наличие элемента на главной
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_bread))
    
    return driver


@pytest.fixture
def start_from_recovery_page(driver):
    page_login = login_site
    driver.get(page_login)

    # Кнопка восстановить пароль
    driver.find_element(*Locators.button_restore_password).click()

    # Ожидание загрузки
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.inscription_button_entrance))
                                                                    
    # Кнопка Войти
    driver.find_element(*Locators.inscription_button_entrance).click()

    # Поиск полей и авторизация
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.field_email))
    driver.find_element(*Locators.field_email).send_keys(Credential.email)
    driver.find_element(*Locators.field_password).send_keys(Credential.password)
    driver.find_element(*Locators.button_entrance).click()

    # Ожидание перехода на главную страницу
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))
    except TimeoutException:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_bread))

    return driver


@pytest.fixture
def start_from_main_page(driver):
    main_page = main_site
    driver.get(main_page)

    # Кнопка личный кабинет
    driver.find_element(*Locators.button_personal_area).click()

    # Кнопка Войти
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.button_entrance))
    driver.find_element(*Locators.button_entrance).click()
                                                                    
    # Поиск полей и авторизация
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.field_email))
    driver.find_element(*Locators.field_email).send_keys(Credential.email)
    driver.find_element(*Locators.field_password).send_keys(Credential.password)
    driver.find_element(*Locators.button_entrance).click()

    # Ожидание перехода на главную страницу
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))
    except TimeoutException:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_bread))

    return driver


@pytest.fixture
def start_from_register_page(driver):
    register_page = register_site
    driver.get(register_page)

    # Кнопка Войти
    driver.find_element(*Locators.inscription_button_entrance).click()
                                                                    
    # Поиск полей и авторизация
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.field_email))
    driver.find_element(*Locators.field_email).send_keys(Credential.email)
    driver.find_element(*Locators.field_password).send_keys(Credential.password)
    driver.find_element(*Locators.button_entrance).click()

    # Ожидание перехода на главную страницу
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))
    except TimeoutException:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_bread))

    return driver


@pytest.fixture
def start_from_main_not_login(driver):
    login_page = login_site
    driver.get(login_page)
    return driver


@pytest.fixture
def start_from_site_not_login(driver):
    main_page = main_site
    driver.get(main_page)
    return driver


@pytest.fixture
def register_new_account(driver):
    register_page = register_site
    driver.get(register_page)

    # Генерация email и password
    generator = EmailPasswordGenerator()
    email, password = generator.generate()

    # Заполнение полей на странице регистрации
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.field_name_register))
    driver.find_element(*Locators.field_name_register).send_keys("ТестовыйПользователь")
    driver.find_element(*Locators.field_email_register).send_keys(email)
    driver.find_element(*Locators.field_password_register).send_keys(password)

    # Клик по кнопке Зарегистрироваться
    driver.find_element(*Locators.button_register).click()

    # Ожидание перехода на страницу логина
    WebDriverWait(driver, 10).until(EC.url_to_be(login_site))
    
    return driver, email, password
