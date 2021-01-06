import DriverModule as dm

def login(scheduleURL, username, password):
    print("*Logging In*")
    dm.chromeDriver.get(scheduleURL)
    print("*Resizing Screen*")
    dm.chromeDriver.set_window_size(1920,1080)

    # These functions may require both the ID and the keys to send
    dm.findandfill_field(username)
    dm.findandfill_field(password)
    dm.submit_form()
    print("-Login Completed-")