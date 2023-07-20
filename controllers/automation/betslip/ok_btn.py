from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import logging

def _ok_btn(driver) -> None:
    try:
        WebDriverWait(driver, timeout=20).until(presence_of_element_located((By.CSS_SELECTOR, "span[data-cms-key='ok']")))
        ok_btn_el = driver.find_element(By.CSS_SELECTOR, "span[data-cms-key='ok']")
    except TimeoutException:
        logging.critical("Could not find the element in time")
        driver.quit()
    except NoSuchElementException:
        logging.critical("Element does not exist, may be due to using the wrong value for the selector or page is not fully loaded so element is not available")
        driver.quit()
    else:
        ok_btn_el.click()
        print(type(ok_btn_el), "Ok")