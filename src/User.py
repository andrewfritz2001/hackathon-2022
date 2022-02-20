# Will act as current user. Right now program only works with one user at a time, although this can be scaled later

from CourseTaken import CourseTaken

class User:
    def __init__(self):
        self.courses_taken = [] # ["CPTS_121", "CPTS_122", "CPTS_360", "PHIL_201"]
        self.name = ""          # Robby Bobby
        self.id_num = 0         # 069696969
        self.major = ""         # Marine Bobology

    def get_required_courses():
        # function to call a db class with self.major and self.courses_taken. function returns list of classes that are still required. 
        pass

    # 0 = course couldn't be added (not found or already taken), 1 = course added
    def add_course(self, course_name : str) -> bool:
        pass

    # can only remove courses with an IP type
    def remove_course(self, course_name : str) -> bool:
        pass

    # must be a function so the major can be validated to make sure it's a real major
    def change_major(self, major_name : str) -> bool:
        pass