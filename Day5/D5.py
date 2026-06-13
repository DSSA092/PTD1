"""lis=list(map(int,input().split()))
k=int(input())#sum where it is checked
r,l,s,m=0,0,0,0
while r<len(lis):
    s+=lis[r]
    while s>k:
        s-=lis[l]
        l+=1
    length=r-l+1
    m=max(m,length)
    r+=1
print(m)

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        s=sum(cardPoints[:k])
        m=s
        for i in range(k):
            s=s-cardPoints[k-1-i]+cardPoints[n-1-i]
            m=max(m,s)
        return m

"""
"""lis=input("Enter password:")
upper,lower=0,0
s,a,l,d=0,0,0,0
for ch in lis:
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower+=1
    elif ch.isdigit():
        d+=1
    elif not ch.isalnum() and not ch.isspace():
        s+=1

if(len(lis)>=8) and upper>0 and lower>0 and d>0  and s>0 :
    print("Valid")
else:
    print("Not Valid")
"""

#Searching:
# Linear Search  ->TimeComplexity -O(n)


s=input()
c,k=1,0
res=""
for i in range(1,len(s)):
    if s[k]==s[i]:
        c+=1
    else:
        res+=s[i-1]+str(c)
        k=i
        c=1
res+=s[-1]+str(c)
print(res)