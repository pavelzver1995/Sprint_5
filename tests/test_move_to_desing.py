import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.locators import Locators

class TestCheckChapterBread:

    def test_check_chapter_bread(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        # Нажали на раздел начинки "Соусы"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_sauce)).click()

        # Нажали на раздел "Булки"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_bread)).click()

        # Проверяем наличие активного раздела
        new_element = WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located(Locators.active_section))
        assert new_element.is_displayed()

        # Проверяем, что активная вкладка соответствует разделу "Булки"
        active_tab = WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(Locators.inscription_bread))
        assert "Булки" in active_tab.text

class TestCheckChapterFillings:

    def test_check_chapter_fillings(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        # Жмем на раздел "Начинки"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_fillings)).click()

        # Проверяем наличие активного раздела
        new_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.active_section))
        assert new_element.is_displayed()

        # Проверяем, что активная вкладка соответствует разделу "Начинки"
        active_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_fillings))
        assert "Начинки" in active_tab.text


class TestCheckChapterSauce:

    def test_check_chapter_sauce(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        # Жмем на раздел "Соусы"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_sauce)).click()

        # Проверяем наличие активного раздела
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.active_section))

        # Проверяем, что активная вкладка соответствует разделу "Соусы"
        active_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_sauce))
        assert "Соусы" in active_tab.text
        