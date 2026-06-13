

"""traversal
temp=head
while temp.next:
    print(temp.data,end=' ')
    temp=temp.next
print(temp.data)
#or
temp=head
while temp:
    print(temp.data,end=' ')
    temp=temp.next
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node

    def display(self):
        temp=self.head
        while temp.next is not None:
            print(temp.data,end='->')
            temp=temp.next
        print(temp.data)

    def even(self):
        s=0
        temp=self.head
        while temp:
            if temp.data%2==0:
                s+=temp.data
            temp=temp.next
        return s
    def counts(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count


l1=LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.display()
s=l1.even()
print(s)
print(l1.counts())
