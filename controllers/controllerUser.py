from models.modelUser import ModelUser

class ControllerUser:
  def __init__(self, view):
    self.modelUser = ModelUser()
    self.view = view
    

  def registerUser(self, userName, password, confirmPassword):
    user = self.modelUser.registerUser(userName, password, confirmPassword)
    self.view.showLoginScreen()