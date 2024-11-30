from course import Course


class Schedule:
    def __init__(self, course: 'Course', day: str, time: str):
        self.__course = course
        self.__day = day
        self.__time = time

    @property
    def course(self) -> 'Course':
        return self.__course

    @property
    def day(self) -> str:
        return self.__day

    @property
    def time(self) -> str:
        return self.__time

    def display_schedule(self) -> str:
        return f"Course: {self.course.course_name}, Day: {self.day}, Time: {self.time}"
    
