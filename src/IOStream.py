import os, DriverModule as dm

PROGRAM_DIRECTORY = os.getcwd()

IMAGE_DEFAULT_LOCATION = os.path.join(PROGRAM_DIRECTORY, "/resources/ScheduleCaptures")
image_current_location = IMAGE_DEFAULT_LOCATION


def checkDirectory():
    # True or False - does the requested directory exist?
    dirExists = os.path.isdir(image_current_location)
    if not dirExists:
        # Creates the new directory
        print("Image directory does not exist.")
        print("*Creating New Image Directory*")
        try:
            os.makedirs(image_current_location)
        except OSError as error:
            print(error)
            dm.chromeDriver.close()

    else:
        # Moves on to saving screenshot
        print("Current image directory exists.")


def setDirectory(newDirectory):
    # Cleans up old directory
    os.rmdir(image_current_location)
    # Sets the new directory path
    image_current_location = newDirectory
    # Checks if new path exists, and creates it otherwise
    checkDirectory(image_current_location)


def getDirectory():
    return image_current_location
