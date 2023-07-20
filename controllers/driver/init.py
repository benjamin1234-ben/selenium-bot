from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

import logging

def init_driver() -> object:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")

    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    except TimeoutError:
        logging.critical("Could not initialize the driver...The process timed out due to poor network connectivity.")
        driver.quit()
    else:
        print(type(driver))
        return driver
    
def init_page(driver) -> object:
    try:
        driver.get("https://www.sportybet.com/ng/")
    except TimeoutError:
        logging.critical("Could not load webpage...The process timed out due to poor network connectivity.")
        driver.quit()
    else:
        print(type(driver))
        return driver