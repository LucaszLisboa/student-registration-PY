from models.modelUser import ModelUser

class ControllerUser:
  def __init__(self, view):
    self.modelUser = ModelUser()
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
