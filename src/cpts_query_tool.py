from search_classes import SearchClasses

class CptsQueryTool:

    def __init__(self, major, courses_taken):
        self.courses = courses_taken

    """
    Functions to get all of the requirements 
    1. ucore
    2. required_stem
    3. required_comp_sci
    4. required_language
    5. machine_learning 
    6. systems
    7. required_dim
    8. required_software
    9. visual_computing
    10. free_electives
    """

    def get_req(self, req):
        req = SearchClasses.search__classes(self.major,req)
        output = []
        taken = False
        
        for i in range(0,len(req.index)):
            for taken_course in self.courses:
                if taken_course.course_name == req.loc[i].at["course"]:
                    taken = True
            if not taken:
                output.append(req.loc[i])
            taken = True

        return output


    # Use CSV File Names as tiny databases
    def get_all_reqs(self):
        output = []
        #output.append(self.get_req("ucore"))
        output.append(self.get_req("free_electives"))
        output.append(self.get_req("machine_learning"))
        output.append(self.get_req("required_comp_sci"))
        output.append(self.get_req("required_dim"))
        output.append(self.get_req("required_language"))
        output.append(self.get_req("required_security"))
        output.append(self.get_req("required_software"))
        output.append(self.get_req("required_stem"))
        output.append(self.get_req("systems"))
        output.append(self.get_req("visual_computing"))        
        return output


    def get_ucore_reqs(self):
    #     ucore_reqs = self.cpts_reqs("UCORE")
    #     # assuming the result of ucore reqs is 
    #     for i in self.courses:
        pass

    def get_stem_reqs(self):
        pass

    #pass this one
    def get_cpts_reqs(self):
        pass

    def get_programming_reqs(self):
        pass

    def get_ml_reqs(self):
        pass

    def get_systems_reqs(self):
        pass

    def get_dim_reqs(self):
        return self.get_req("required_dim")


    def get_software_reqs(self):
        pass

    def get_visual_computing_reqs(self):
        pass

    def get_free_electives(self):
        pass

    def get_all_reqs(self):
        pass
