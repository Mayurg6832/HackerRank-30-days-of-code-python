import math
def is_prime(num):
    if num==1:
        return False
    if num == 2:
        return True
    if num>2 and num%2==0:
        return False
    
    max_div=math.floor(math.sqrt(num))
    for i in range(3,max_div+1,2):
        if num%i==0:
            return False
    return True

for i in range(int(input())):
    n=int(input())
    if is_prime(n):
        print('Prime')
    else:
        print('Not prime')
