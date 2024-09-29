number= input("Enter numbers seperated by a single space")
number=number.split(" ")
x= len(number)
print(x)
number=[int(i) for i in number]
sum=sum(number)
print("The sum is" + str(sum))
