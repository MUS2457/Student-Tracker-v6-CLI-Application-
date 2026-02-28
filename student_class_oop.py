class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = {}

    def add_subject(self, subject, score):
        self.subjects[subject] = score

    def to_dictionary(self):
        # JSON cannot store objects  convert to pure data
        return {
            "name": self.name,
            "subjects": self.subjects
        }

    @classmethod
    def from_dictionary(cls, data):
        # Rebuild object from saved JSON data
        student = cls(data["name"])
        student.subjects = data["subjects"]
        return student

