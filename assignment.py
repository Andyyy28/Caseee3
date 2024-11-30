from datetime import datetime  # Correctly import datetime

class Assignment:
    def __init__(self, title: str, description: str, due_date: datetime, course):
        self.__title = title
        self.__description = description
        self.__due_date = due_date  # Expecting a datetime object
        self.__course = course  # The course to which this assignment belongs
        self.grades = []  # Initialize grades list

    @property
    def title(self) -> str:
        return self.__title

    @property
    def description(self) -> str:
        return self.__description

    @property
    def due_date(self) -> datetime:
        return self.__due_date

    @property
    def course(self):
        return self.__course

    def is_overdue(self) -> bool:
        """Check if the assignment is overdue."""
        return datetime.now() > self.__due_date

    def display_info(self) -> str:
        """Display information about the assignment."""
        return (f"Assignment: {self.title} \n"
                f"Description: {self.description} \n"
                f"Due Date: {self.due_date.strftime('%Y-%m-%d %H:%M:%S')} \n"
                f"Course: {self.__course.course_name}")

    def add_grade(self, grade: float) -> None:
        """Add a grade to the assignment."""
        self.grades.append(grade)