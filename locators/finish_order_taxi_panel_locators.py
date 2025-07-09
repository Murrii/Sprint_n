from selenium.webdriver.common.by import By


FINISH_ORDER_TAXI_TITLE_LOCATOR = (By.XPATH, ".//*[@class='order-header-title']")

FINISH_ORDER_TAXI_PICTURE_LOCATOR = (By.XPATH, ".//img[@alt='Car']")
FINISH_ORDER_TAXI_CAR_NUMBER_LOCATOR = (By.XPATH, ".//*[@class='number']")

FINISH_ORDER_TAXI_CAR_DRIVER_PICTURE_LOCATOR = (By.XPATH, ".//*[@class='order-btn-rating']/../img")
FINISH_ORDER_TAXI_CAR_DRIVER_RATING_LOCATOR = (By.XPATH, ".//*[@class='order-btn-rating']")
FINISH_ORDER_TAXI_CAR_DRIVER_NAME_LOCATOR = (By.XPATH, ".//*[@class='order-btn-rating']/../../div[2]")

FINISH_ORDER_RETURN_BUTTON_LOCATOR = (By.XPATH, ".//div[text()='Отменить']/../button")
FINISH_ORDER_RETURN_BUTTON_TEXT_LOCATOR = (By.XPATH, ".//div[text()='Отменить']")
FINISH_ORDER_DETAILS_BUTTON_LOCATOR = (By.XPATH, ".//div[text()='Детали']/../button")
FINISH_ORDER_DETAILS_BUTTON_TEXT_LOCATOR = (By.XPATH, ".//div[text()='Детали']")

FINISH_ORDER_TAXI_DETAILS_PRICE_LOCATOR = (By.XPATH, ".//*[text()='Стоимость - ']")