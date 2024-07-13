




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








