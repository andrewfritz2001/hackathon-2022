import pandas as pd

# storing in a csv for now as data can be ported to any database/file format (HD5)

# CSV File names
#   "visual_computing"
#   "required_software"
#   "required_dim"
#   "systems"
#   "machine_learning"
#   "required_programming"
#   "required_comp_sci"
#   "required_stem"
#   "free_electives"
#   "ucore"

# List order (CSV in sqlite database)
#   Courses, Course name, PreReqs, Sequence, Credits
#   get the csv matching the name 
#   return the csv as a dataframe 

#   Make seperate classes to handle this data
db = {  "CPTS":["required_comp_sci","required_dim","required_language","required_security","required_software","required_stem","free_electives","machine_learning","systems","visual_computing","ucore"],
        "UCORE":["ROOT","COMM","QUAN","WRTG","ART","BSCI","HUM","PSCI","SSCI","DIVR","CAPS"]
}

class SearchClasses:

    '''
        Connects to the database 
        Returns the 
    '''

    @staticmethod
    def search__classes(major, category):
        if major in list(db.keys()) and category in db[major]:
            try:
                print("PATH: ../bin/{major}/{category}.csv")
                df = pd.read_csv(f"../bin/{major}/{category}.csv")
            except:
                print(f"ERROR: {major} does not contain {category}")
                df = None 
        try:
            return df
        except:
            print("ERROR: Could not create data frame")
    
    @staticmethod
    def majors():
        return list(db.keys())

    @staticmethod
    def categories(major):
        if major in list(db.keys()):
            return db[major]
        
        

            

        

        

            
