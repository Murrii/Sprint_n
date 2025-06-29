from pages.get_taxi_panel import GetTaxiPanel
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