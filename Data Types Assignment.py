#Question1
b=[]
a=input("Enter the input for list")
b.append(a)
f=input("Enter the input for list ")
b.append(f)
print("The list is",b)

#Question2
c=['google','apple','facebook','microsoft','tesla']
d=c+b
print(d)

#Question3
e=[1,1,2,6,4,1]
print(e.count(1))

#Question4
m=[3,8,1]
m.sort()
print(m)

#Question5
x=[7,8,9]
y=[2,3,4]
x.sort()
y.sort()
z=x+y
z.sort()
print(z)

#Question6
#Implementing stack
n=[1,2,3,4,5]
n.pop()
print(n)
n.append(2)
print(n)

#Question7
even=[]
odd=[]
for num in range(1,31):
    if num%2 ==0:
        even.append(num)
    else:
        odd.append(num)
print(even)
print(odd)
print(len(even))
print(len(odd))
