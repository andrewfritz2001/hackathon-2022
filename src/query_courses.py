import sqlite3 as sq

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
#   Courses, Course name, PreReqs, Sequence, Credits, Description (not for ucore)
# Make query class to search for a csv in an sql lite database
#   return the csv matching the name 
#   parse the rows into list
#   zip all the list together
#   pass in a list(zip of list) into a dataframe, return the df containing 
#   all courses in the courses in the csv

#   Make seperate classes to handle this data

class query