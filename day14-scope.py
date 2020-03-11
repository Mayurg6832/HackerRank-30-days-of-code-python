class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        mini=0
        maxi=0
        mini=min(self.__elements)
        maxi=max(self.__elements)
        maxDiff=abs(maxi)-abs(mini)
        self.maximumDifference=maxDiff

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
