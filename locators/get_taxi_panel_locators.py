from selenium.webdriver.common.by import By

# Локатор для получения списка тарифов
TAXI_TARIFFS_NAMES_LIST_LOCATOR = (By.XPATH, ".//div[@class='tcard-title']")

# Локаторы для работы с активным тарифом (Имя, иконка инфо, тексты панели инфо)
TAXI_TARIFFS_ACTIVE_TARIFF_NAME_LOCATOR = (By.XPATH, ".//div[@class='tcard active']/div[@class='tcard-title']")
TAXI_TARIFFS_ACTIVE_INFO_BUTTON_LOCATOR = (By.XPATH, ".//div[@class='tcard active']/button[@class = 'i-button tcard-i active']")
TAXI_TARIFFS_ACTIVE_INFO_TITLE_TEXT_LOCATOR = (By.XPATH, ".//div[@class='tcard active']//div[@class = 'i-title']")
TAXI_TARIFFS_ACTIVE_INFO_DESCRIPTION_LOCATOR = (By.XPATH, ".//div[@class='tcard active']//div[@class = 'i-dPrefix']")

# Локаторы для выбора тарифа
TAXI_TARIFFS_TARIFF_WORK_LOCATOR = (By.XPATH, ".//div[@class='tariff-cards']/div/div[text()='Рабочий']")
TAXI_TARIFFS_TARIFF_SLEEP_LOCATOR = (By.XPATH, ".//div[@class='tariff-cards']/div/div[text()='Сонный']")
TAXI_TARIFFS_TARIFF_HOLIDAY_LOCATOR = (By.XPATH, ".//div[@class='tariff-cards']/div/div[text()='Отпускной']")
TAXI_TARIFFS_TARIFF_TALK_LOCATOR = (By.XPATH, ".//div[@class='tariff-cards']/div/div[text()='Разговорчивый']")
TAXI_TARIFFS_TARIFF_GLAD_LOCATOR = (By.XPATH, ".//div[@class='tariff-cards']/div/div[text()='Утешительный']")
TAXI_TARIFFS_TARIFF_GLAM_LOCATOR = (By.XPATH, ".//div[@class='tariff-cards']/div/div[text()='Глянцевый']")

# локаторы для полей с доп информацией

EXTRA_INFO_PHONE_FIELD_TEXT_LOCATOR = (By.CLASS_NAME, "np-text")
EXTRA_INFO_PAYMENT_INFO_TEXT_LOCATOR = (By.CLASS_NAME, "pp-text")
EXTRA_INFO_COMMENT_FIELD_TEXT_LOCATOR = (By.XPATH, ".//input[@id='comment']/../label")
EXTRA_INFO_EXTRA_WISHES_TEXT_LOCATOR = (By.CLASS_NAME, 'reqs-head')
EXTRA_INFO_GET_TAXI_BUTTON_TEXT_LOCATOR = (By.CLASS_NAME, "smart-button-main")
EXTRA_INFO_EXTRA_WISHES_CUT_LOCATOR = (By.CLASS_NAME, 'reqs-arrow')
EXTRA_INFO_LAPTOP_CHECKBOX_LOCATOR = (By.XPATH, ".//*[@class='slider round']")
EXTRA_INFO_PANEL_LOCATOR = (By.XPATH, ".//*[@class='tariff-picker shown']")