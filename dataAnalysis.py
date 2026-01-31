import numpy as np

def initialize_data():
    subject = np.array(['English', 'Maths', 'Science', 'Social', 'History'])
    students = np.array(['Alice', 'Bob', 'Charlie', 'Dan'])
    marks = np.array([[81, 78, 80, 60, 63],
                      [50, 40, 65, 48, 65],
                      [30, 83, 97, 97, 75],
                      [99, 55, 60, 58, 30]])

    # also can generate random marks for each student and subject as
    # marks = np.random.randint(30, 101, size=(len(students), len(subject)))

    return subject, students, marks

def add_record(studentArray, subjectArray, marksArray):
    print('\n Add New Student Data\n')
    studentName = input('Student Name : ')
    # initialize an empty marks array of same length as subject
    marks = np.empty(len(subjectArray), dtype=int)
    # get inputs from the user
    for i in range(len(subjectArray)):
        marks[i] = int(input(f"Enter marks for {subjectArray[i]}: "))

    studentArray = np.append(studentArray, studentName)
    marksArray = np.vstack((marksArray, marks))

    return studentArray, marksArray

def display_record(studentArray, subjectArray, marksArray):
    
    totalArray = np.sum(marksArray, axis=1)
    avgArray = np.mean(marksArray, axis=1)
    resultArray = np.where(np.all(marksArray >= 40, axis=1), 'Pass', 'Fail')
    
    headerArray = np.hstack(('Student/Subject', subjectArray, np.array(['Total', 'Average', 'Result'])))
    header = "|".join(headerArray)
    print(header)
    
    lengthArray = np.array([len(element) for element in headerArray])
    
    separator = "+".join(["-" * length for length in lengthArray])
    print(separator)
    
    for i, student in enumerate(studentArray):
        row = f"{student :<{lengthArray[0]}}"
        row += ''.join(f"|{mark:<{lengthArray[col+1]}}" for col, mark in enumerate(marksArray[i]))

        row += "|" + f"{totalArray[i]:<{lengthArray[6]}}" 
        row += "|" + f"{avgArray[i]:<{lengthArray[7]}}" 
        row += "|" + f"{resultArray[i]:<{lengthArray[8]}}" 
        print(row)
    print(separator)

def obtain_results(studentArray, subjectArray, marksArray):

    avgSubject = np.mean(marksArray, axis=0)
    
    stdSubject = np.std(marksArray, axis = 0)
    varSubject = np.var(marksArray, axis = 0)
    stdStudents = np.std(marksArray, axis = 1)
    varStudents = np.var(marksArray, axis = 1)
    
    topPerformer =  studentArray[np.argmax(np.sum(marksArray, axis=1))]
    bottomPerformer =  studentArray[np.argmin(np.sum(marksArray, axis=1))]
    
    easiestSubject = subjectArray[np.argmax(avgSubject)]
    hardestSubject = subjectArray[np.argmin(avgSubject)]
    
    totalAverage = np.mean(marksArray)
    totalStd = np.std(marksArray)
    totalVar = np.var(marksArray)
    
   
    print('Total Number of students: ', len(studentArray))
    
    print('\nAverage Marks in Each Subject')
    for i,subject in enumerate(subjectArray):
        print('\t',subject,':', avgSubject[i])
    
    print('\nStandard Deviation and Variance per Subject')
    header = np.array(['Subject Name','Standard Deviation','Variance'])
    print("|".join(header))

    separator = "+".join(["-" * len(item) for item in header])
    print(separator)
    for i, subject in enumerate(subjectArray):
        row = f"{subject :<{len(header[0])}}" +'|'+ f"{stdSubject[i] :<{len(header[1])}}" + '|' + f"{varSubject[i] :<{len(header[2])}}"
        print(row) 
    
    print('\nStandard Deviation and Variance per Student')
    print("|".join(header))

    print(separator)
    for i, student in enumerate(studentArray):
        row = f"{student :<{len(header[0])}}" +'|'+ f"{stdStudents[i] :<{len(header[1])}}" + '|' + f"{varStudents[i] :<{len(header[2])}}"
        print(row)
   
    print('\nTop performer: ', topPerformer)
    print('Bottom performer:', bottomPerformer)
    
    print('\nEasiest Subject:',easiestSubject, '\nHardest Subject:',hardestSubject)
    
    print('\nMetrics across all Students and Subjects')
    print('Average Marks: ',totalAverage, '\nStandard Deviation: ',totalStd, '\nVariance: ',totalVar)
    
def main():
    subject, students, marks = initialize_data()
    while(1):
        choice = int(input('1. Press 1 to Display Student Results\n2. Press 2 to Add a new Student Record\n3. Press 3 to Display Analyzed Results\n4. Press 4 to Exit\n\n'))
        print('-'* 75)
        if(choice == 1):
            display_record(students, subject, marks)
        elif(choice == 2):
            students,marks = add_record(students, subject, marks)
        elif(choice == 3):
            obtain_results(students, subject, marks)
        elif(choice == 4):
            break
        else:
            print('Invalid Choice')
main()