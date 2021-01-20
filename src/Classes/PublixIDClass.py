import sys


class PublixID:
    def __init__(self, username, password):
        self.name = "Publix"
        self.address = "https://oasis-sso.publix.org/ess/portal?siteId=0566#wfmess/wfmess-myschedule////"
        self.userElementID = "userNameInput"
        self.passwordElementID = "passwordInput"
        self.submitElementID = "submitButton"
        self.username = username
        self.password = password


if __name__ == '__main__':
    sys.exit("!--Code ran from improper Entry Point--!")
