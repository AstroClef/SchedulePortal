from Modules import IOStreamModule as iom
import datetime as dt
import time as t
from selenium import webdriver
import os


chromeDriver = webdriver.Chrome(executable_path=os.path.join(iom.PROGRAM_DIRECTORY,
                                                             "../resources/WebDriver/chromedriver.exe"))


def fill_form_element(elementID, userInput):
    activeElement = chromeDriver.find_element_by_id(elementID)
    if activeElement:
        activeElement.send_keys(userInput)
    else:
        print("Website form Element ID, " + elementID + " from \""
              + str(chromeDriver.current_url) + "\", does not exist.")
        print("Please inform the program author with a screenshot of this error.")


def submit_form(submitElementID):
    chromeDriver.find_element_by_id(submitElementID).click()


def screenCap():
    todays_date = str(dt.date.today())
    directory = iom.getImageDirectory()
    iom.checkDirectory()
    t.sleep(5)
    chromeDriver.save_screenshot(directory + "/ScheduleScreenshot_" + todays_date + ".png")
    print("-Screenshot Captured-")
