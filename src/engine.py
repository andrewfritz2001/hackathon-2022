import camelot
import copy
import pandas as pd

import PyPDF2
# import re
# import io

from user import User
from course_taken import CourseTaken

# file = "../bin/SAA_STD_DS.pdf"

class Engine:
    # intitalize the engine with the user's pdf
    def __init__(self,pdf):
        course_list = self.compute_taken_courses(pdf)
        self.user = User(course_list)
        self.get_user_from_pdf(pdf)
        (name,id_num) = self.get_user_from_pdf(pdf)
        self.user.name = name
        self.user.id_num = id_num

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
                
                if l[j][4]:
                    c.credits = float(l[j][4])
                c.type = l[j][5]
                if c.course_title not in [x.course_title for x in taken_course_list]:
                    taken_course_list.append(c)
        print("done")
        return taken_course_list

    def normalize_course_name(self,name):
        name = name.replace("  ", "_")
        name = name.replace("CPT_S", "CPTS")
        return name

    def get_user_from_pdf(self,pdf):
        file = open(pdf,'rb')
        pdfReader = PyPDF2.PdfFileReader(file)
        page = pdfReader.getPage(0)
        text = page.extractText()
        
        text = text[21:] # skipping over "Academic Requirements"
        id_index = text.index(":")
        name = text[:id_index-2]
        id_num = text[id_index+2:id_index+11]
        return (name,id_num)

    def get_user_name(self):
        return self.user.name
    
    def get_user_id(self):
        return self.user.id_num

    def get_user_tcredits(self):
        return self.user.get_total_credits()

    def get_user_dcredits(self):
        return self.user.get_upperd_credits()

    def get_user_gpa(self):
        return round(self.user.get_gpa(),2)