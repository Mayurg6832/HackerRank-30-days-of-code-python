class PhoneNumbers:
    def __init__(self):
        self.nameandnumbers={}
    def numbersAndName(self,name,numbers):
        self.name=name
        self.numbers=numbers
        self.nameandnumbers[self.name]=self.numbers
    def viewInfo(self,name):
        self.name=name
        if self.name in self.nameandnumbers.keys():
            print("{}={}".format(self.name,self.nameandnumbers[self.name]))
        else:
            print("Not found")

phoneNumbers=PhoneNumbers()
limit=int(input())
for i in range(limit):
    name,number=input().split()
    phoneNumbers.numbersAndName(name, number)
while True:
    n=input()
    phoneNumbers.viewInfo(n)
    
