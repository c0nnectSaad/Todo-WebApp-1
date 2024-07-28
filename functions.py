def get_todo(filepath="todos.txt"):
  """
  read from the file and returns the todos in list format...
  """
  with open(filepath, "r") as file:
    todos = file.readlines()
  return todos

def write_todo(text, filepath="todos.txt"):
  """
  writes todo  in the file and returns nothing...
  """
  with open(filepath, "w") as file:
      file.writelines(text)

