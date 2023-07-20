from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import logging

def _phone_input(driver, phone) -> None:
    phone_input_x_path = '//*[@id="j_page_header"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/input'

    try:
        WebDriverWait(driver, timeout=10).until(presence_of_element_located((By.XPATH, phone_input_x_path)))
        phone_input_el = driver.find_element(By.XPATH, phone_input_x_path)
    except TimeoutException:
        logging.critical("Could not find the element in time")
        driver.quit()
    except NoSuchElementException:
        logging.critical("Element does not exist, may be due to using the wrong value for the selector")
        driver.quit()
    else:
        phone_input_el.send_keys(phone)
        print(type(phone_input_el))