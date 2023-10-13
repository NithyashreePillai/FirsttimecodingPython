print("do u want to add or multipy")
print("if add say yes or to multipy say no")
print("what are the 2 numbers u want to add or multipy")
number1=input("wat is the 1st number")
number1=float(number1)
number2=input("what is no 2")
number2=float(number2)
print("do you want to add or multiply,yes=+ no=*(multiply)")
answer=input("yes or no")
if answer=="yes":
  result=number1+number2
else:
  result=number1*number2
print("ur result is",result)

