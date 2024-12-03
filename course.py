from datetime import datetime
from typing import List
from assignment import Assignment  # Ensure Assignment class is defined and imported
from grade import Grade            # Ensure Grade class is defined and imported
from student import Student        # Ensure Student class is defined and imported
from instructor import Instructor  # Ensure Instructor class is defined and imported

class Course:

    def __init__(self, course_name: str, course_code: str, instructor: 'Instructor', units: int):
        self.__course_name = course_name
        self.__course_code = course_code
        self.__instructor = instructor
        self._students: List['Student'] = []  # List to hold students
        self._units = units
        self.assignments: List['Assignment'] = []  # Initialize assignments list
        self.grades = {} 
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Course':
        """Create a Course instance from a dictionary."""
        instructor = Instructor(data['instructor_id'])  # Assuming you have a way to get an Instructor instance
        return cls(course_name=data['course_name'], 
                   course_code=data['course_code'], 
                   instructor=instructor, 
                   units=data['units'])
        
    def add_grade(self, course, grade):
        """Add a grade for the given course."""
        self.grades[course.course_code] = grade
        print(f"Grade for {course.course_name} added: {grade}")

    def to_dict(self) -> dict:
        """Convert course details to a dictionary."""
        return {
            'course_name': self.course_name,
            'course_code': self.course_code,
            'instructor_id': self.instructor.instructor_id,
            'units': self._units
        }

    def assign_assignment(self, title: str, description: str, due_date: str) -> None:
        """Create and assign a new assignment to the course."""
        due_datetime = datetime.fromisoformat(due_date)
        if due_datetime <= datetime.now():
            print("Error: The due date must be in the future.")
            return
        
        new_assignment = Assignment(title, description, due_datetime, self)  # Pass self as course
        self.assignments.append(new_assignment)
        print(f"Assignment '{title}' added to course '{self.course_name}'.")

    def input_grades(self) -> None:
        from student import Student
        """Input grades for a specific assignment."""
        assignment_title = input("Enter the assignment title: ")
        assignment = next((a for a in self.assignments if a.title == assignment_title), None)

        if assignment:
            student_id = input("Enter the student's ID: ")
            student = next((s for s in self._students if s.student_id == student_id), None)

            if student:
                self._handle_grade_input(student, assignment)
            else:
                print("Student not found. Please check the ID and try again.")
        else:
            print("Assignment not found. Please check the title and try again.")

    def _handle_grade_input(self, student: Student, assignment: 'Assignment') -> None:
        """Helper method to handle grade input for a specific student."""
        try:
            score = float(input("Enter the grade: "))
            feedback = input("Enter feedback: ")
            grade = Grade(student, assignment, score, feedback)  # Create a Grade instance
            assignment.add_grade(score)  # Assuming add_grade accepts score
            print(f"Grade for student '{student.name}' added to assignment '{assignment.title}'.")
        except ValueError:
            print("Invalid score. Please enter a numeric value.")

    @property
    def course_name(self) -> str:
        return self.__course_name

    @property
    def course_code(self) -> str:
        return self.__course_code

    @property
    def instructor(self) -> 'Instructor':
        return self.__instructor


    def display_info(self) -> str:
        """Display course information."""
        return (f"Course: {self.course_name} \n"
                f"Code: {self.course_code} \n"
                f"Units: {self._units} \n"
                f"Instructor: {self.instructor.name}")
