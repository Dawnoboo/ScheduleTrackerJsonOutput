import json
class Course: # convert this sample class to json
    # stuff known already known
    courseTitle: str
    courseSubject: str
    courseNumber: str
    units: int
    # stuff needing to be calculated before function call
    preRequirements = [] # what classes are needed for this course (need to determine if this should be an id to prereqs or just the name of said prereq)
    genEdFulfillment = [] # what areas of CalGETC does this cover?
    useableForSchools = [] # what schools need this
    def __init__(self, t: str, s: str, n: str, u: int, p: list[str], g: list[str], U: list[str]): # simple class constructor
        self.courseTitle = t
        self.courseSubject = s 
        self.courseNumber = n
        self.units = u 
        self.preRequirements = p
        self.genEdFulfillment = g 
        self.useableForSchools = U

# sample dict: 
# dictionary = {"College": ["Chabot","LasPositas"], "Courses": [[courseA, courseB,courseC],[courseA]]}
# Number of college names must match number of arrays in courses

# Template function for outputting data from algorithms to front via json
def User_Courses(result): # argument : dict
    output = [] # what will be outputted into a Json
    i = 0 # needed for inner for loop
    indent = 0 # counts number of indents (kinda like number of lines) we need
    for college in result["College"]: # loops through each college
        temp = {
                college: [] # will store our course info as json objects
            }
        for course in result["Courses"][i]: # loops through the actual courses
            courseTemp = {
                "title": course.courseTitle,
                "subject": course.courseSubject,
                "number": course.courseNumber,
                "units": course.units,
                "preReq":course.preRequirements,
                "genEd": course.genEdFulfillment,
                "forSchools": course.useableForSchools
            }
            indent += 1
            temp[college].append(courseTemp) # pushes the course to the end of the Temp
        output.append(temp) # pushes the temp to the end of the output
        i += 1
        indent +=1
    with open("result.json", "w") as file:
        json.dump(output,file, indent=indent) # dumps output into a json format

# Sample test Code : 
# a = Course("Introduction to Programming C++","CSCI", "14", 3, ["MTH55"],[],["SJSU"])
# b = Course("Calcus II", "MTH", "2", 5,["MTH1"],["Area 2"],["SJSU"])
# c = Course("General Physics I","PHYS","1A",5,["MTH2"],["Area 5A"],["SJSU"])
# d = {"College": ["chabot","lasPositas"], "Courses": [[a,b],[c]]}
# User_Courses(d)
#
# Sample json output :
# [
#      {
#           "chabot": [
#                {
#                     "title": "Introduction to Programming C++",
#                     "subject": "CSCI",
#                     "number": "14",
#                     "units": 3,
#                     "preReq": [
#                          "MTH55"
#                     ],
#                     "genEd": [],
#                     "forSchools": [
#                          "SJSU"
#                     ]
#                },
#                {
#                     "title": "Calcus II",
#                     "subject": "MTH",
#                     "number": "2",
#                     "units": 5,
#                     "preReq": [
#                          "MTH1"
#                     ],
#                     "genEd": [
#                          "Area 2"
#                     ],
#                     "forSchools": [
#                          "SJSU"
#                     ]
#                }
#           ]
#      },
#      {
#           "lasPositas": [
#                {
#                     "title": "General Physics I",
#                     "subject": "PHYS",
#                     "number": "1A",
#                     "units": 5,
#                     "preReq": [
#                          "MTH2"
#                     ],
#                     "genEd": [
#                          "Area 5A"
#                     ],
#                     "forSchools": [
#                          "SJSU"
#                     ]
#                }
#           ]
#      }
# ]