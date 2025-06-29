from selenium.webdriver.common.by import By


TAXI_TARIFFS_NAMES_LIST_LOCATOR = (By.XPATH, ".//div[@class='tcard-title']")
TAXI_TARIFFS_ACTIVE_TARIFF_NAME_LOCATOR = (By.XPATH, ".//div[@class='tcard active']/div[@class='tcard-title']")