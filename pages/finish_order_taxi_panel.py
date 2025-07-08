from locators import finish_order_taxi_panel_locators as locators
from pages.base_page import BasePage
import allure


class FinishOrderTaxiPanel(BasePage):
    @allure.step("Получаем текст заголовка панели завершения заказа")
    def get_title_text(self):
        return self.get_text_from_element(locators.FINISH_ORDER_TAXI_TITLE_LOCATOR)

    @allure.step("Проверяем, что отображается картинка с машиной")
    def is_car_picture_visible(self):
        return self.is_element_visible(locators.FINISH_ORDER_TAXI_PICTURE_LOCATOR)

    @allure.step("Проверяем, что картинка с машиной не отображается")
    def is_car_picture_invisible(self):
        return self.is_element_invisible(locators.FINISH_ORDER_TAXI_PICTURE_LOCATOR)

    @allure.step("Проверяем, что отображается валидный номер машины")
    def is_car_number_valid(self):
        number_len = len(self.get_text_from_element(locators.FINISH_ORDER_TAXI_CAR_NUMBER_LOCATOR))
        if number_len == 8: # длина номера с учетом пробелов
            return True
        else:
            return False

    @allure.step("Проверяем, что отображается аватар водителя")
    def is_driver_picture_visible(self):
        return self.is_element_visible(locators.FINISH_ORDER_TAXI_CAR_DRIVER_PICTURE_LOCATOR)

    @allure.step("Проверяем, что отображается рейтинг водителя")
    def is_rating_visible(self):
        return self.is_element_visible(locators.FINISH_ORDER_TAXI_CAR_DRIVER_RATING_LOCATOR)

    @allure.step("Проверяем, что отображается имя водителя")
    def is_driver_name_visible_and_not_empty(self):
        is_visible = self.is_element_visible(locators.FINISH_ORDER_TAXI_CAR_DRIVER_NAME_LOCATOR)
        len_name = len(self.get_text_from_element(locators.FINISH_ORDER_TAXI_CAR_DRIVER_NAME_LOCATOR))
        if is_visible and len_name >= 1:
            return True
        else:
            return False

    @allure.step("Получаем текст кнопки Отменить")
    def get_return_button_text(self):
        return self.get_text_from_element(locators.FINISH_ORDER_RETURN_BUTTON_TEXT_LOCATOR)

    @allure.step("Получаем текст кнопки Детали")
    def get_details_button_text(self):
        return self.get_text_from_element(locators.FINISH_ORDER_DETAILS_BUTTON_TEXT_LOCATOR)

    @allure.step("Кликаем на кнопку Отменить")
    def click_on_return_button(self):
        self.click_on_element(locators.FINISH_ORDER_RETURN_BUTTON_LOCATOR)

    @allure.step("Кликаем на кнопку Детали")
    def click_on_details_button(self):
        self.click_on_element(locators.FINISH_ORDER_DETAILS_BUTTON_LOCATOR)

    @allure.step("Получаем текст 'Стоимость - Х рублей'")
    def get_text_details_order_price(self):
        return self.get_text_from_element(locators.FINISH_ORDER_TAXI_DETAILS_PRICE_LOCATOR)