from common.database import Database


class User(object):
    def __init__(self, name, account, password):
        self.name = name
        self.account = account
        self.password = password

    @staticmethod
    def isLoginValid(account, password):
        user_data = Database.find_one(collection='users', query={"account": account})
        if user_data is None:
            return False
        if user_data['password'] != password:
            return False
        return True

    @staticmethod
    def register_user(name, account, password):
        user_data = Database.find_one(collection="users", query={"account": account})
        if user_data is not None:
            return False
        User(name, account, password).saveToDB()
        return True

    def saveToDB(self):
        Database.insert(collection='users', data=self.json())

    def json(self):
        return {
            "name": self.name,
            "account": self.account,
            "password": self.password,
        }

    def findUserData(account):
        user_data = Database.find_one(collection='users', query={"account": account})
        return user_data
