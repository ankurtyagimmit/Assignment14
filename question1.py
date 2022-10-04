#1. Write a Python script to create a list of first N natural numbers
n=int(input("Enter any digit:"))
def createList(n):
    lst = []
    for i in range(n+1):

            lst.append(i)
    return(lst)

print(createList(n))
