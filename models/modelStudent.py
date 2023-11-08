from database.database import Database
from bson.objectid import ObjectId

class ModelStudent:
  def __init__(self):
    self.id = None
    self.name = None
    self.registration = None
    self.dateOfBirth = None
    self.photo = None
    self.db = Database().get_database()

  def registerStudent(self, name, registration, dateOfBirth, photo):
    self.validateStudentData(name, registration, dateOfBirth)
    existRegister = self.verifyStudentRegister(registration)
    if existRegister == False:
      self.id = str(ObjectId())
      self.name = name
      self.registration = registration
      self.dateOfBirth = dateOfBirth
      self.photo = photo
      collection = self.db['students']
      student = {
          "_id": self.id,
          "name": self.name,
          "registration": self.registration,
          "dateOfBirth": self.dateOfBirth,
          "photo": self.photo
      }
      collection.insert_one(student)
    else:
      raise ValueError("Student already registered, try again!")
    
  def validateStudentData(self, name, registration, dateOfBirth):
    if not name or not registration or not dateOfBirth:
      raise ValueError("Todos os campos são obrigatórios")
    
  def verifyStudentRegister(self, registration):
    collection = self.db['students']
    student = collection.find_one({"registration": registration})
    if student == None:
      return False
    else:
      return True

    
