from datetime import datetime
from person import Person
from course import Course
    # Now you can use Course class here.

class DiscussionThread:

    def __init__(self, course: 'Course', title: str, creator: 'Person'):
        self.course = course  # The course associated with this discussion thread
        self.title = title
        self.creator = creator  # Person (could be Student or Instructor)
        self.posts = []  # List of posts (messages) in this thread
        self.timestamp = datetime.now()

    def display_thread(self) -> None:
        """Display the thread details with all posts."""
        print(f"Discussion Thread: {self.title}")
        print(f"Created by: {self.creator.name} on {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Course: {self.course.course_name}")
        print("Posts:")
        for post in self.posts:
            print(f"- {post['person']} ({post['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}): {post['message']}")
