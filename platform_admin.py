# platform_admin.py
import json
from enrollment import Enrollment

class PlatformAdmin:
    def __init__(self):
        self.students = []
        self.instructors = []
        self.courses = []
        self.enrollments = Enrollment()  # Ensure Enrollment does not import PlatformAdmin

    @staticmethod
    def admin_login():
        """Authenticate admin user."""
        email = input("Enter admin email: ")
        password = input("Enter admin password: ")

        try:
            with open("data.json", "r") as file:
                data = json.load(file)

            admins = data.get("admins", [])
            for admin in admins:
                if admin["email"] == email and admin["password"] == password:
                    print("Login successful. Welcome, Admin!")
                    return True

            print("Invalid email or password. Access denied.")
            return False

        except FileNotFoundError:
            print("Error: data.json file not found.")
            return False

    def load_data(self, filename='data.json'):
        import student  # Moved import
        import course   # Moved import
        import instructor  # Moved import
        import schedule

        try:
            with open(filename, 'r') as f:
                data = json.load(f)

                # Load instructors
                self.instructors = [instructor.Instructor(**instructor_data) for instructor_data in data.get('instructors', [])]

                # Load students
                self.students = [student.Student.from_dict(student_data, self.courses) for student_data in data.get('students', [])]

                # Load courses
                self.courses = []
                for course_data in data.get('courses', []):
                    instructor_id = course_data.get('instructor_id')
                    
                    if instructor_id is None:
                        print(f"Warning: Missing instructor_id in course data for '{course_data.get('course_name', 'Unknown')}'.")
                        continue
                    
                    instructor_obj = next(
                        (i for i in self.instructors if i.instructor_id == instructor_id), 
                        None
                    )
                    
                    if not instructor_obj:
                        print(f"Warning: Instructor ID {instructor_id} not found. Skipping course '{course_data.get('course_name', 'Unknown')}'.")
                        continue
                    
                    course_obj = course.Course(course_data['course_name'], course_data['course_code'], instructor_obj, course_data['units'])
                    self.courses.append(course_obj)

                # Load enrollments
                for enrollment in data.get('enrollments', []):
                    student_obj = next((s for s in self.students if s.student_id == enrollment['student_id']), None)
                    course_obj = next((c for c in self.courses if c.course_code == enrollment['course_code']), None)
                    
                    if student_obj and course_obj:
                        student_obj.enroll(course_obj)
                    else:
                        if not student_obj:
                            print(f"Warning: Student ID {enrollment['student_id']} not found during enrollment.")
                        if not course_obj:
                            print(f"Warning: Course code {enrollment['course_code']} not found during enrollment.")

                 # Load schedules
                schedules = data.get('schedules', [])
                for schedule_data in schedules:
                    course_obj = next((c for c in self.courses if c.course_code == schedule_data['course_code']), None)
                if course_obj:
                    schedule_obj = schedule.Schedule(course_obj, schedule_data['day'], schedule_data['time'])
                    course_obj.schedule = schedule_obj  # Attach the schedule to the course
                else:
                    print(f"Warning: Course with code {schedule_data['course_code']} not found for schedule.")

        except FileNotFoundError:
            print("Data file not found. Starting with empty data.")
        except json.JSONDecodeError:
            print("Error decoding JSON data. Please check the file format.")