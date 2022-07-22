import math as m
def perfect(num):
    sum=1
    i=2
    sq=int(m.sqrt(num))
    while i!=sq:#for i in range(2,sqrt+1):
        if(num%i==0):
            sum=sum+i
            sum+=num//i
            print(i,num//i,sum)
        i+=1
    return sum==num
n=int(input())
res=perfect(n)
print(res)
