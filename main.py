import time
print("Please input the numbers your would like to multiply below :)")
number1 = input("Type your first number: ")
number2 = input("Type your second number: ")
answer = int(number1)*int(number2)
print("Thank you, calculating...")
time.sleep(1.5)
print("Your answer is " + str(answer))
