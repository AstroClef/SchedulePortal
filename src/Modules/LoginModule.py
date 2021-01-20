import sys
from Modules import DriverModule as dm


def login(loginID):
    print("*Logging In*")
    dm.chromeDriver.get(loginID.address)
    print("*Resizing Screen*")
    dm.chromeDriver.set_window_size(1920, 1080)
    print("*Filling Form*")
    dm.fill_form_element(loginID.userElementID, loginID.username)
    dm.fill_form_element(loginID.passwordElementID, loginID.password)
    dm.submit_form(loginID.submitElementID)
    print("-Login Completed-")


if __name__ == '__main__':
    sys.exit("!--Code ran from improper Entry Point--!")