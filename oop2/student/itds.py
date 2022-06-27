from student import Student

class ITDS(Student):
    def __init__(self, student, name, major) -> None:
        super().__init__(student, name, major)

    def _displayNameAndMajor(self):
        print(f'{self._name}')
        super()._displayNameAndMajor()

stu = ITDS("640108","Amorn","Infomation Technology")
stu._displayNameAndMajor()