#2. Write a Python script to create a list of first N odd natural numbers.
N=int(input("Enter any number:"))
a=1;
li=[]
for i in range(a,N+1):
    li.append(i)
even_num = list(filter(lambda x: (x%2!=0),li)) 
print(even_num)
