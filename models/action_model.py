class ActionModel:
  
  actions = [
      {'id': 1, 'name': 'Action 1'},
      {'id': 2, 'name': 'Action 2'},
      {'id': 3, 'name': 'Action 3'}
    ] 

  def GetActions(self) -> list:
    return self.actions

  def GetAction(self, action_id: int) -> dict:
    for action in self.actions:
      if action['id'] == action_id:
        return action
    
    return None 