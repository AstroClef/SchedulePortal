from Modules import IOStreamModule as iom
from Classes import PublixIDClass

# TODO: Create a Check Cystem that makes sure that the file Exists
# Handle by creating the file
# TODO: Create a Check System that makses sure user and password elements exist
# Handle by asking for input and saving the new data to the file
myPublixID = PublixIDClass.PublixID(str(iom.fileRead("logindata.json", "JSON")["username"]),
                                    str(iom.fileRead("logindata.json", "JSON")["password"]))
