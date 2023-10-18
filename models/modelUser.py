import pymongo
from database.database import Database
from bson.objectid import ObjectId
import hashlib
import datetime

class ModelUser:
  def __init__(self):
    self.id = None
    self.userName = None
    self.password = None
    self.date_created = None
    self.last_change = None
    self.db = Database().get_database()

  def registerUser(self, userName, password, confirmPassword):
    existRegister = self.verifyUserRegister(userName)
    if existRegister == False:
      if password == confirmPassword:
        self.id = str(ObjectId())
        self.userName = userName
        encryptedPassword = hashlib.sha256(password.encode()).hexdigest()
        self.password = encryptedPassword
        self.dateCreated = datetime.datetime.now()
        self.lastChange = None
        collection = self.db['usuarios']
        user = {
            "_id": self.id,
            "userName": self.userName,
            "password": self.password,
            "dateCreated": self.dateCreated,
            "lastChange": self.lastChange
        }
        collection.insert_one(user)
      else:
        print("Senhas não coincidem")
    else:
      print("Usuário já cadastrado")
    # return user
    
  def verifyUserRegister(self, userName):
    collection = self.db['usuarios']
    user = collection.find_one({"userName": userName})
    if user == None:
      return False
    else:
      return True
      
