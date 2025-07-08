import allure
import pytest

from pages.finish_order_taxi_panel import FinishOrderTaxiPanel
from data import FINISH_ORDER_TAXI_TITLE_TEXT, FINISH_ORDER_TAXI_DETAILS_BUTTON_TEXT, FINISH_ORDER_TAXI_RETURN_BUTTON_TEXT

class TestFinishOrderTaxiPanel:
    @allure.title("Элементы окна завершения заказа соответствуют ТЗ")
    def test_finish_order_taxi_panel_elements_visible_and_has_expected_texts(self, driver_open_finish_order_taxi_panel):
        finish_panel_driver, _ = driver_open_finish_order_taxi_panel
        page = FinishOrderTaxiPanel(finish_panel_driver)
        assert (FINISH_ORDER_TAXI_TITLE_TEXT in page.get_title_text() and
                page.is_car_picture_visible and page.is_car_number_valid() and
                page.is_driver_picture_visible() and page.is_rating_visible() and page.is_driver_name_visible_and_not_empty() and
                page.get_details_button_text() == FINISH_ORDER_TAXI_DETAILS_BUTTON_TEXT and
                page.get_return_button_text() == FINISH_ORDER_TAXI_RETURN_BUTTON_TEXT)

    @allure.title("При нажатии на кнопку Детали открывается окно с деталями заказа")
    def test_click_details_button_open_details_panel(self, driver_open_finish_order_taxi_panel):
        finish_panel_driver, price = driver_open_finish_order_taxi_panel
        page = FinishOrderTaxiPanel(finish_panel_driver)
        page.click_on_details_button()
        text_with_price = page.get_text_details_order_price()
        assert price in text_with_price, print(price, text_with_price)

    @pytest.mark.xfail(reason="Кнопка Отменить не работает, заведен баг")
    @allure.title("При нажатии на кнопку Отмена окно завершения заказа закрывается")
    def test_click_return_button_open_closed_finish_order_panel(self, driver_open_finish_order_taxi_panel):
        finish_panel_driver, _ = driver_open_finish_order_taxi_panel
        page = FinishOrderTaxiPanel(finish_panel_driver)
        page.click_on_return_button()
        assert page.is_car_picture_invisible()
