from models.modelUser import ModelUser

class ControllerUser:
  def __init__(self, view):
    self.modelUser = ModelUser()
    self.view = view
    