#7. Write a Python script to remove all non int values from a list.
l1=[10,50,"Java",40,"C",90,"Python",70,12.8,5.6,60,"MySirG"]
l2=[]
for i in l1:
    if(type(i)==int):
        l2.append(i)
li=l2
print(l2)

