import os
import sys
import datetime as dt
import time as t

from Modules import IOStreamModule as iom, NotificationManager as nm
from selenium import webdriver

chromeDriver = webdriver.Chrome(executable_path=os.path.join(iom.PROGRAM_DIRECTORY,
                                                             "../resources/WebDriver/chromedriver.exe"))


def fill_form_element(elementID, userInput):
    activeElement = chromeDriver.find_element_by_id(elementID)
    activeElement.send_keys(userInput)


def submit_form(submitElementID="", submitElementName=""):
    if submitElementID is not None:
        chromeDriver.find_element_by_id(submitElementID).click()
    elif submitElementName is not None:
        chromeDriver.find_element_by_name(submitElementName).click()


def screenCap():
    todays_date = str(dt.date.today())
    directory = iom.getImageDirectory()
    iom.checkDirectory(directory)
    t.sleep(5)
    chromeDriver.save_screenshot(directory + "/ScheduleScreenshot_" + todays_date + ".png")
    nm.sendCompletionNote(directory)
    print("-Screenshot Captured-")


if __name__ == '__main__':
    sys.exit("!--Code ran from improper Entry Point--!")
