

class Course:
    def __init__(self, code, name):
        self.code = code
        self.name = name


class Student:
    def __init__(self, name):
        self.name = name


class Student_Course:
    def __init__(self, studID, courseID,registrationDate, report):
        self.studID = studID
        self.courseID = courseID
        self.registrationDate = registrationDate
        self.report = report

