from person import Person

class Student(Person):
    def __init__(self, name, email, contact_number, address, student_id, year_level, program, gpa=0.0, birth_date=None, enrolled_courses=None, role = "Student"):
        super().__init__(name, email, contact_number, address)
        self.__student_id = student_id
        self._enrolled_courses = []
        self.__year_level = year_level
        self.__program = program
        self.__gpa = gpa
        self.__birth_date = birth_date
        self.role = role
        self._enrolled_courses = enrolled_courses if enrolled_courses is not None else []

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'contact_number': self._contact_number,
            'address': self._address,
            'student_id': self.student_id,
            'year_level': self.year_level,
            'program': self.program,
            'gpa': self.gpa,
            'birth_date': self.birthdate,
            'enrolled_courses': [course.to_dict() for course in self.enrolled_courses]  # Assuming Course has a to_dict method
        }

    @classmethod
    def from_dict(cls, data, all_courses):
        student = cls(data['name'], data['email'], data['contact_number'], data['address'],
                      data['student_id'], data['year_level'], data['program'])
        student.gpa = data['gpa']
        student.birthdate = data['birth_date']
        
        # Load actual Course objects from the enrolled_courses list of dictionaries
        for course_data in data.get('enrolled_courses', []):
            course = next(
                (c for c in all_courses if c.course_code == course_data['course_code']), 
                None
            )
            if course:
                student.enroll(course)

        return student
    
    @property
    def student_id(self):
        return self.__student_id

    @property
    def year_level(self):
        return self.__year_level

    @property
    def program(self):
        return self.__program

    @property
    def birthdate(self):
        return self.__birth_date

    @birthdate.setter
    def birthdate(self, value):
        self.__birth_date = value

    @property
    def enrolled_courses(self):
        return self._enrolled_courses

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        if 0 <= value <= 4.0:
            self.__gpa = value
        else:
            raise ValueError("GPA must be between 0 and 4.0")

    def enroll(self, course):
        if course not in self._enrolled_courses:  # Check for duplicates
            self._enrolled_courses.append(course)

    def display_info(self):
        return (f"ID: {self.student_id} \nStudent: {self.name} \nYear Level: {self.year_level} "
                f"\nProgram: {self.program} \nEmail: {self.email} \nContact#: {self._contact_number} "
                f"\nAddress: {self._address}")
