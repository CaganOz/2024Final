class Course:
    def __init__(self, course_number, course_title, instructor):
        self.course_number = course_number
        self.course_title = course_title
        self.instructor = instructor 

    def __str__(self):
        return (f"Course Number: {self.course_number}, Title: {self.course_title}, "
                f"Instructor: {self.instructor.first_name} {self.instructor.last_name}")
