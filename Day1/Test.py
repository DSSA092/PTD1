w=int(input("Enter the weight of watermelon"))
if w%2!=0 or  w==2:
    print("No")
else:
    print("Yes")

#

x=int(input("Enter the x dist"))
if(x<5):
    print(1)
elif(x%5==0):
    print(x/5)
else:
    print(x//5+1)



a,b=map(int,input().split())
c=0
while(a<=b):
    a=a*3
    b=b*2
    c=c+1

print(c)


n,m,a,b=map(int,input().split())
if a*m<b:
    print(a*n)
else:
    print((n//m)*b+min(b,(n%m)*a))

