import camelot
import copy
import pandas as pd

from user import User
from course_taken import CourseTaken

# file = "../bin/SAA_STD_DS.pdf"

class Engine:
    # intitalize the engine with the user's pdf
    def __init__(self,pdf):
        course_list = self.compute_taken_courses(pdf)
        self.user = User(course_list)


    # transfers pds to a list of camelot tables
    def pdf_to_dataframes(self,pdf):
        tables = camelot.read_pdf(pdf, pages="all",line_scale=30)
        print("Total tables extracted:", tables.n)
        return tables

    # camelot table --> numpy array --> user.courses_taken[]
    def compute_taken_courses(self,pdf):
        dataframes = self.pdf_to_dataframes(pdf)
        taken_course_list = []
        for i in range (1,dataframes.n):
            d = dataframes[i].df
            l = d.values.tolist()
            print(l)
            for j in range(1,len(l)):
                c = CourseTaken()
                c.term = l[j][0]
                c.course_name = self.normalize_course_name(l[j][1])
                c.course_title = l[j][2]
                c.grade = l[j][3]
                c.credits = l[j][4]
                c.type = l[j][5]
                taken_course_list.append(c)
        print("done")
        return taken_course_list

    def normalize_course_name(self,name):
        name = name.replace("  ", "_")
        name = name.replace("CPT_S", "CPTS")
        return name

        