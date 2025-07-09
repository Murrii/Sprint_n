from pages.get_taxi_panel import GetTaxiPanel
from pages.search_taxi_panel import SearchTaxiPanel
from data import SEARCH_TAXI_TITLE_TEXT, SEARCH_TAXI_DETAILS_BUTTON_TEXT, SEARCH_TAXI_RETURN_BUTTON_TEXT
from data import FINISH_ORDER_TAXI_TITLE_TEXT
import allure


class TestSearchTaxiPanel:
    @allure.title("Нажатие на кнопку Заказать такси открывает окно ожидания машины")
    @allure.description("Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать")
    def test_click_on_extra_info_get_taxi_button_open_waiting_taxi_window(self, driver_open_choose_taxi_panel):
        get_taxi_panel = GetTaxiPanel(driver_open_choose_taxi_panel)
        get_taxi_panel.click_on_work_tariff()
        get_taxi_panel.click_on_extra_wishes_title()
        get_taxi_panel.scroll_down_extra_panel()
        get_taxi_panel.click_on_extra_wishes_laptop_checkbox()
        get_taxi_panel.click_on_extra_info_get_taxi_button()
        search_taxi_panel = SearchTaxiPanel(driver_open_choose_taxi_panel)
        assert search_taxi_panel.get_title_text() == SEARCH_TAXI_TITLE_TEXT

    @allure.title("Элементы окна ожидания машины соответствуют ТЗ")
    def test_search_taxi_panel_elements_visible_and_has_expected_texts(self, driver_open_search_taxi_panel):
        page = SearchTaxiPanel(driver_open_search_taxi_panel)
        assert (page.get_title_text() == SEARCH_TAXI_TITLE_TEXT and
                page.is_timer_visible() and
                page.get_return_button_text() == SEARCH_TAXI_RETURN_BUTTON_TEXT and
                page.get_details_button_text() == SEARCH_TAXI_DETAILS_BUTTON_TEXT)

    @allure.title("После окончания таймера отображается окно совершенного заказа")
    def test_timer_end_open_order_window(self, driver_open_search_taxi_panel):
        page = SearchTaxiPanel(driver_open_search_taxi_panel)
        page.wait_for_zero_timer()
        assert FINISH_ORDER_TAXI_TITLE_TEXT in page.get_title_text()
