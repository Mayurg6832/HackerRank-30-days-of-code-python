n=int(input())
arr=list(map(int,input().rstrip(",").split()))
arr2=arr[::-1]
for i in arr2:
    print(i,end=" ")
