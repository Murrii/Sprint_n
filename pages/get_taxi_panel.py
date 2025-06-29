from locators import get_taxi_panel_locators
from pages.base_page import BasePage
from data import EXPECTED_TARIFFS_TAXI_LIST
import allure


class GetTaxiPanel(BasePage):
    @allure.step("Получаем имя активного тарифа")
    def get_active_tariff_name(self):
        self.find_element_with_wait_visibility(get_taxi_panel_locators.TAXI_TARIFFS_ACTIVE_TARIFF_NAME_LOCATOR)
        return self.get_text_from_element(get_taxi_panel_locators.TAXI_TARIFFS_ACTIVE_TARIFF_NAME_LOCATOR)

    @allure.step("Получаем список всех отображающихся тарифов")
    def get_tariff_names_list(self):
        tariffs_list = self.get_list_of_elements(get_taxi_panel_locators.TAXI_TARIFFS_NAMES_LIST_LOCATOR)
        tariffs_names_list = []
        for tariff in tariffs_list:
            tariffs_names_list.append(self.get_text_from_element_without_locator(tariff))
        return tariffs_names_list

    @allure.step("Проверяем, все ли ожидаемые тарифы отображаются в списке тарифов")
    def is_all_expected_tariffs_in_tariffs_names_list(self):
        actual_tariff_list = self.get_tariff_names_list()
        for tariff in EXPECTED_TARIFFS_TAXI_LIST:
            if tariff in actual_tariff_list:
                continue
            else:
                return False
        return True

    @allure.step("Проверяем, все ли отображающиеся тарифы есть в ТЗ")
    def is_all_visible_tariffs_is_expected(self):
        actual_tariff_list = self.get_tariff_names_list()
        for tariff in actual_tariff_list:
            if tariff in EXPECTED_TARIFFS_TAXI_LIST:
                continue
            else:
                return False
        return True

    @allure.step("Проверяем, что в списке тарифов есть активный тариф")
    def is_active_tariff_in_tariff_names_list(self):
        active_tariff = self.get_active_tariff_name()
        all_tariffs = self.get_tariff_names_list()
        if active_tariff in all_tariffs:
            return True
        else:
            return False