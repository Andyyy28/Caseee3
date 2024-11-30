from typing import List
from student import Student  # Correctly import Student
from course import Course    # Ensure Course is imported

# Enrollment Class
class Enrollment:
    def __init__(self):
        self._enrollments: List[dict] = []  # Explicitly type the list for better clarity

    def enroll_student(self, student: 'Student', course: 'Course') -> None:
        """Enroll a student in a course if they are not already enrolled."""
        if not any(enrollment['course'] == course and enrollment['student'] == student for enrollment in self._enrollments):
            student.enroll(course)
            course.add_student(student)
            self._enrollments.append({'student': student, 'course': course})
            print(f"{student.name} has been enrolled in {course.course_name}.")
        else:
            print(f"{student.name} is already enrolled in {course.course_name}.")

    def get_enrollment_list(self) -> list:
        """Return a list of all enrollments in a readable format."""
        return [f"{enrollment['student'].name} enrolled in {enrollment['course'].course_name}" for enrollment in self._enrollments]

    def display_enrollments(self) -> None:
        """Display all enrollments."""
        if not self._enrollments:
            print("No enrollments found.")
            return
        
        print("Current Enrollments:")
        for enrollment in self._enrollments:
            print(f"- {enrollment['student'].name} enrolled in {enrollment['course'].course_name}")