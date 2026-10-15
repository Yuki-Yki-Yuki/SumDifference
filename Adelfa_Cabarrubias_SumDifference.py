# Global Variables (num1 and num2)
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

def calculate_sum():
    sum = num1 + num2 # Local Variable
    print("Sum:", sum)

def calculate_difference():
    difference = num1 - num2 # Local Variable
    print("Difference:", difference)

calculate_sum()
calculate_difference()

