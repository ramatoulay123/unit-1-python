

number1_input = float(input("Enter the first number: "))
number2_input = float(input("Enter the second number: "))  
# A list of the different operations the user can reference 
print("choose an aperation")
print("1. Addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
print("5. exponents")
print("6. floor division")
print("7. remainder") 
# They input the number of the operator 
operation = int(input("enter an operation from 1 to 7: ")) 
# Calculation for the addition 
if operation == 1:
    result = number1_input + number2_input 
    print(result)
# calculation for subtraction 
elif operation == 2:
    result2 = number1_input - number2_input
    print(result2) 
# calculation for multiplication 
elif operation == 3:
    result3 = number1_input * number2_input 
    print(result3) 
# calculation for division 
elif operation == 4: 
    result4 = number1_input / number2_input 
    print(result4)
# calculation for exponents 
elif operation == 5: 
    result5 = number1_input ** number2_input
    print(result5) 
# calculation for floor division
elif operation == 6:
    result6 = number1_input // number2_input
    print(result6)
# calculation for remainder 
elif operation == 7: 
    result7 = number1_input % number2_input
    print(result7)

