#3. Write a Python script to create a list of first N even natural numbers.
N=int(input("Enter any digit:"))
a=2
li=[]
for i in range(a,N+1):
    li.append(i)
# printing odd numbers using the lambda function
even= list(filter(lambda x: (x%2==0),li)) 
print(even)
