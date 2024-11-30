from person import Person  # Ensure Person class is defined and imported


class Instructor(Person):
    def __init__(self, name: str, email: str, contact_number: str, address: str, instructor_id: str, role = "Instructor"):
        super().__init__(name, email, contact_number, address)
        self.role = role
        self.__instructor_id = instructor_id
        self._courses_taught = []

    @property
    def instructor_id(self) -> str:
        return self.__instructor_id

    @property
    def courses_taught(self) -> list:
        return self._courses_taught

    def to_dict(self) -> dict:
        """Convert instructor details to a dictionary."""
        return {
            'instructor_id': self.instructor_id,
            'name': self.name,
            'email': self.email,
            'contact_number': self._contact_number,
            'address': self._address,
            # Add other relevant attributes here
        }

    def teach_course(self, course) -> None:
        """Add a course to the list of courses taught by the instructor."""
        if course not in self._courses_taught:  # Check for duplicates
            self._courses_taught.append(course)
            print(f"Course '{course.course_name}' added to instructor '{self.name}'.")
        else:
            print(f"Instructor '{self.name}' is already teaching the course '{course.course_name}'.")

    def display_info(self) -> str:
        """Display information about the instructor."""
        courses = ', '.join(course.course_name for course in self._courses_taught) if self._courses_taught else "No courses taught"
        return