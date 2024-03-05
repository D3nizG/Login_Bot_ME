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
import datetime
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

"""
Code starts here
""" 

"""some functions that help with the functionality of the bot"""
# Randomly halts code
def evadeCyberPolice():
    int = random.randint(1,4)
    time.sleep(int)


# function to pause execution until time has arrived
def wait_until(target_time):
    target_datetime = datetime.datetime.combine(datetime.datetime.today(), target_time)

    time_difference = target_datetime - datetime.datetime.now()
    
    # Convert time difference to seconds
    total_seconds = time_difference.total_seconds()

    # Check if the target time is in the future
    if total_seconds > 0:
        time.sleep(total_seconds)
    else:
        print("Target time is already in the past.")

# menu at the start of application
def menu():
    b = input('\nTo book a session enter 1.\nTo exit application enter 2.\n\n')

    if b == "2":
        sys.exit

    elif b == "1":
        setup()

    else:
        print("That is not a valid selection. Please try again.\n")
        menu()


#  initialize values and accept additional inputs from user 
def setup(studio = "Custom 75", bookingType = "24hr"):

    print ('\nDefault studio is ' + studio)
    print ('Default session length is 2 hours')
    print ('Default booking type is ' + bookingType + '\n\n')

    selection = input("To start proceed with booking enter '1'.\nTo change default studio enter '2'.\
                 \nTo change session length enter '3'.(Currently Unavailable)\nTo change booking type enter '4'.\n\n")
    
    # Option 1 proceed with booking process
    if selection == "1":
        booking_amt = int(input('\nHow many bookings will you want to make?\n\n'))
        sess_times = []
        
        # collect session times for all bookings
        for i in range(booking_amt):
            sess_times += [int(input(f"\nPlease enter the session time in the format 'xxxx' for booking #{i+1}.\
                                     \nFor example 10 pm will be '2200'\n"))]
            
        # run cript for each booking time available
        for i in range(len(sess_times)):
            getThatRoom(sess_times[i], studio, bookingType)

    # Option 2 change studio
    elif selection == "2":
        print("\nStudio Selection options are Angel - Prod Suites, Angel Two, Angel Post, Custom 75, Tech Lab One, and Tech Lab Two")
        studio = input("Please enter the name of the studio you would like to book.\n\n")
        return setup(studio = studio, bookingType = bookingType)

    # Option 3 change session length
    elif selection == "3":
        print("\nThat feature is still under development. Please choose another option.\n\n")
        setup()

    # Option 4 change booking type 
    elif selection == "4":
        print("\nBooking types are '24hr' and 'Advance'")
        bookingType = input("Please enter the booking type you would like.\n\n")
        return setup(studio = studio, bookingType = bookingType)

    else:
        print("\nThat is not a valid selection. Please try again.\n")
        setup()


#Initiate and run the selenium script
def getThatRoom(sessionTime, studio, bookingType):
    
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
    studio_slct.send_keys(studio)
    studio_slct.send_keys(Keys.ENTER)
    evadeCyberPolice()

    # select next day
    nxt_btn = driver.find_element(by=By.CLASS_NAME, value='next')
    nxt_btn.click()
    evadeCyberPolice()


    # select time slot
    """
    Calculatins for div value : Whatever the booking time is -8
    eg. 9:00 = [1], 21:00 = [13]
    """
    timeIdentifier = (int(sessionTime)/100)-8
    time_slot = driver.find_element(by=By.XPATH,\
                                    value=f'//*[@id="day_main"]/tbody/tr[{timeIdentifier}]/td')
    time_slot.click()
    evadeCyberPolice()

    # change booking type to 24h
    bookType = driver.find_element(by=By.ID, value="type")
    select = Select(bookType)
    select.select_by_visible_text(bookingType)

    # submit booking request
    def submitBooking():
        nxt_btn = driver.find_element(by=By.CLASS_NAME, value='default_action')
        nxt_btn.click()
        evadeCyberPolice()

    target_time = datetime.time(6, 3, 0)
    wait_until(target_time)
    submitBooking()

    time.sleep(10)

# the function that jumpstarts all the code
menu()
