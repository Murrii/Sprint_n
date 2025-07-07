from pages.base_page import BasePage
from locators import search_taxi_panel_locators
import allure


class SearchTaxiPanel(BasePage):
    @allure.step("Получаем заголовок окна поиска такси")
    def get_title(self):
        return self.get_text_from_element(search_taxi_panel_locators.SEARCH_TAXI_TITLE_LOCATOR)

    @allure.step("Получаем текст кнопки Отменить")
    def get_return_button_text(self):
        return self.get_text_from_element(search_taxi_panel_locators.SEARCH_TAXI_RETURN_BUTTON_TEXT_LOCATOR)

    @allure.step("Получаем текст кнопки Детали")
    def get_details_button_text(self):
        return self.get_text_from_element(search_taxi_panel_locators.SEARCH_TAXI_DETAILS_BUTTON_TEXT_LOCATOR)

    @allure.step("Кликаем на кнопку Отменить")
    def click_on_return_button(self):
        self.click_on_element(search_taxi_panel_locators.SEARCH_TAXI_RETURN_BUTTON_TEXT_LOCATOR)

    @allure.step("Кликаем на кнопку Детали")
    def click_on_details_button(self):
        self.click_on_element(search_taxi_panel_locators.SEARCH_TAXI_DETAILS_BUTTON_TEXT_LOCATOR)

    @allure.step("Проверяем, что отображается таймер")
    def is_timer_visible(self):
        try:
            self.find_element_with_wait_visibility(search_taxi_panel_locators.SEARCH_TAXI_TIMER_LOCATOR)
            return True
        except TimeoutError:
            return False

    @allure.step("ждем, пока таймер закончит отсчет")
    def wait_for_zero_timer(self):
        # с запасом в 1 секунду, чтобы функция успела отработать
        self.wait_text_is_visible(search_taxi_panel_locators.SEARCH_TAXI_TIMER_LOCATOR, "00:01")
        # ждем, пока пройдет еще 1 секунда
        self.wait_change_of_element(search_taxi_panel_locators.SEARCH_TAXI_TIMER_LOCATOR, "00:01")
