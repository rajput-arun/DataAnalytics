def get_unique_marks(class_register: dict) -> list:
    result=[]
    for grades in class_register.values():
        result.append(grades)
    unique_result = list(set(result))
    print(unique_result)
    return(unique_result)

class_register = {
  "Robb Stark": 2,
  "Sansa Stark": 12,
  "Arya Stark": 2,
  "Bran Stark": 2,
  "Jon Snow": 2,
}



get_unique_marks(class_register)
