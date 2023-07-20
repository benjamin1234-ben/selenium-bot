from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import logging

def _logout_btn(driver) -> None:
    logout_btn_x_path = '//*[@id="j_userInfo"]/ul/li[8]'

    try:
        logout_btn_el = driver.find_element(By.XPATH, logout_btn_x_path)
    except NoSuchElementException:
        logging.critical("Element does not exist, may be due to using the wrong value for the selector")
        driver.quit()
    else:
        logout_btn_el.click()
        print(type(logout_btn_el))