
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input('Enter mode of operation: ')

if operator == '+': 
    print('The answer is' ,num1 + num2)
elif operator == '-' :
    print('The answer is',num1 - num2)
elif operator == '*':
    print('The answer is',num1*num2)
elif operator == '/':
    print('The answer is',num1/num2)
else:
    print("THis operation is not possible")


