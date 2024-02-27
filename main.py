"""
Procedure:

0. Load web page
1. Sign into web page (username and password followed by login button)
2. Change/select "Custom 75" (studio name) (select from a drop down box)
3. Select the following day (pressing the right arrow button)
4. Select prefered time for booking : 9:00pm - 11:00pm (21:00-23:00) (select by clicking on the box)
5. Update booking type to 24hr
6. Save

IMPORTANT

be able to change the time of booking available-->> asks for input for time

*Books 24 hours in advance to book for 24 hour bookings
*MUST BE '24 HOUR BOOKING' option ***NOT 'ADVANCE' booking option
*Will need to change booking option from advance to 24 hour if loaded outside of time
*If logged in already during the time of 24 hours it will default to only 24 hour setting??
"""

import secretSquirrelSauce
import schedule
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

def evadeCyberPolice():
    int = random.randint(1,4)
    time.sleep(int)

# def waitToLoad(driver, byType, identifier):
#     try:
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located((byType, identifier)))
#     except:
#         TimeoutException


def getThatRoom():
    
    # Start session
    driver = webdriver.Chrome()
    
    # Load webpage
    driver.get(secretSquirrelSauce.abbeyRoad)
    driver.implicitly_wait(10)
    evadeCyberPolice()

    # Enter username
    ar_user = driver.find_element(by=By.ID, value="username")
    ar_user.send_keys(secretSquirrelSauce.userPass)
    evadeCyberPolice()

    # Enter password
    ar_pass = driver.find_element(by=By.ID, value="password")
    ar_pass.send_keys(secretSquirrelSauce.userPass)
    evadeCyberPolice()

    # Login to page
    login_btn = driver.find_element(by=By.XPATH, value='//*[@id="logon"]/fieldset[2]/div/input')
    login_btn.click()
    evadeCyberPolice()

    # Change studio 
    studio_drpdwn = driver.find_element(by=By.CLASS_NAME, value='select2-selection__rendered')
    studio_drpdwn.click()
    evadeCyberPolice()
    studio_slct = driver.find_element(by=By.CLASS_NAME, value='select2-search__field')
    studio_slct.send_keys(secretSquirrelSauce.studio)
    studio_slct.send_keys(Keys.ENTER)
    evadeCyberPolice()

    # select next day
    nxt_btn = driver.find_element(by=By.CLASS_NAME, value='next')
    nxt_btn.click()
    evadeCyberPolice()


    # select time slot
    """
    Whatever the time is -8
    eg. 9:00 = [1], 21:00 = [13]
    """
    time_slot = driver.find_element(by=By.XPATH, value='//*[@id="day_main"]/tbody/tr[11]/td')
    time_slot.click()
    evadeCyberPolice()

    # change booking type to 24h
    bookType = driver.find_element(by=By.ID, value="type")
    select = Select(bookType)
    select.select_by_visible_text('24hr')


    time.sleep(5)


# schedule.every().day.at("21:00").do(getThatRoom)
    
getThatRoom()

