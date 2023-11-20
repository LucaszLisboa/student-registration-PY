from database.database import Database
from bson.objectid import ObjectId
import datetime

class ModelStudent:
  def __init__(self):
    self.id = None
    self.name = None
    self.registration = None
    self.dateOfBirth = None
    self.photo = None
    self.db = Database().get_database()

  def registerStudent(self, name, registration, dateOfBirth, photo, userLoggedIn):
    self.validateStudentData(name, registration, dateOfBirth)
    existRegister = self.verifyStudentRegister(registration)
    if existRegister == False:
      self.id = str(ObjectId())
      self.name = name
      self.registration = registration
      self.dateOfBirth = dateOfBirth
      self.photo = photo
      studentsRepository = self.db['students']
      student = {
          "_id": self.id,
          "name": self.name,
          "registration": self.registration,
          "dateOfBirth": self.dateOfBirth,
          "photo": self.photo
      }
      studentsRepository.insert_one(student)
      self.updateLastChangeUserLoggedIn(userLoggedIn)
    else:
      raise ValueError("Matrícula já cadastrada, tente novamente!")
    
  def updateStudent(self, student_id, name, registration, dateOfBirth, photo, userLoggedIn):
    self.validateStudentData(name, registration, dateOfBirth)
    studentsRepository = self.db['students']
    student = studentsRepository.find_one({"_id": student_id})
    if student != None:
      existRegister = self.verifyStudentRegister(registration)
      if existRegister == False or registration == student['registration']:
        studentsRepository.update_one({"_id": student_id}, {"$set": {"name": name, "registration": registration, "dateOfBirth": dateOfBirth, "photo": photo}})
        self.updateLastChangeUserLoggedIn(userLoggedIn)
      else:
        raise ValueError("Matrícula já cadastrada, tente novamente!")
    else:
      raise ValueError("Aluno não encontrado, tente novamente!")

    
  def consultStudents(self, search_term=None):
    studentsRepository = self.db['students']
    if search_term == None:
      return studentsRepository.find()
    else:
      return studentsRepository.find({"name": {"$regex": search_term, "$options": "i"}})
    
  def removeStudent(self, student_id, userLoggedIn):
    studentsRepository = self.db['students']
    studentsRepository.delete_one({"_id": student_id})
    self.updateLastChangeUserLoggedIn(userLoggedIn)
    
  def validateStudentData(self, name, registration, dateOfBirth):
    if not name or not registration or not dateOfBirth:
      raise ValueError("Todos os campos são obrigatórios!")
    
  def verifyStudentRegister(self, registration):
    studentsRepository = self.db['students']
    student = studentsRepository.find_one({"registration": registration})
    if student == None:
      return False
    else:
      return True
    
  def updateLastChangeUserLoggedIn(self, userLoggedIn):
    usersRepository = self.db['usuarios']
    usersRepository.find_one_and_update({"userName": userLoggedIn}, {"$set": {"lastChange": datetime.datetime.now()}})

    
