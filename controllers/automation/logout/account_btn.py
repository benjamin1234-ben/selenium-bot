from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import logging

def _account_btn(driver) -> None:
    account_btn_x_path = '//*[@id="j_userInfo"]/span'

    try:
        account_btn_el = driver.find_element(By.XPATH, account_btn_x_path)
    except NoSuchElementException:
        logging.critical("Element does not exist, may be due to using the wrong value for the selector")
        driver.quit()
    else:
        print(driver.find_element(By.ID, "j_balance").text)
        account_btn_el.click()
        print(type(account_btn_el))