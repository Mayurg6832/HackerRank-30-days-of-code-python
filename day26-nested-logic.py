returnDate=list(map(int,input().split()))
dueDate=list(map(int,input().split()))
if returnDate[-1]>dueDate[-1]:
    print("10000")
elif returnDate[1]>dueDate[1] and returnDate[-1]>=dueDate[-1]:
    print(500*(returnDate[1]-dueDate[1]))
elif returnDate[0]>dueDate[0] and returnDate[1]>=dueDate[1] and returnDate[-1]>=dueDate[-1]:
    print(15*(returnDate[0]-dueDate[0]))
else:
    print(0)
