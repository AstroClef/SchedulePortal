from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime as dt, time as t, IOStream as ios

# instantiates the Chrome Driver
chromeDriver = webdriver.Chrome(executable_path="E:\GameDev\PythonTestField\WebDrivers\chromedriver.exe")

activeElement = False


# Searches for an HTML Form field by ID
# the "fieldname" arguement could pass case sensitive instead of using a case system.
# TODO Add second arguement that passes string to send to active element.
def findandfill_field(fieldname):
    print("*Searching for '" + fieldname + "' field in the fillable form.*")
    if fieldname == "USERNAME":
        activeElement = chromeDriver.find_element_by_id("userNameInput")

        # Checking if the activeElement isnt found like this, may be irrelevent since Chrome Driver throws it's own err
        # this IF-ELSE may be replaced by a try catch later
        if activeElement:
            print("Found Username field.")
            print("*Filling out Form*")

            # strings sent to active elements will be pulled from an encrypted JSON for safety
            activeElement.send_keys("p1530404")
        else:
            print("User field not found.")

    # CodeBlock: Same as USERNAME but for PASSWORD
    # By using a case-sensitive arg for parent func, we can reduce redundancy,
    elif fieldname == "PASSWORD":
        active_element2 = chromeDriver.find_element_by_id("passwordInput")
        if active_element2:
            print("Found Password field.")
            print("*Filling out Form*")
            active_element2.send_keys("p@ssword1")
    else:
        print("Cannot find '" + fieldname + "' in the form.")


# Separated func to submit the HTML forum - allows control over when it is called.
# TODO add an arg that passes a field ID for Chrome Driver to use
def submit_form():
    chromeDriver.find_element_by_id("submitButton").click()


# Function to capture screenshot of schedual
def screenCap():
    todaysdate = str(dt.date.today())
    directory = ios.getDirectory()
    # Checks if the photo director exists
    ios.checkDirectory()
    # Waits for webpage to load before taking a screenshot
    t.sleep(2)
    chromeDriver.save_screenshot(directory + "ScheduleScreenshot_" + todaysdate + ".png")
    print("-Screenshot Captured-")
