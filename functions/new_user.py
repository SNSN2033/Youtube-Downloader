from common.database import Database

Database.initialize()
Database.insert('users', {"account": "shining@test.com", "password": "123456", "name": "shining"})
user = Database.find_one('users', {"account": "shining@test.com"})
print(user)