class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

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
    def __init__(self,firstName,lastName,idNumber,scores):
        Person.__init__(self,firstName,lastName,idNumber)
        self.scores=scores
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        sum1=0
        for i in self.scores:
            sum1+=i
        avrage=sum1//len(self.scores)
        if avrage in range(90,101):
            return "O"
        elif avrage in range(80,91):
            return "E"
        elif avrage in range(70,81):
            return "A" 
        elif avrage in range(55,71):
            return "P"
        elif avrage in range(40,56):
            return "D"
        elif avrage in range(0,41):
            return "T"
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
