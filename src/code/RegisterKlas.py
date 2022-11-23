class RegisterKlas:
    def __init__(self):
        self.name = "name"
        self.email = "email"
        self.username = "username"
        self.password = "password"
        self.isButtonPressed = False

    def setNama(self, name):
        self.name = name

    def setEmail(self, email):
        self.email = email
    
    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password

    def getIsButtonPressed(self):
        return self.isButtonPressed