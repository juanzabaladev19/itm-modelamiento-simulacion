class Person:
    id:str = None
    fullname: str = None
    email: str = None

    def __init__(self, id: str):
        self.id = id

    def setId(self, id:str):
        self.id = id
    def getId(self):
        return self.id
    def setFullname(self, fullname:str):
        self.fullname = fullname
    def getFullname(self):
        return self.fullname
    def setEmail(self, email:str):
        self.email = email
    def getEmail(self):
        return self.email
