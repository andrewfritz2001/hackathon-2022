from search_classes import SearchClasses
# For storing user information about which courses they have taken.

class CourseTaken:
    def __init__(self, major, category, name):
        self.course_name = name   # CPTS_121
        self.grade = ""         # A-
        self.credits = 0        # 3
        self.term = ""          # Spring 2022
        self.category = category
        #self.chatroom

    def find_course_info(self,major):
        df = SearchClasses.search_classes(major, self.category)
        course = df.loc[df["courses"] == self.course_name]
        print(course)