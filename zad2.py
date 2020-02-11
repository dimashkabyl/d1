#а,б листндағы бар элементтерді жана листке шығару 
a=[1,2,3,4,5,9,11,45,99]
b=[1,45,99,55,63,78,87,]
result=[]
for i in a:
    if i in b:
        result.append(i)
print(result)