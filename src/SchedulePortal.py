import LoginModule as lm, DriverModule as dm, IOStream as ios


def main():
    lm.login("https://oasis-sso.publix.org/ess/portal?siteId=0566#wfmess/wfmess-myschedule////", "USERNAME", "PASSWORD")
    dm.screenCap()
    dm.chromeDriver.close()
    print("Schedual Portal Successful and Terminated")


if __name__ == '__main__':
    print("-Entry Execution-")
    main()
else:
    print("!--Code ran from impropper Entry Point--!")
