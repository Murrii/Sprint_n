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

@allure.title("Открываем главную страницу, вводим два адреса, выбираем опцию Велосипед")
@pytest.fixture
def driver_option_bike(driver_with_addresses):
    page = MainPage(driver_with_addresses)
    page.click_on_tab_self()
    page.click_on_bike_option()
    yield driver_with_addresses

@allure.title("Открываем окно выбора тарифа такси")
@pytest.fixture
def driver_open_choose_taxi_panel(driver_with_addresses):
    page = MainPage(driver_with_addresses)
    page.click_on_tab_fast()
    page.click_on_choose_route_panel_button()
    yield driver_with_addresses