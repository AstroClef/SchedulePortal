import sys
from Modules import DriverModule as dm, LoginModule as lm, IDModule as idm


def main():
    lm.login(idm.myPublixID)
    dm.screenCap()
    dm.chromeDriver.close()
    print("-Schedule Portal Successful and Terminated-")


if __name__ == '__main__':
    print("-Entry Execution-")
    main()
else:
    sys.exit("!--Code ran from improper Entry Point--!")
