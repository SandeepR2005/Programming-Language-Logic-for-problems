def sumofnum(n):
    return (n*(n+1))/2
def sum(n,num):
    sum=0
    for i in range(n,num+1):
        sum+=i
    return sum
num=int(input("Enter a number :"))
for i in range(1,num+1):
    if(sumofnum(i)==sum(i,num)):
        pivot=i
if(pivot):
    print("The pivot number of ",num," is ",pivot)
else:
    print("Not a pivot ")
    