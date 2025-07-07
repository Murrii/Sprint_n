from selenium.webdriver.common.by import By


SEARCH_TAXI_TITLE_LOCATOR = (By.XPATH, ".//*[@class='order-header-title']")
SEARCH_TAXI_TIMER_LOCATOR = (By.XPATH, ".//*[@class='order-header-time']")
SEARCH_TAXI_RETURN_BUTTON_LOCATOR = (By.XPATH, ".//div[text()='Отменить']/../button")
SEARCH_TAXI_RETURN_BUTTON_TEXT_LOCATOR = (By.XPATH, ".//div[text()='Отменить']")
SEARCH_TAXI_DETAILS_BUTTON_LOCATOR = (By.XPATH, ".//div[text()='Детали']/../button")
SEARCH_TAXI_DETAILS_BUTTON_TEXT_LOCATOR = (By.XPATH, ".//div[text()='Детали']")