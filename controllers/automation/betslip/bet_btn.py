from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException

import logging

def accept_changes_btn(driver):
    try:
        bet_btn_el = driver.find_element(By.CSS_SELECTOR, "span[data-cms-key='accept_changes']")
    except TimeoutException:
        logging.critical("Could not find the element in time")
        place_bet_btn(driver=driver)
    except StaleElementReferenceException:
        logging.critical("State of element has changed.")
        place_bet_btn(driver=driver)
    except NoSuchElementException:
        logging.critical("Element does not exist, may be due to using the wrong value for the selector or page is not fully loaded so element is not available")
        place_bet_btn(driver=driver)
    else:
        bet_btn_el.click()
        print(type(bet_btn_el), bet_btn_el, "accept")

def place_bet_btn(driver):
    try:
        WebDriverWait(driver, timeout=10).until(presence_of_element_located((By.CSS_SELECTOR, "span[data-cms-key='place_bet']")))
        bet_btn_el = driver.find_element(By.CSS_SELECTOR, "span[data-cms-key='place_bet']")
    except TimeoutException:
        logging.critical("Could not find the element in time")
        accept_changes_btn(driver=driver)
    except StaleElementReferenceException:
        logging.critical("State of element has changed.")
        accept_changes_btn(driver=driver)
    except NoSuchElementException:
        logging.critical("Element does not exist, may be due to using the wrong value for the selector or page is not fully loaded so element is not available")
        accept_changes_btn(driver=driver)
    else:
        bet_btn_el.click()
        print(type(bet_btn_el), bet_btn_el, "place")