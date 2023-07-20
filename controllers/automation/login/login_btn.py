from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import logging

def _login_btn(driver) -> None:
    login_btn_x_path = '//*[@id="j_page_header"]/div[1]/div/div[1]/div[1]/div[2]/div[3]/div[1]/button'

    try:
        login_btn_el = driver.find_element(By.XPATH, login_btn_x_path)
    except NoSuchElementException:
        logging.critical("Element does not exist, may be due to using the wrong value for the selector")
        driver.quit()
    else:
        login_btn_el.click()
        print(type(login_btn_el))