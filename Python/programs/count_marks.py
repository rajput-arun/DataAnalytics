def count_marks(class_register: dict) -> dict:
    result={}
    for grades in class_register.values():
        if grades in result:
            result[grades] += 1
        else:
            result[grades] = 1
        grades += 1
    print(result)
    return(result)

class_register = {
  "Robb Stark": 10,
  "Sansa Stark": 12,
  "Arya Stark": 6,
  "Bran Stark": 8,
  "Jon Snow": 8,
}


count_marks(class_register)
