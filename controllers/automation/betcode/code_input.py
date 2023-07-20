from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import logging

def _code_input(driver, code) -> None:
    code_input_x_path = '//*[@id="j_betslip"]/div[2]/div[3]/div[1]/div[2]/span/input'

    try:
        WebDriverWait(driver, timeout=10).until(presence_of_element_located((By.XPATH, code_input_x_path)))
        code_input_el = driver.find_element(By.XPATH, code_input_x_path)
    except TimeoutException:
        logging.critical("Could not find the element in time")
        driver.quit()
    except NoSuchElementException:
        logging.critical("Element does not exist, may be due to using the wrong value for the selector or page is not fully loaded so element is not available")
        driver.quit()
    else:
        code_input_el.send_keys(code)
        print(type(code_input_el), code)