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


# FILE READWRITE MANAGEMENT
def fileRead(filename, fileType):
    with open(os.path.join(PROGRAM_DIRECTORY, "..\\resources\\Data\\", filename), "r") as readfile:
        if fileType == "JSON":
            accessed_data = json.loads(readfile.read())
        else:
            accessed_data = readfile.read()
        return accessed_data
        # print(str(accessed_data["username"]) + " " + str(accessed_data["password"]))


# SCREENSHOT FILE MANAGEMENT
IMAGE_DEFAULT_LOCATION = os.path.join(PROGRAM_DIRECTORY, "..\\resources\\ScheduleCaptures")
dynamic_image_directory = IMAGE_DEFAULT_LOCATION


# TODO: UX [Priority: LOW] - Allow the user to change image save location.
def setImageDirectory(newDirectory):
    pass


def getImageDirectory():
    return IMAGE_DEFAULT_LOCATION
