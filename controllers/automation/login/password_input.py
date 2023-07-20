from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import logging

def _password_input(driver, password) -> None:
    password_input_x_path = '//*[@id="j_page_header"]/div[1]/div/div[1]/div[1]/div[2]/div[3]/div[1]/input'

    try:
        password_input_el = driver.find_element(By.XPATH, password_input_x_path)
    except NoSuchElementException:
        logging.critical("Element does not exist, may be due to using the wrong value for the selector")
        driver.quit()
    else:
        password_input_el.send_keys(password)
        print(type(password_input_el))