import os
from dotenv import load_dotenv

import logging

from services.db import connect_db, get_users

from controllers.driver.init import init_driver, init_page

from controllers.automation.login.phone_input import _phone_input
from controllers.automation.login.password_input import _password_input
from controllers.automation.login.login_btn import _login_btn

from controllers.automation.betcode.code_input import _code_input
from controllers.automation.betcode.load_btn import _load_btn

from controllers.automation.betslip.tab_btn import _tab_btn
from controllers.automation.betslip.bet_input import _bet_input
from controllers.automation.betslip.bet_btn import accept_changes_btn, place_bet_btn
from controllers.automation.betslip.confirm_btn import _confirm_btn
from controllers.automation.betslip.ok_btn import _ok_btn

from controllers.automation.logout.account_btn import _account_btn
from controllers.automation.logout.logout_btn import _logout_btn

from controllers.automation.check_funds import _check_funds

from controllers.crypto.keys import loadKeyPair
from controllers.crypto.cryptic import _decrypt

def load_env() -> (str):
    try:
        load_dotenv()
    except:
        logging.error("Cannot load enviromental variables")
    else:
        MONGO_URI = os.getenv("MONGO_URI")
        return (MONGO_URI)
    
def login(driver, user) -> None:
    # Enter phone number
    key = loadKeyPair()
    phone = _decrypt(data=user["phone"], key=key[1])
    _phone_input(driver=driver, phone=int(phone))

    # Enter password
    key = loadKeyPair()
    password = _decrypt(data=user["password"], key=key[1])
    _password_input(driver=driver, password=password)

    # Click login button
    _login_btn(driver=driver)

def betcode(driver, code) -> None:
    # Enter bet code
    _code_input(driver=driver, code=code)

    # Load the bet code
    _load_btn(driver=driver)

def bet_btn(driver) -> None:
    # Accept changes
    accept_changes_btn(driver=driver)

    # Place bet
    place_bet_btn(driver=driver)

def confirm(driver) -> None:
    # Confirm betslip
    _confirm_btn(driver=driver)

    # Finalize betting process
    _ok_btn(driver=driver)

def betslip(driver, user) -> None:
    # Select betting system
    _tab_btn(driver=driver)

    # Enter betting stake amount
    _bet_input(driver=driver, wager=user["wager"])

    # Place bet and accept any changes
    bet_btn(driver=driver)

    # Confirm and finalize betslip
    confirm(driver=driver)

def logout(driver) -> None:
    # Click account button
    _account_btn(driver=driver)

    # Click logout button
    _logout_btn(driver=driver)

def automation(driver, user, code) -> None:
    # Begin login process
    login(driver=driver, user=user)

    # Checks the balance of the user
    funds = _check_funds(driver=driver)

    if(funds):
        # Begin betting process
        betcode(driver=driver, code=code)

        # Begin betslip process
        betslip(driver=driver, user=user)

    # Begin logout process
    logout(driver=driver)

def termination(driver) -> None:
    # Close page
    driver.close()

    # Close the browser and terminate driver session
    driver.quit()
    
def selenium_automation(users, code) -> None:
    # Initialize driver
    driver = init_driver()

    # Initialize Page Driver
    pg_driver = init_page(driver=driver)

    # Begin automation process
    for user in users:
        print(user)
        if user["active"] == 0:
            continue
        automation(driver=pg_driver, user=user, code=code)

    # Terminate automation process
    termination(driver=pg_driver)
    
def _index(code):
    # Load eniviromental variables
    (uri) = load_env()

    # Connect to database
    db = connect_db(uri=uri)

    # Retrieve user's data from database
    users = get_users(db=db)

    # Begin selenium autamation
    selenium_automation(users=users, code=code)