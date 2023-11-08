from models.modelUser import ModelUser
from models.modelStudent import ModelStudent

class ControllerUser:
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

  def registerStudent(self, name, registration, dateOfBirth, photo):
    try:
      self.modelStudent.registerStudent(name, registration, dateOfBirth, photo)
      self.view.clearAllFieldsStudent()
      self.view.showSuccessMessage('Student registered successfully!')
    except ValueError as error:
      self.view.showWarningMessage(error)
