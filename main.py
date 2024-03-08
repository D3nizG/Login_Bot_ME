import sys
import datetime
import time
import pytz
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


# Halts code for random periods of time
def evadeCyberPolice():
    int = random.randint(1,3)
    time.sleep(int)

# Function to format the time difference into a string to make it human readable
def format_timedelta(td):
    # Extract hours, minutes, and seconds from the timedelta object
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Construct the formatted string
    formatted_time = ""
    if hours > 0:
        formatted_time += f"{hours} hours "
    if minutes > 0:
        formatted_time += f"{minutes} minutes "
    if seconds > 0:
        formatted_time += f"{seconds} seconds"

    return formatted_time.strip()

# Function to pause execution until required time has arrived
def wait_until(target_time):

    london_tz = pytz.timezone('Europe/London')
    london_now = datetime.datetime.now(london_tz)
    target_datetime = london_tz.localize(datetime.datetime.combine(london_now.date(), target_time))

    if target_datetime < london_now:
        target_datetime += datetime.timedelta(days=1)

    time_difference = target_datetime - london_now
    time_left = format_timedelta(time_difference)
    print ("The time left until submission is " + time_left)

    # Convert time difference to seconds
    total_seconds = time_difference.total_seconds()

    # Check if the target time is in the future
    if total_seconds > 0:
        time.sleep(total_seconds)

# menu at the start of application
def main():
    b = input('\nTo book a session enter 1.\nTo exit application enter 2.\n\n')

    if b == "2":
        sys.exit

    elif b == "1":
        setup()

    else:
        print("That is not a valid selection. Please try again.\n")
        main()


#  initialize values and accept additional inputs from user 
def setup(studio = "Custom 75", bookingType = "24hr"):

    print ('\nDefault studio is ' + studio)
    print ('Default session length is 2 hours')
    print ('Default booking type is ' + bookingType + '\n\n')

    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    selection = input("\nTo start proceed with booking enter '1'.\nTo change default studio enter '2'.\
                 \nTo change session length enter '3'.(Currently Unavailable)\nTo change booking type enter '4'.\n\n")
    
    # Option 1 proceed with booking process
    if selection == "1":
        booking_amt = int(input('\nHow many bookings will you want to make?\n\n'))
        sess_times = []
        
        # collect session times for all bookings
        for i in range(booking_amt):
            sess_times += [(input(f"\nPlease enter the session time in the format 'xx:xx' for booking #{i+1}.\
                                     \nFor example 10 pm will be '22:00'\n\n"))]
            
        # run cript for each booking time available
        for i in range(len(sess_times)):
            getThatRoom(username, password, sess_times[i], studio, bookingType)

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
def getThatRoom(username, password, sessionTime, studio, bookingType):

    abbeyRoad = "https://booking.abbeyroadinstitute.co.uk/"

    # Start session
    driver = webdriver.Chrome()
    
    # Load webpage
    driver.get(abbeyRoad)
    driver.implicitly_wait(5)
    evadeCyberPolice()

    # Enter username
    ar_user = driver.find_element(by=By.ID, value="username")
    ar_user.send_keys(username)
    evadeCyberPolice()

    # Enter password
    ar_pass = driver.find_element(by=By.ID, value="password")
    ar_pass.send_keys(password)
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
    sessionTimeHr, *_ = sessionTime.split(":", 1)
    timeIdentifier = int((int(sessionTimeHr))-8)
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


    target_time = datetime.time(int(sessionTimeHr), 0, 1)
    wait_until(target_time)
    submitBooking()

    time.sleep(10)

# the function that jumpstarts all the code
if __name__ == "__main__":
    main()
