from selenium.webdriver.common.by import By


class Locators:

    # ЛОКАТОРЫ ДЛЯ СТРАНИЦЫ РЕГИСТРАЦИИ
    field_name_register = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    field_email_register = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    field_password_register = (By.XPATH, "//input[@type='password']")
    button_register = (By.XPATH, "//button[text()='Зарегистрироваться']")
    
    # ЛОКАТОРЫ ДЛЯ СТРАНИЦЫ ЛОГИНА
    button_entrance = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Войти']")
    
    # ЛОКАТОРЫ ДЛЯ ГЛАВНОЙ СТРАНИЦЫ
    entrance_on_the_main = (By.XPATH, "//button[text()='Войти в аккаунт']")
    button_arrange_order = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    button_personal_area = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    inscription_bread = (By.XPATH, "//span[contains(text(), 'Булки')]")
    inscription_sauce = (By.XPATH, "//span[contains(text(), 'Соусы')]")
    inscription_fillings = (By.XPATH, "//span[contains(text(), 'Начинки')]")
    
    # ЛОКАТОРЫ ДЛЯ ЛИЧНОГО КАБИНЕТА
    button_exit = (By.XPATH, "//button[contains(text(), 'Выход')]")
    inscription_profile = (By.XPATH, "//a[contains(text(), 'Профиль')]")
    button_constructor = (By.XPATH, "//p[text()='Конструктор']")
    logo = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    
    # ЛОКАТОРЫ ДЛЯ СТРАНИЦЫ ВОССТАНОВЛЕНИЯ ПАРОЛЯ
    button_restore_password = (By.XPATH, "//a[text()='Восстановить пароль']")
    inscription_button_entrance = (By.XPATH, "//a[text()='Войти']")
    
    # УНИВЕРСАЛЬНЫЕ ЛОКАТОРЫ
    field_name = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    field_email = (By.XPATH, "//input[@type='text']")
    field_password = (By.XPATH, "//input[@type='password']")
    button_login = (By.XPATH, "//button[text()='Зарегистрироваться']")
    inscription_login = (By.XPATH, "//a[text()='Зарегистрироваться']")
    
    # ЛОКАТОРЫ ДЛЯ ПРОВЕРКИ СОСТОЯНИЯ И ОШИБОК
    active_section = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
    inscription_error_account = (By.XPATH, "//p[contains(text(), 'Такой пользователь уже существует')]")
    inscription_error_password = (By.XPATH, "//div[contains(@class, 'input_status_error')]")
    