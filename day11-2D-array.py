def matrix(array,row,col):
    sum=0
    sum+=array[row-1][col-1]
    sum+=array[row-1][col]
    sum+=array[row-1][col+1]
    sum+=array[row][col]
    sum+=array[row+1][col-1]
    sum+=array[row+1][col]
    sum+=array[row+1][col+1]
    return sum

arr=[]
for i in range(6):
    arr.append(list(map(int, input().rstrip().split())))

max_sum=-63
for i in range(1,5):
    for j in range(1,5):
        total_sum=matrix(arr,i,j)
        if total_sum>max_sum:
            max_sum=total_sum
print(max_sum)
