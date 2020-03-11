n=int(input())
current=0
maxi=0
while n>0:
    rem=n%2
    if rem is 1:
        current+=1
        if current>maxi:
            maxi=current
    else:
        current = 0

    n=n//2
print(maxi)
