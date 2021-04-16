import json #module makes it easy to parse JSON strings and files containing JSON object
def createStudentRecord(studentData):
    with open('student.json','a') as outfile:
        json.dump(studentData,outfile)
    
    