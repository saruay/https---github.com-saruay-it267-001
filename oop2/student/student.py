class Student:
    def __init__(self,student,name,major) -> None:
        self._student = student
        self._name = name
        self._major = major 
    
    def _displayNameAndMajor(self):
        print(f'Name: {self._name}')
        print(f'Major: {self._major}')