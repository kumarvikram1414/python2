




#print hello

"""hi="Welcome to the dark side"
for i in range(1,len(hi)+1):
    
    print(hi[:i])"""


"""class squre:
    def square(self,squ):

        sqq=[]
        for i in squ:
            

            b=(i)**2
            sqq.append(b)
        return sqq

t=5
squ=[]

for i in range(0,t):
    a=int(input("Enter ;"))
    
    squ.append(a)


ma=squre()
solution=ma.square(squ)
print(solution)
"""

#find leapyear under range

"""pr=[]
a=2000
b=2024
for i in range(a,b+1):
    if i%4==0 and i%100:
        pr.append(i)
print(pr)    
"""

#finding number is pelimdrom
'''
a=['ramior','dear','wow','non']

for i in a:
    if i[::-1]==i:
        print(i)
    

    '''


#a=[66,3,2,1,22,3,22,2,34]



# for value less then b


'''
    b=10
    for i in a:
        if i <b:
        print(i)
'''
# for gretest and smallest value

'''a.sort()
print("gretest :", a[-1])
print("smallest :", a[0])
'''

#s="geekorgeeks"a=[66,3,2,1,22,3,22,2,34]

'''l1=[x for x in s if x in 'aeiou']
print(l1)

l4=[x*2 for x in range(6)]
print(l4)

l2=['geeks','ide','course','gfg']
l3=[ x for x in l2 if x.startswith('g')]
print(l3)'''

'''for x in s:
    if x in "aeiou":
        

'''

#Sum of two to target

'''b=[2,3,4,5,6,7,8,2,3]

target=10
t2=16

for i in range(len(b) - 1):

    for j in range(i+1,len(b)):
    
        if b[i]+b[j]==target:
            print([i,j])
        
        print("nothing here!")'''

'''
def get(l):
    even=(x for x in l if x%2==0)
    odd=(x for x in l if x%2!=0)

    return odd,even

l=[2,2,3,44,22,31,11,10]
odd,even=get(l)
print(odd,even)

'''

# second largest
'''def gbig(a):
    if not a:
        return None
    
    res=a[0]
    for i in range(1,len(a)):
        if a[i]>res:
            res=a[i]
            
    return res-1


a=(10,222,202,242,240,240,240,242,241)
print(gbig(a))

#print (max(a))
'''

 #check if sorted or not
'''def sorted(a):
    i=1
    while i<len(a):
        if a[i]<a[i-1]:
            return False
        i=i+1
    return True



a=[1,2,33,5]
if sorted(a):
    print('yes')
else:
    print('no')
'''

# find the odd number
# if number apperar emultiple of 2 then it's even other wise odd

'''
def odd(num):
    
    res=[]
    fi=[]

    for i in (num):
        count=num.count(i)
        if count%2!=0:
            if i in res:
                fi.append(i)
            else:
                res.append(i)
    return fi 
    # finding dupplicate
    '''
# using bit wise operetor    
'''def odd(num):
    res=0
    for i in num:
        res=res^i
    return res
    
num=[10,11,11,10,12,12,12,1,1,1]

print(odd(num))'''


#Reverse List

'''l=[11,2,2,6,66]

s=0
e=len(i)-1

while s<e:
    i[s],i[e]=i[e],i[s]
    s=s+1
    e=e-1
print(l)
    '''

#multiple list reverse

'''m=[[1,2,3],[3,2,4],[5,4,23]]

for i in m: 
    i.reverse()
    print(i)
'''


'''l=[[1,2,3],[3,2,4],[5,4,23]]
for i in l:
    s=0
    e=len(i)-1

    while s<e:
        i[s],i[e]=i[e],i[s]
        s=s+1
        e=e-1
print(l)'''



# Right rotate list 
'''
def reo(l):
    n=len(l)
    x=l[0] # store 1st value of list
    for i in range(1,n):
        l[i-1]=l[i] # left shift the list
    l[n-1]=x #add store value to list at last.

l=[10,1,20,4]
reo(l) 
print(l)'''

# Left Rotate 
'''class so:
    def rr(self,l):
        s=l[0]
        x=len(l)
        for i in range(1,x):
            l[i-1]=l[i]
        l[x-1]=s
        return l

l=[2,3,1,13]
q=so()
r=q.rr(l)
print(r)'''


'''def rr(l):
    n=2
    while n>0:
        n=n-1
        for i in range(len(l)):
            a=l.pop(0  )
            l.append(a)        
        return l
l=[2,3,1,44,12]
rr(l)
print(l)

'''

'''l=[1,2,3,4,56]
co=0
s=[]
for i in l:
    co=co+1

    for i in range(l(co)):
        a=i**2
        s.append(i)
    print(s[i])
    '''
        
    
'''nums=[4,5,6,7,0,1,2]
target=0
for i in range(len(nums)):
            if nums[i]==target:
                print(i)
            else:
                print(-1)

'''


'''n=[1,2,3,8]
re=1
for i in range(2,len(n)+1):
    re*=i
print(re)'''
    
'''# left rotate
num=[4,1,5,6,3,2,55]

for i in range(0,3):
    num.append(num.pop(0))
print(num)
'''



#reverse string

'''a='hello rom'
r=''
for i in a:
    r=i+r
    
print(r)'''

# Find smalles missing interger

num=[2,3,5,9]
 for i in range(num):




















