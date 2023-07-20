from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException

import logging

def _tab_btn(driver) -> None:
    tab_btn_x_path = "//*[@id='j_betslip']/div[2]/div[2]/div/div/div[2]/span"

    try:
        WebDriverWait(driver, timeout=10).until(element_to_be_clickable((By.XPATH, tab_btn_x_path)))
        tab_btn_el = driver.find_element(By.XPATH, tab_btn_x_path)
    except TimeoutException:
       logging.critical("Could not find the element in time")
       driver.quit()
    except NoSuchElementException:
        logging.critical("Element does not exist, may be due to using the wrong value for the selector or page is not fully loaded so element is not available")
        driver.quit()
    except ElementClickInterceptedException:
        logging.critical("Element is not clickable")
        driver.quit()
    else:
        tab_btn_el.click()
        print(type(tab_btn_el), tab_btn_el)