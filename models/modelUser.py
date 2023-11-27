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
    self.checkUserAndPasswordEntry(userName, password)
    if existRegister == False:
      if password == confirmPassword:
        self.id = str(ObjectId())
        self.userName = userName
        encryptedPassword = hashlib.sha256(password.encode()).hexdigest()
        self.password = encryptedPassword
        self.dateCreated = datetime.datetime.now()
        self.lastChange = None
        collection = self.db['users']
        user = {
            "_id": self.id,
            "userName": self.userName,
            "password": self.password,
            "dateCreated": self.dateCreated,
            "lastChange": self.lastChange
        }
        collection.insert_one(user)
      else:
        raise ValueError("Senhas não coincidem, tente novamente!")
    else:
      raise ValueError("Usuário já cadastrado, tente novamente!")
    
  def verifyUserRegister(self, userName):
    collection = self.db['users']
    user = collection.find_one({"userName": userName})
    if user == None:
      return False
    else:
      return True
    
  def checkUserAndPasswordEntry(self, user, password):
    if len(user) < 3:
      raise ValueError("Usuário deve conter no mínimo 3 caracteres, tente novamente!")
    if len(password) < 4:
      raise ValueError("Senha deve conter no mínimo 4 caracteres, tente novamente!")
    
  def loginUser(self, userName, password):
    encryptedPassword = hashlib.sha256(password.encode()).hexdigest()
    collection = self.db['users']
    record = collection.find_one({"userName": userName, "password": encryptedPassword})
    if record is None:
      raise ValueError("Usuário ou senha inválidos, tente novamente!")


      
