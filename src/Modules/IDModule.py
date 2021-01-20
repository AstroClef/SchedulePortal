import sys
from Modules import IOStreamModule as iom
from Classes import PublixIDClass, GitHubIDClass

idKeys = iom.fileRead("logindata.json", "JSON")


def getKeys(platform, keytype):
    platform_keys = idKeys[str(platform)]
    requested_key = platform_keys[str(keytype)]
    return requested_key


myPublixID = PublixIDClass.PublixID(str(getKeys("publix", "username")), str(getKeys("publix", "password")))
myGithubID = GitHubIDClass.GitHubID(str(getKeys("github", "username")), str(getKeys("github", "password")))

if __name__ == '__main__':
    sys.exit("!--Code ran from improper Entry Point--!")
