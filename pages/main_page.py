from pages.base_page import BasePage
from locators import main_page_locators
import  allure


class MainPage(BasePage):
    @allure.step("Заполняем адрес начала маршрута")
    def fill_start_address_field(self, address):
        self.fill_text_to_field(main_page_locators.ADDRESS_FROM_FIELD_LOCATOR, address)

    @allure.step("Заполняем адрес конца маршрута")
    def fill_end_address_field(self, address):
        self.fill_text_to_field(main_page_locators.ADDRESS_TO_FIELD_LOCATOR, address)

    @allure.step("Получаем список точек маршрута на карте")
    def get_list_of_travel_points(self):
        points = self.get_list_of_elements(main_page_locators.ADDRESS_POINTS_LOCATOR)
        return points

    @allure.step("Получаем список вкладок с вариантами маршрутов")
    def get_list_of_routes_tabs(self):
        tabs = self.get_list_of_elements(main_page_locators.TABS_LIST_LOCATOR)
        return tabs

    @allure.step("Нажимаем на вкладку 'Оптимальный'")
    def click_on_tab_optimal(self):
        tab = self.get_list_of_routes_tabs()[0]
        self.click_on_element_without_locator(tab)

    @allure.step("Получаем текст вкладки 'Оптимальный'")
    def get_text_from_tab_optimal(self):
        tab = self.get_list_of_routes_tabs()[0]
        return self.get_text_from_element_without_locator(tab)

    @allure.step("Нажимаем на вкладку 'Быстрый'")
    def click_on_tab_fast(self):
        tab = self.get_list_of_routes_tabs()[1]
        self.click_on_element_without_locator(tab)

    @allure.step("Получаем текст вкладки 'Быстрый'")
    def get_text_from_tab_fast(self):
        tab = self.get_list_of_routes_tabs()[1]
        return self.get_text_from_element_without_locator(tab)

    @allure.step("Нажимаем на вкладку 'Свой'")
    def click_on_tab_self(self):
        tab = self.get_list_of_routes_tabs()[2]
        self.click_on_element_without_locator(tab)

    @allure.step("Получаем текст вкладки 'Свой'")
    def get_text_from_tab_self(self):
        tab = self.get_list_of_routes_tabs()[2]
        return self.get_text_from_element_without_locator(tab)

    @allure.step("Проверяем видимость панели выбора маршрута")
    def is_choose_route_panel_visible(self):
        return self.is_element_visible(main_page_locators.CHOOSE_ROUTE_PANEL_LOCATOR)

    @allure.step("Получаем текст со стоимостью поездки")
    def get_text_from_route_description(self):
        return self.get_text_from_element(main_page_locators.ROUTE_DESCRIPTION_TEXT_LOCATOR)

    @allure.step("Получаем текст со длительностью поездки")
    def get_text_from_route_duration(self):
        return self.get_text_from_element(main_page_locators.ROUTE_DURATION_TEXT_LOCATOR)

    @allure.step("Получаем текст активной вкладки панели выбора маршрута")
    def get_text_from_active_tab(self):
        self.find_element_with_wait_visibility(main_page_locators.ACTIVE_TAB_LOCATOR)
        return self.get_text_from_element(main_page_locators.ACTIVE_TAB_LOCATOR)