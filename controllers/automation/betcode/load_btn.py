from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import logging

def _load_btn(driver) -> None:
    load_btn_x_path = '//*[@id="j_betslip"]/div[2]/div[3]/div[1]/button/span/span'

    try:
        load_btn_el = driver.find_element(By.XPATH, load_btn_x_path)
    except NoSuchElementException:
        logging.critical("Element does not exist, may be due to using the wrong value for the selector")
        driver.quit()
    else:
        print(type(load_btn_el), "load")
        load_btn_el.click()
        print(driver.find_element(By.ID, "j_balance").text)