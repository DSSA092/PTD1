#left rotation
"""l=list(map(int,input().split()))
r=int(input())
length=len(l)
r=r%length
for i in range(r):
    l.append(l[0])
    l.pop(0)
print(l)
"""
#rotate right by n points-> clockwise
"""l=list(map(int,input().split()))
n=int(input())
length=len(l)-1
for i in range(n):
    l.insert(0,l[length])
    l.pop()
print(l)
"""
"""Efficient way to rotate an array
l=list(map(int,input().split()))
k=int(input())
n=len(l)
k=k%len(l)

def rotate(l,i,j):
    while i<j:
        l[i],l[j]=l[j],l[i]
        i+=1
        j-=1

rotate(l,0,k-1)
rotate(l,k,n-1)
rotate(l,0,n-1)
print(l)
"""

"""
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
i=0
j=0
res=[]
while i<len(l1) and j<len(l2):
    if l1[i]<l2[j]:
        res.append(l1[i])
        i+=1
    else:
        res.append(l2[j])
        j+=1
while i<len(l1):
    res.append(l1[i])
    i+=1
while j<len(l2):
    res.append(l2[j])
    j+=1
print(res)
"""

#Sliding Window

l=list(map(int,input().split()))
w=int(input())
i=0
c=sum(l[:w])
c1=0
while i<len(l)-w:
    if(c>c1):
        c1=c
    i=i+1

print(c1)


l=list(map(int,input().split()))
w=int(input())
i=0
c=sum(l[:w])
m=0
while i<len(l)-w:
    c+=l[i+w]-l[i]
    m=max(m,c)
    i=i+1

print(m)