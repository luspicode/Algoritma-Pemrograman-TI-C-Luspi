class Person:
  def __init__(self, name, salary, age):
    self.name = name
    self.__age = age
    self._salary = salary  # Protected property

p1 = Person("Linus", 50000, 55)
print(p1.name)
print(p1._salary)  # Can access, but shouldn't
print(p1._Person__age)




class Student:
  def __init__(self, name):
    self.name = name
    self.__grade = 0

  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print("Grade must be between 0 and 100")

  def get_grade(self):
    return self.__grade

  def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"

student = Student("Emil")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())
