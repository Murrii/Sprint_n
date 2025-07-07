from locators import get_taxi_panel_locators
from pages.base_page import BasePage
from data import EXPECTED_TARIFFS_TAXI_LIST
import allure


class GetTaxiPanel(BasePage):
    @allure.step("Получаем имя активного тарифа")
    def get_active_tariff_name(self):
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

    @allure.step("Нажимаем на тариф Рабочий")
    def click_on_work_tariff(self):
        self.click_on_element(get_taxi_panel_locators.TAXI_TARIFFS_TARIFF_WORK_LOCATOR)

    @allure.step("Нажимаем на тариф Сонный")
    def click_on_sleep_tariff(self):
        self.click_on_element(get_taxi_panel_locators.TAXI_TARIFFS_TARIFF_SLEEP_LOCATOR)

    @allure.step("Нажимаем на тариф Отпускной")
    def click_on_holiday_tariff(self):
        self.click_on_element(get_taxi_panel_locators.TAXI_TARIFFS_TARIFF_HOLIDAY_LOCATOR)

    @allure.step("Нажимаем на тариф Разговорчивый")
    def click_on_talk_tariff(self):
        self.click_on_element(get_taxi_panel_locators.TAXI_TARIFFS_TARIFF_TALK_LOCATOR)

    @allure.step("Нажимаем на тариф Утешительный")
    def click_on_glad_tariff(self):
        self.click_on_element(get_taxi_panel_locators.TAXI_TARIFFS_TARIFF_GLAD_LOCATOR)

    @allure.step("Нажимаем на тариф Глянцевый")
    def click_on_glam_tariff(self):
        self.click_on_element(get_taxi_panel_locators.TAXI_TARIFFS_TARIFF_GLAM_LOCATOR)

    @allure.step("Наводим курсор на иконку i для активной вкладки и удерживаем его 5 секунд")
    def focus_on_info_icon(self):
        self.focus_on_element(get_taxi_panel_locators.TAXI_TARIFFS_ACTIVE_INFO_BUTTON_LOCATOR)


    @allure.step("Проверяем, что отображается окно с подсказкой")
    def is_info_panel_visible(self):
        return self.is_element_visible(get_taxi_panel_locators.TAXI_TARIFFS_ACTIVE_INFO_DESCRIPTION_LOCATOR)

    @allure.step("Получаем заголовок окна с подсказкой")
    def get_info_panel_title(self):
        return self.get_text_from_element(get_taxi_panel_locators.TAXI_TARIFFS_ACTIVE_INFO_TITLE_TEXT_LOCATOR)

    @allure.step("Получаем описание окна с подсказкой")
    def get_info_panel_description(self):
        return self.get_text_from_element(get_taxi_panel_locators.TAXI_TARIFFS_ACTIVE_INFO_DESCRIPTION_LOCATOR)

    @allure.step("Получаем текст поля Телефон")
    def get_text_from_extra_info_phone_field(self):
        return self.get_text_from_element(get_taxi_panel_locators.EXTRA_INFO_PHONE_FIELD_TEXT_LOCATOR)

    @allure.step("Получаем текст поля Способ оплаты")
    def get_text_from_extra_info_payment_field(self):
        return self.get_text_from_element(get_taxi_panel_locators.EXTRA_INFO_PAYMENT_INFO_TEXT_LOCATOR)

    @allure.step("Получаем текст поля Комментарий водителю")
    def get_text_from_extra_info_comment_field(self):
        return self.get_text_from_element(get_taxi_panel_locators.EXTRA_INFO_COMMENT_FIELD_TEXT_LOCATOR)

    @allure.step("Получаем заголовок блока Требования к заказу")
    def get_text_from_extra_info_extra_wishes_field(self):
        return self.get_text_from_element(get_taxi_panel_locators.EXTRA_INFO_EXTRA_WISHES_TEXT_LOCATOR)

    @allure.step("Получаем текст кнопки Заказать такси")
    def get_text_from_extra_info_get_taxi_button(self):
        return self.get_text_from_element(get_taxi_panel_locators.EXTRA_INFO_GET_TAXI_BUTTON_TEXT_LOCATOR)

    @allure.step("Раскрываем блок с требованиями к заказу и прокручиваем вниз")
    def click_on_extra_wishes_title(self):
        self.click_on_element(get_taxi_panel_locators.EXTRA_INFO_EXTRA_WISHES_CUT_LOCATOR)

    @allure.step("Прокручиваем вниз панель с доп. опциями")
    def scroll_down_extra_panel(self):
        extra_info_panel = self.find_element_with_wait_clickable(get_taxi_panel_locators.EXTRA_INFO_PANEL_LOCATOR)
        self.move_to_down_in_container(extra_info_panel)

    @allure.step("Нажимаем на чекбокс Столик для ноутбука")
    def click_on_extra_wishes_laptop_checkbox(self):
        self.find_element_with_wait_clickable(get_taxi_panel_locators.EXTRA_INFO_LAPTOP_CHECKBOX_LOCATOR)
        self.click_on_element(get_taxi_panel_locators.EXTRA_INFO_LAPTOP_CHECKBOX_LOCATOR)

    @allure.step("Нажимаем на кнопку Заказать такси")
    def click_on_extra_info_get_taxi_button(self):
        self.click_on_element(get_taxi_panel_locators.EXTRA_INFO_GET_TAXI_BUTTON_TEXT_LOCATOR)


