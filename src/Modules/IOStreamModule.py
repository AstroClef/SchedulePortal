from Modules import DriverModule as dm
import json
import os

# General Program Directory Navigation
PROGRAM_DIRECTORY = os.path.abspath(os.getcwd())


def checkDirectory():
    dirExists = os.path.isdir(dynamic_image_directory)
    if dirExists:
        # Moves on to saving screenshot
        print("Current image directory exists.")
        print(dynamic_image_directory)
    else:
        # Creates the new directory
        print("Image directory does not exist.")
        print("*Creating New Image Directory*")
        try:
            os.makedirs(dynamic_image_directory)
        except OSError as error:
            print(error)
            dm.chromeDriver.close()


# Login Data Management
# TODO: Create a Check Cystem that makes sure that the file Exists
# Handle by creating the file
# TODO: Create a Check System that makses sure user and password elements exist
# Handle by asking for input and saving the new data to the file
savedUser = ""
savedPassword = ""

with open(os.path.join(PROGRAM_DIRECTORY, "..\\resources\\Data\\", "logindata.json"), "r") as activefile:
    ld = activefile.read()

logindata = json.loads(ld)

print(str(logindata["username"]) + " " + str(logindata["password"]))

# Screenshot File Management
IMAGE_DEFAULT_LOCATION = os.path.join(PROGRAM_DIRECTORY, "..\\resources\\ScheduleCaptures")
dynamic_image_directory = IMAGE_DEFAULT_LOCATION


# TODO: UX [Priority: LOW] - Allow the user to change image save location.
def setImageDirectory(newDirectory):
    pass


def getImageDirectory():
    return IMAGE_DEFAULT_LOCATION
