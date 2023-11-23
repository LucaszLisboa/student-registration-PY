from models.modelUser import ModelUser
from models.modelStudent import ModelStudent

class Controller:
  def __init__(self, view):
    self.modelUser = ModelUser()
    self.modelStudent = ModelStudent()
    self.view = view
    
  def registerUser(self, userName, password, confirmPassword):
    try:
      self.modelUser.registerUser(userName, password, confirmPassword)
      self.view.showLoginScreen()
    except ValueError as error:
      self.view.showWarningMessage(error)

  def loginUser(self, userName, password):
    try:
      self.modelUser.loginUser(userName, password)
      self.view.showMainScreen()
    except ValueError as error:
      self.view.showWarningMessage(error)

  def registerStudent(self, name, registration, dateOfBirth, photo, userLoggedIn):
    try:
      self.modelStudent.registerStudent(name, registration, dateOfBirth, photo, userLoggedIn)
      self.view.clearAllStudentFields()
      self.view.updateStudentsTable()
      self.view.showSuccessMessage('Aluno cadastrado com sucesso!')
    except ValueError as error:
      self.view.showWarningMessage(error)

  def updateStudent(self, student_id, name, registration, dateOfBirth, photo, userLoggedIn):
    try:
      self.modelStudent.updateStudent(student_id, name, registration, dateOfBirth, photo, userLoggedIn)
      self.view.clearAllStudentFields()
      self.view.updateStudentsTable()
      self.view.showSuccessMessage('Aluno atualizado com sucesso!')
    except ValueError as error:
      self.view.showWarningMessage(error)

  def consultStudents(self, search_term=None):
    return self.modelStudent.consultStudents(search_term)
  
  def removeStudent(self, student_id, userLoggedIn):
    try:
      self.modelStudent.removeStudent(student_id, userLoggedIn)
      self.view.clearAllStudentFields()
      self.view.updateStudentsTable()
      self.view.showSuccessMessage('Aluno removido com sucesso!')
    except ValueError as error:
      self.view.showWarningMessage(error)


