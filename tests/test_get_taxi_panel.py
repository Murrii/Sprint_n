import pytest
from pages.get_taxi_panel import GetTaxiPanel
from data import (TARIFFS_INFO_WORK_TEXTS, TARIFFS_INFO_SLEEP_TEXTS, TARIFFS_INFO_HOLIDAY_TEXTS,
                  TARIFFS_INFO_TALK_TEXTS, TARIFFS_INFO_GLAD_TEXTS, TARIFFS_INFO_GLAM_TEXTS)
from data import (EXTRA_INFO_PHONE_FIELD_TEXT, EXTRA_INFO_PAYMENT_INFO_TEXT, EXTRA_INFO_COMMENT_FIELD_TEXT,
                  EXTRA_INFO_EXTRA_WISHES_TEXT, EXTRA_INFO_GET_TAXI_BUTTON_TEXT)
import allure


class TestGetTaxiNamePage:
    @allure.title("Открывается форма заказа со всеми 6 тарифами по ТЗ")
    @allure.description("Проверяем, что в списке тарифов есть все необходимые тарифы и нет лишних тарифов")
    def test_actual_list_of_tariffs_identical_with_expected_tariffs_list(self, driver_open_choose_taxi_panel):
        page = GetTaxiPanel(driver_open_choose_taxi_panel)
        assert page.is_all_expected_tariffs_in_tariffs_names_list() and page.is_all_visible_tariffs_is_expected()

    @allure.title("В списке тарифов по умолчанию один тариф - активный")
    def test_tariffs_list_include_active_tariff(self, driver_open_choose_taxi_panel):
        page = GetTaxiPanel(driver_open_choose_taxi_panel)
        assert page.is_active_tariff_in_tariff_names_list()

    @allure.title("При наведении на i отображается подсказка с информацией о тарифе")
    def test_focus_on_info_button_shows_info_panel(self, driver_open_choose_taxi_panel):
        page = GetTaxiPanel(driver_open_choose_taxi_panel)
        page.focus_on_info_icon()
        assert page.is_info_panel_visible()

    @allure.title("Проверка текстов карточки инфо на соответствие ТЗ для всех тарифов (параметризация)")
    @pytest.mark.xfail(reason="описания для тарифов Сонный и Разговорчивый перепутаны местами")
    @pytest.mark.parametrize('click_on_tariff_method, result_texts_dict', [(GetTaxiPanel.click_on_work_tariff, TARIFFS_INFO_WORK_TEXTS),
                                                                           (GetTaxiPanel.click_on_sleep_tariff, TARIFFS_INFO_SLEEP_TEXTS),
                                                                           (GetTaxiPanel.click_on_holiday_tariff, TARIFFS_INFO_HOLIDAY_TEXTS),
                                                                           (GetTaxiPanel.click_on_talk_tariff, TARIFFS_INFO_TALK_TEXTS),
                                                                           (GetTaxiPanel.click_on_glad_tariff, TARIFFS_INFO_GLAD_TEXTS),
                                                                           (GetTaxiPanel.click_on_glam_tariff, TARIFFS_INFO_GLAM_TEXTS)])
    def test_info_panel_title_and_description_match_with_expected_texts(self, driver_open_choose_taxi_panel,
                                                                        click_on_tariff_method, result_texts_dict):
        page = GetTaxiPanel(driver_open_choose_taxi_panel)
        click_on_tariff_method(page)
        page.focus_on_info_icon()
        actual_title = page.get_info_panel_title()
        actual_description = page.get_info_panel_description()
        assert actual_title == result_texts_dict['title'] and actual_description == result_texts_dict['description']

    @allure.title("Проверяем, состав блока доп. информации к заказу")
    @allure.description("Проверяем, что все поля присутствуют ч что заголовки соответствуют ТЗ")
    def test_extra_info_panel_include_phone_payment_comment_and_extra_wishes_fields(self, driver_open_choose_taxi_panel):
        page = GetTaxiPanel(driver_open_choose_taxi_panel)
        assert (page.get_text_from_extra_info_phone_field() == EXTRA_INFO_PHONE_FIELD_TEXT and
                page.get_text_from_extra_info_payment_field() == EXTRA_INFO_PAYMENT_INFO_TEXT and
                page.get_text_from_extra_info_comment_field() == EXTRA_INFO_COMMENT_FIELD_TEXT and
                page.get_text_from_extra_info_extra_wishes_field() == EXTRA_INFO_EXTRA_WISHES_TEXT and
                page.get_text_from_extra_info_get_taxi_button() == EXTRA_INFO_GET_TAXI_BUTTON_TEXT)

