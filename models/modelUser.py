import pymongo

class ModelUser:
  def __init__(self):
    self.id = None
    self.username = None
    self.password = None
    self.date_created = None
    self.get_dataBase()

  def get_dataBase(self):
    client = pymongo.MongoClient('localhost', 27017)
    self.db = client['Users']