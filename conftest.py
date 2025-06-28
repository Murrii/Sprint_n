import allure
import pytest
from selenium import webdriver
from data import BASE_URL, FIRST_ADDRESS, SECOND_ADDRESS
from pages.main_page import MainPage

@allure.title("Открываем главную страницу")
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@allure.title("Открываем главную страницу и вводим два адреса")
@pytest.fixture
def driver_with_addresses(driver):
    page = MainPage(driver)
    page.fill_start_address_field(FIRST_ADDRESS)
    page.fill_end_address_field(SECOND_ADDRESS)
    yield driver
    driver.quit()