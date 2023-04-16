class UserModel:
  
  users = [
      {'id': 1, 'name': 'Alice'},
      {'id': 2, 'name': 'Bob'},
      {'id': 3, 'name': 'Charlie'}
    ]

  def GetUsers(self) -> list:
    return self.users 
  
  def GetUser(self, user_id:int) -> dict:
    for user in self.users:
      if user['id'] == user_id:
        return user
    
    return None