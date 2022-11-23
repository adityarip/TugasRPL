class User:
    def __init__(self, userid, name, email, username, password):
        self.userid = userid
        self.name = name
        self.email = email
        self.username = username
        self.password = password

    def getID(self):
        return self.userid

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password