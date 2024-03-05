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

Should be able to change the time of booking available-->> asks for input for time

*Books 24 hours in advance to book for 24 hour bookings
*MUST BE '24 HOUR BOOKING' option ***NOT 'ADVANCE' booking option
*Will need to change booking option from advance to 24 hour if loaded outside of time
*If logged in already during the time of 24 hours it will default to only 24 hour setting??
"""

import secretSquirrelSauce
import sys
import schedule
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

"""
Code starts here
""" 

def evadeCyberPolice():
    int = random.randint(1,4)
    time.sleep(int)

def menu():
    b = input('To book a session enter 1.\nTo exit application enter 2.\n\n')

    if b == "2":
        sys.exit

    elif b == "1":
        setup()

    else:
        print("That is not a valid selection. Please try again.\n")
        menu()


# booking_amt = input('How many bookings will you want to make?')
# print("The default studio is Custom 75.\nThe default studio session time is 2 hours.") 
# sess_time = 


# schedule.every().day.at("21:00").do(getThatRoom)

def setup():
    print ('Default studio is "Custom 75"')
    print ('Default session length is 2 hours')
    print ('Default booking type is 24hr\n\n')

    selection = input("To start proceed with booking enter '1'.\nTo change defaut studio enter '2'.\nTo change session length enter '3'.\nTo change boking type enter '4'.\n\n")
    if selection == "1":
        booking_amt = int(input('How many bookings will you want to make?'))
        sess_times = []
        for i in range(booking_amt):
            sess_times += [int(input(f"Please enter the session time in the format 'xxxx' for booking #{i}\nFor example 10 pm will be '2200'\n"))]
            # print(sess_times)
        for i in range(len(sess_times)):
            getThatRoom(sess_times[i])
    elif selection == "2":
        pass

    else:
        pass


def getThatRoom(sessionTime):
    
    # Start session
    driver = webdriver.Chrome()
    
    # Load webpage
    driver.get(secretSquirrelSauce.abbeyRoad)
    driver.implicitly_wait(5)
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
    timeIdentifier = (int(sessionTime)/100)-8
    time_slot = driver.find_element(by=By.XPATH, value=f'//*[@id="day_main"]/tbody/tr[{timeIdentifier}]/td')
    time_slot.click()
    evadeCyberPolice()

    # change booking type to 24h
    bookType = driver.find_element(by=By.ID, value="type")
    select = Select(bookType)
    select.select_by_visible_text('24hr')


    # submit booking request
    """
    nxt_btn = driver.find_element(by=By.CLASS_NAME, value='default_action')
    nxt_btn.click()
    evadeCyberPolice()
    """

    time.sleep(5)


# schedule.every().day.at("21:00").do(getThatRoom)

menu()

# getThatRoom()

