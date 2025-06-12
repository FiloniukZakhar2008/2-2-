class Zakhar:
    def __init__(self, first_name=None, last_name=None, birth_year=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def calculate_course(self):
        if self.birth_year is None:
            return None
        current_year = 2025
        age = current_year - self.birth_year
        if 17 <= age <= 21:
            return age - 15
        return None

    def get_name_list(self):
        return [self.first_name, self.last_name]


class StudentExtended(Zakhar):
    def __init__(self, first_name, last_name, birth_year, university, major, student_id):
        super().__init__(first_name, last_name, birth_year)
        self.university = university
        self.major = major
        self.__student_id = student_id

    def _generate_email(self):
        if self.first_name and self.last_name:
            return f"{self.first_name.lower()}.{self.last_name.lower()}@{self.university.lower().replace(' ', '')}.edu"
        return None

    def get_full_info(self):
        email = self._generate_email()
        return {
            "Name": f"{self.first_name} {self.last_name}",
            "Birth Year": self.birth_year,
            "University": self.university,
            "Major": self.major,
            "Course": self.calculate_course(),
            "Email": email,
            "Student ID": self.__student_id
        }


extended_student = StudentExtended("Захар", "Філонюк", 2008, "Київський національний університет", "Інформатика", "123456")

print(extended_student.get_full_info())
