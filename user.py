class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f"Username: {self.username}"


class Student(User):
    def __init__(self, username, password, first_name, last_name):
        super().__init__(username, password)
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, Username: {self.username}"


class Instructor(User):
    def __init__(self, username, password, first_name, last_name, title):
        super().__init__(username, password)
        self.first_name = first_name
        self.last_name = last_name
        self.title = title

    def __str__(self):
        return f"Instructor: {self.title} {self.first_name} {self.last_name}, Username: {self.username}"


class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def __str__(self):
        return f"Admin: {self.username}"
