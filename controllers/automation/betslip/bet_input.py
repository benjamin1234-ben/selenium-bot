from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys

import logging

def _bet_input(driver, wager) -> None:
    bet_input_x_path = '//*[@id="j_stake_0"]/div/div[3]/div/span/input'

    try:
        WebDriverWait(driver, timeout=10).until(presence_of_element_located((By.XPATH, bet_input_x_path)))
        bet_input_el = driver.find_element(By.XPATH, bet_input_x_path)
    except NoSuchElementException:
        logging.critical("Element does not exist, may be due to using the wrong value for the selector or page is not fully loaded so element is not available")
        driver.quit()
    except TimeoutException:
        logging.critical("Could not find the element in time")
        driver.quit()
    else:
        while bet_input_el.get_attribute("value") != "":
           bet_input_el.send_keys(Keys.BACK_SPACE)
        bet_input_el.send_keys(wager)
        print(type(bet_input_el), bet_input_el.get_attribute("value"))
        print(driver.find_element(By.ID, "j_balance").text)