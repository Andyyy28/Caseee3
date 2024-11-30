class Announcement:
    def __init__(self, title, content, date, recipient_groups):
        self.title = title
        self.content = content
        self.date = date
        self.recipient_groups = recipient_groups

    def __str__(self):
        return f"{self.date}: {self.title} - {self.content} (Recipients: {', '.join(self.recipient_groups)})"