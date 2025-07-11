from selenium.webdriver.common.by import By

# Панель ввода адреса
ADDRESS_FROM_FIELD_LOCATOR = (By.ID, "from")
ADDRESS_TO_FIELD_LOCATOR = (By.ID, "to")


# Панель с выбором маршрута
CHOOSE_ROUTE_PANEL_LOCATOR = (By.XPATH, ".//div[@class='type-picker shown']")
TABS_LIST_LOCATOR = (By.XPATH, ".//div[@class='modes-container']/div[contains(@class, 'mode')]")
ROUTE_DESCRIPTION_TEXT_LOCATOR = (By.CLASS_NAME, "text")
ROUTE_DURATION_TEXT_LOCATOR = (By.CLASS_NAME, "duration")
ACTIVE_TAB_LOCATOR = (By.XPATH, ".//div[@class='mode active']")
CHOOSE_ROUTE_PANEL_BUTTON_LOCATOR = (By.XPATH, ".//div[@class = 'results-container']//button")

# опции маршрута для тарифа "Свой"
SELF_OPTION_CAR_LOCATOR = (By.XPATH, ".//img[contains(@src, 'car.')]/..")
SELF_OPTION_WALK_LOCATOR = (By.XPATH, ".//img[contains(@src, 'walk')]/..")
SELF_OPTION_TAXI_LOCATOR = (By.XPATH, ".//img[contains(@src, 'taxi')]/..")
SELF_OPTION_BIKE_LOCATOR = (By.XPATH, ".//img[contains(@src, 'bike')]/..")
SELF_OPTION_SCOOTER_LOCATOR = (By.XPATH, ".//img[contains(@src, 'scooter')]/..")
SELF_OPTION_DRIVE_LOCATOR = (By.XPATH, ".//img[contains(@src, 'drive')]/..")


# Карта
# локатор для получения точек старта/финиша маршрута
ADDRESS_POINTS_LOCATOR = (By.XPATH, ".//ymaps[contains(@class, 'ymaps-2-1-79-route-pin__text')]/ymaps[@id]")
