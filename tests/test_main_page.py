import pytest
from pages.main_page import MainPage
from data import FIRST_ADDRESS, SECOND_ADDRESS
from data import DESCRIPTION_FOR_IDENTICAL_ADDRESSES, DURATION_FOR_IDENTICAL_ADDRESSES
from data import TEXT_FROM_TAB_OPTIMAL, TEXT_FROM_TAB_FAST, TEXT_FROM_TAB_SELF
from data import TEXT_GET_TAXI_BUTTON, TEXT_GET_DRIVE_BUTTON
import allure

class TestMainPage:
    @allure.title("Отрисовка маршрута: на карте отображаются точки начала и конца маршрута")
    def test_enter_start_and_finish_travel_points_shows_points_on_the_map(self, driver):
        page = MainPage(driver)
        page.fill_start_address_field(FIRST_ADDRESS)
        page.fill_end_address_field(SECOND_ADDRESS)
        points_list = page.get_list_of_travel_points()
        assert len(points_list) == 2

    @allure.title("При вводе точек начала и конца маршрута появляется панель выбора маршрута")
    def test_enter_start_and_finish_travel_points_shows_choose_route_panel(self, driver):
        page = MainPage(driver)
        page.fill_start_address_field(SECOND_ADDRESS)
        page.fill_end_address_field(FIRST_ADDRESS)
        assert page.is_choose_route_panel_visible()

    @allure.title("Ввод одинакового адреса в начало и конец маршрута")
    def test_enter_identical_addresses_shows_text_count_free_time_zero(self, driver):
        page = MainPage(driver)
        page.fill_start_address_field(FIRST_ADDRESS)
        page.fill_end_address_field(FIRST_ADDRESS)
        assert (page.get_text_from_route_description() == DESCRIPTION_FOR_IDENTICAL_ADDRESSES and
                page.get_text_from_route_duration() == DURATION_FOR_IDENTICAL_ADDRESSES)

    @pytest.mark.parametrize('active_page_method,active_tab_title', [(MainPage.click_on_tab_optimal, TEXT_FROM_TAB_OPTIMAL),
                                                                     (MainPage.click_on_tab_fast, TEXT_FROM_TAB_FAST)])
    @allure.title("Переключение тарифа на Оптимальный/Быстрый")
    @allure.description("При переключении происходит смена активного таба и пересчет времени и стоимости маршрута")
    def test_click_on_tab_optimal_made_tab_active_and_recalculated_time_and_price(self, driver_option_bike, active_page_method, active_tab_title):
        page = MainPage(driver_option_bike)
        # сохраняем тексты стоимости и длительности для текущего варианта (велосипед)
        old_duration = page.get_text_from_route_duration()
        old_description = page.get_text_from_route_description()
        # вызываем метод из параметризации для нашей страницы (открываем целевую вкладку)
        active_page_method(page)
        # тексты вкладки Оптимальный/Быстрый
        active_tab_text = page.get_text_from_active_tab()
        new_duration = page.get_text_from_route_duration()
        new_description = page.get_text_from_route_description()
        assert (active_tab_text == active_tab_title and
                old_description != new_description and
                old_duration != new_duration)

    @allure.title("Переключение тарифа на Свой")
    @allure.title("При переключении происходит смена активного таба "
                  "и становятся активны типы передвижения (Машина, Пешком, Такси, Велосипед, Самокат, Драйв)")
    def test_click_on_tab_self_made_tab_active_and_able_more_route_options(self, driver_with_addresses):
        page = MainPage(driver_with_addresses)
        page.click_on_tab_fast()
        page.click_on_tab_self()
        assert page.is_all_options_available()

    @allure.title("При выборе вида маршрута Быстрый отображается кнопка Вызвать такси")
    def test_click_on_tab_fast_show_get_taxi_button(self, driver_with_addresses):
        page = MainPage(driver_with_addresses)
        page.click_on_tab_fast()
        assert page.get_text_from_choose_route_panel_button() == TEXT_GET_TAXI_BUTTON

    @allure.title("При выборе вида маршрута Свой, типа передвижения Драйв отображается кнопка Забронировать")
    def test_click_on_tab_fast_show_get_taxi_button(self, driver_with_addresses):
        page = MainPage(driver_with_addresses)
        page.click_on_tab_self()
        page.click_on_drive_option()
        assert page.get_text_from_choose_route_panel_button() == TEXT_GET_DRIVE_BUTTON





