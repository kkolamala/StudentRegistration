import filesUtility
import validations

def registerFields():
    studentDict = {}
    firstName = input('enter first name:')
    lastName = input('enter last name:')
    studentDict['firstName']  = firstName
    studentDict['lastName'] = lastName
    #validate fields
    if not validations.validateFirstName(firstName):
        print('first name is required')
        studentDict = {}
    if not validations.validateLastName(lastName):
        print('last name is required')
        studentDict = {}
    return studentDict
    

def registerStudent():
    studentDict = registerFields()
    if studentDict:
        filesUtility.createStudentRecord(studentDict)
        print('Student record created successfully')
    
registerStudent()