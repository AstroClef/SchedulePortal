from Modules import DriverModule as dm, LoginModule as lm, IDModule as idm
import os


def main():
    lm.login(idm.myPublixID)
    dm.screenCap()
    dm.chromeDriver.close()
    print("Schedule Portal Successful and Terminated")


if __name__ == '__main__':
    print("-Entry Execution-")
    main()
else:
    print("!--Code ran from improper Entry Point--!")
