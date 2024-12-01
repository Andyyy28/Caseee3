from student import Student
from assignment import Assignment


class Grade:
    def __init__(self, student: 'Student', assignment: 'Assignment', score: float, feedback: str = None):
        self.__student = student  # Student who received the grade
        self.__assignment = assignment  # Associated assignment
        self.__score = score  # Score for the assignment
        self.__feedback = feedback  # Optional feedback from the instructor
        self.validate_score(self.__score)  # Validate the score on initialization

    @property
    def student(self) -> 'Student':
        return self.__student

    @property
    def assignment(self) -> 'Assignment':
        return self.__assignment

    @property
    def score(self) -> float:
        return self.__score

    @property
    def feedback(self) -> str:
        return self.__feedback

    @staticmethod
    def validate_score(score: float) -> None:
        """Validate that the score is within the acceptable range (0-100)."""
        if not (0 <= self.__score <= 100):
            raise ValueError("Score must be between 0 and 100.")

    def display_grade_info(self) -> str:
        """Return a formatted string with the grade information."""
        return (f"Student: {self.student.name} \n"
                f"Assignment: {self.assignment.title} \n"
                f"Score: {self.score} \n"
                f"Feedback: {self.feedback if self.feedback else 'No feedback'}")

    def update_score(self, new_score: float) -> None:
        """Update the score for the assignment and validate it."""
        self.__score = new_score
        self.validate_score()

    def update_feedback(self, feedback: str) -> None:
        """Update the feedback for the grade."""
        self.__feedback = feedback
