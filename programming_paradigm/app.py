class Student:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def get_name(self):
        return self._name
    
    @get_name.setter
    def get_name(self, value):
        self._name = value

    @property
    def get_age(self):
        return self._age
    
    @get_age.setter
    def set_age(self, value):
        self._age =value


student1 = Student("Keitie", 25)
student1.set_age