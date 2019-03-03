# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

hrs = input("Enter Hours:")
h = float(hrs)
rate = 10.50

if h <= 40:
  pay = h * rate
elif h > 40
  pay = h * rate * 1.5

# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
score = input("Enter Score: ")
score = float(score)

if score >= 0.9 :
  print('A')
elif score >= 0.8 :
  print('B')
elif score >= 0.7 :
  print('C')
elif score >= 0.6 :
  print('D')
elif score < 0.6 :
  print('F')
else :
  print('Aj-oh')

# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and 1.5 for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number.

hrs = input("Enter Hours:")
hrs = float(hrs)

rt = input("Enter Rate:")
rt = float(rate)

def computepay(hours,rate):
    if hours <= 40 :
      pay = hour * rate
    elif hours > 40 :
      pay = 40 * rate + (hours - 40) * rate * 1.5
    return pay

computepay(hrs, rt)

# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" : break

    try:
      num = int(num)
    except:
      print("Invalid input")

    if largest is None
      largest = num
    elif num > largest
      largest = num
    elif num < smallest
      smallest = num

print("Maximum", largest)
print("Minimum", smallest)
