from course_taken import CourseTaken
from cpts_query_tool import CptsQueryTool

# Will act as current user. Right now program only works with one user at a time, although this can be scaled later
class User:
    def __init__(self,course_list):
        self.courses_taken = course_list # ["CPTS_121", "CPTS_122", "CPTS_360", "PHIL_201"]
        self.name = ""                   # Robby Bobby
        self.id_num = 0                  # 069696969
        self.major = "CPTS"                  # Rabine Bobology

    # function to call a db class with self.major and self.courses_taken. function returns list of classes that are still required. 
    def get_required_courses(self):
        query = CptsQueryTool(self.major, self.courses_taken)
        print("Required Data Information Management")
        query.get_dim_reqs()

    def get_total_credits(self):
        sum = 0
        for course in self.courses_taken:
            sum += course.credits
        return sum
        
    def get_upperd_credits(self):
        sum = 0
        for course in self.courses_taken:
            if int(course.course_name[-3:]) <= 300:
                sum += course.credits
        return sum 

    def get_gpa(self):
        total_sum  = 0.0
        credit_sum = 0.0
        for course in self.courses_taken:
            credit_sum += course.credits
            total_sum += self.get_grade(course.grade)*course.credits
        return total_sum / credit_sum

    def get_grade(self,str):
        if str == "A":
            return 4.0
        elif str == "A-":
            return 3.7
        elif str == "B+":
            return 3.3
        elif str == "B":
            return 3.0
        elif str == "B-":
            return 2.7
        elif str == "C+":
            return 2.3        
        elif str == "C":
            return 2.0        
        elif str == "C-":
            return 1.7
        elif str == "D+":
            return 1.3
        elif str == "D":
            return 1.0
        elif str == "D-":
            return 0.7
        else:
            return 0

    # 0 = course couldn't be added (not found or already taken), 1 = course added
    def add_course(self, course_name : str) -> bool:
        pass

    # can only remove courses with an IP type
    def remove_course(self, course_name : str) -> bool:
        pass

    # must be a function so the major can be validated to make sure it's a real major
    def change_major(self, major_name : str) -> bool:
        pass