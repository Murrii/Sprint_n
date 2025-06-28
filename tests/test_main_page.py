from pages.main_page import MainPage
from data import FIRST_ADDRESS, SECOND_ADDRESS
from data import DESCRIPTION_FOR_IDENTICAL_ADDRESSES, DURATION_FOR_IDENTICAL_ADDRESSES
from data import TEXT_FROM_TAB_OPTIMAL, TEXT_DESCRIPTION_FOR_OPTIMAL_ROUTE, TEXT_DURATION_FOR_OPTIMAL_ROUTE
from data import TEXT_FROM_TAB_FAST, TEXT_DESCRIPTION_FOR_FAST_ROUTE, TEXT_DURATION_FOR_FAST_ROUTE
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

    @allure.title("Переключение тарифа на Оптимальный")
    def test_click_on_tab_optimal_made_tab_active_and_recalculated_time_and_price(self, driver_with_addresses):
        page = MainPage(driver_with_addresses)
        page.click_on_tab_optimal()
        active_tab_text = page.get_text_from_active_tab()
        assert (active_tab_text == TEXT_FROM_TAB_OPTIMAL and
                page.get_text_from_route_description() == TEXT_DESCRIPTION_FOR_OPTIMAL_ROUTE and
                page.get_text_from_route_duration() == TEXT_DURATION_FOR_OPTIMAL_ROUTE)

    @allure.title("Переключение тарифа на Быстрый")
    def test_click_on_tab_fast_made_tab_active_and_recalculated_time_and_price(self, driver_with_addresses):
        page = MainPage(driver_with_addresses)
        page.click_on_tab_fast()
        assert (page.get_text_from_active_tab() == TEXT_FROM_TAB_FAST and
                page.get_text_from_route_description() == TEXT_DESCRIPTION_FOR_FAST_ROUTE and
                page.get_text_from_route_duration() == TEXT_DURATION_FOR_FAST_ROUTE)

