class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

from statistics import mean

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName,idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        avg = mean(self.scores)
        if avg >= 90 and avg <= 100:
            grade = 'O'
        elif avg >=80 and avg < 90:
            grade = 'E'
        elif avg >=70 and avg < 80:
            grade = 'A'
        elif avg >=55 and avg < 70:
            grade = 'P'
        elif avg >=40 and avg < 55:
            grade = 'D'
        else:
            grade = 'T'
        return grade


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())