import allure
import pytest
from selenium import webdriver
from data import BASE_URL, FIRST_ADDRESS, SECOND_ADDRESS
from pages.main_page import MainPage
from pages.get_taxi_panel import GetTaxiPanel
from pages.search_taxi_panel import SearchTaxiPanel
from pages.finish_order_taxi_panel import FinishOrderTaxiPanel

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

@allure.title("Открываем окно поиска такси (тариф Рабочий + столик для ноутбука)")
@pytest.fixture
def driver_open_search_taxi_panel(driver_open_choose_taxi_panel):
    page = GetTaxiPanel(driver_open_choose_taxi_panel)
    page.click_on_work_tariff()
    page.click_on_extra_wishes_title()
    page.scroll_down_extra_panel()
    page.click_on_extra_wishes_laptop_checkbox()
    page.click_on_extra_info_get_taxi_button()
    yield driver_open_choose_taxi_panel

@allure.title("Открываем окно завершения заказа, возвращаем драйвер и цену поездки")
@pytest.fixture
def driver_open_finish_order_taxi_panel(driver_open_choose_taxi_panel):
    get_taxi_panel = GetTaxiPanel(driver_open_choose_taxi_panel)
    get_taxi_panel.click_on_work_tariff()
    price = get_taxi_panel.get_taxi_order_price()
    get_taxi_panel.click_on_extra_info_get_taxi_button()
    search_taxi_panel = SearchTaxiPanel(driver_open_choose_taxi_panel)
    search_taxi_panel.wait_for_zero_timer()
    finish_order_taxi_panel = FinishOrderTaxiPanel(driver_open_choose_taxi_panel)
    finish_order_taxi_panel.is_driver_picture_visible()
    yield driver_open_choose_taxi_panel, price


