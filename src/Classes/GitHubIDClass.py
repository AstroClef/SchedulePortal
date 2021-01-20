import sys


class GitHubID:
    def __init__(self, username, password):
        self.name = "GitHub"
        self.address = "https://github.com/login"
        self.userElementID = "login_field"
        self.passwordElementID = "password"
        self.submitElementName = "submitButton"
        self.username = username
        self.password = password


if __name__ == '__main__':
    sys.exit("!--Code ran from improper Entry Point--!")
