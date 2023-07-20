from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import logging

def _check_funds(driver) -> None:
    balance_x_path = '//*[@id="j_balance"]'

    try:
        WebDriverWait(driver, timeout=10).until(presence_of_element_located((By.XPATH, balance_x_path)))
        balance_el = driver.find_element(By.XPATH, balance_x_path)
    except TimeoutException:
        logging.critical("Could not find the element in time")
        driver.quit()
        return False
    except NoSuchElementException:
        logging.critical("Element does not exist, may be due to using the wrong value for the selector or page is not fully loaded so element is not available")
        driver.quit()
        return False
    else:
        print(type(balance_el), balance_el.text)
        return True