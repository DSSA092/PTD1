"""#l=[2,3,44,True,"Sash"]

#l=list(map(int,input().split()))

#l=input().split()


l=[1,2,3,4,5,6]

l.append(7) # adds an element to a list at the end
l.insert(3,3.5) # to insert in the middle of a list
l.extend([7,8,9]) # can add another list at the end, extend only works with iterable items ie, strings,list  not an individual object like l.extend(10) -> shows an error


l1=[1,2,3]
l2=l1 # here l1 and l2 points to the same object ie same reference address
l2.append(4)
print(len(l)) # gives 4

l1=[1,2,3]
l2=l1.copy # hcreates a whole new list which points at different reference location
l2.append(4)
print(len(l)) # gives 3


l=[5,1,2,8,4]
for i in l:
    print(i,end=" ")

l=[5,1,2,8,4]
for i in range(0,len(l)):
    print(i,end=" ")

l1=[1,2,3,4,5,6]
for i in l1:
    l1.remove(i)
print(l1)
"""
"""l=input().split()
res=[]
for i in l:
    if(i not in res):
        res.append(i)
print(res)
"""
l=list(map(int,input().split()))
res=[]
for i in l:
    if i not in res and l.count(i)%2!=0:
        res.append(i)
print(res)


l=input().split()
l.sort()
res=[]
for i in l:
    if i%2!=0:
        res.append(i)
    else:
        res.insert(0,i)
print(res)
