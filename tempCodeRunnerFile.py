def odd(num):
    res=0
    for i in num:
        res=res^i
    return res
    
num=[10,11,11,10,12,12,12,1,1,1]

print(odd(num))