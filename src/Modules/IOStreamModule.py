import json
import os
import sys

from Modules import DriverModule as dm

# General Program Directory Navigation
PROGRAM_DIRECTORY = os.path.abspath(os.getcwd())


def createDirectory(new_directory):
    print("*Creating Directory*")
    try:
        os.makedirs(new_directory)
    except OSError as error:
        print(error)
        dm.chromeDriver.close()


def checkDirectory(checked_directory):
    dirExists = os.path.isdir(checked_directory)
    fileExists = os.path.isfile(checked_directory)
    if dirExists or fileExists:
        print("Current directory exists.")
        print(checked_directory)
        return True
    else:
        return False


# FILE READWRITE MANAGEMENT
def fileRead(file_name, file_type):
    file_path = os.path.join(PROGRAM_DIRECTORY, "..\\resources\\Data\\", file_name)
    if checkDirectory(file_path):
        with open(file_path, "r") as readfile:
            if file_type == "JSON":
                accessed_data = json.loads(readfile.read())
            else:
                accessed_data = readfile.read()
            return accessed_data
    else:
        dm.chromeDriver.close()
        raise FileNotFoundError(file_name + " could not be found. \nTerminating Program...")


# SCREENSHOT FILE MANAGEMENT
IMAGE_DEFAULT_LOCATION = os.path.join(PROGRAM_DIRECTORY, "..\\resources\\ScheduleCaptures")
dynamic_image_directory = IMAGE_DEFAULT_LOCATION


def getImageDirectory():
    return dynamic_image_directory


if __name__ == '__main__':
    sys.exit("!--Code ran from improper Entry Point--!")
