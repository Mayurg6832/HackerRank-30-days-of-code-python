for m in range(int(input())):
    s=input()
    for i in range(0,len(s),2):
        print(s[i],end="")
    print(end=" ")
    for j in range(1,len(s),2):
        print(s[j],end="")
    print("\n",end="")
