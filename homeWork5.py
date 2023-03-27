class course:
    school = 'RedRover'

    def __init__(self, name, duration, speciality):
        self.__name = name
        self._duration = duration
        self.speciality = speciality


    def study(self):
        return 'You study'

    def get_name(self):
        return f'You study on the course {self.__name}'

    def set_name(self, new_name):
        self.__name = new_name

# создаем объекты этого класса
course1 = course('Python', '4 month', 'Python developer')
course2 = course('Java', '6 month', 'Java developer')
course3 = course('Frontend', '4 month', 'Frontend developer')
course4 = course('QA', '2 month', 'Manual QA')

class practice(course):
    def __init__(self, name, duration, speciality, type):
        super().__init__(name, duration, speciality)
        self.type = type

    def study(self):
        return 'You study by doing'

course5 = practice('QA Avtomation', '4 month', 'QA Avtomation', 'internship')

print(course1.get_name())
course2.set_name('JAVA')
print(course2.get_name())
print(course4.study())
print(course5.study())