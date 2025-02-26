# 1
# Checking Discounts Based on Age
# A store offers discounts based on the age of the customer:

# Kids (under 12): 50% discount
# Seniors (60 and above): 30% discount
# Others: No discount

your_cart = float(input('What is your amount of cart: '))
age = int(input('how old are you? '))
if age < 12:
  print(your_cart*0.5)
elif age > 60:
  print(your_cart*0.7)
else:
  print(f'The amount which you should pay: {your_cart}')

# 2
# Validating a Password
# A system requires a user to enter a password, and it checks if the password matches a predefined value.

stored_password = "secure123"

password = str(input('Enter your password: '))

if password == "secure123" :
  print('The password is entered correctly')
else:
  print('The password is entered incorrectly,try again')

#3
# Grading System Based on Marks
# Calculate a student's grade based on their score:

# 90 and above: A
# 80–89: B
# 70–79: C
# Below 70: F
your_score = int(input('What is your score in exam? '))
if your_score<70:
   print('You should study more!')
elif 70<your_score<79:
   print('Not bad')
elif 80<your_score<89:
   print('Good Job') 
elif your_score>90:
   print('Great Job')
else:
 print('Nothing')

#4
# ATM Withdrawal
# An ATM allows withdrawal only if:

# The amount is a multiple of 10.
# The account has sufficient balance.

account_balance = int(input('What is the balance in your card: '))
if account_balance % 10 == 0 and account_balance >= 10:
  print('The balance of account is approved, you can withdraw')
elif account_balance % 10 != 0:
  print('The amount should be a multiple of 10')
elif account_balance <= 10:
  print('There is not sufficient balance')
else: 
  print('smth')

# 5
# Traffic Light System
# Simulate actions based on traffic light colors.

traffic_light = input("The color of traffic light: ")

if traffic_light == 'Red':
 print('Stop')
elif traffic_light == 'Green':
 print('Go')
elif traffic_light == 'Yellow':
 print('Get ready')
else:
  print('Nothing')

# 6

# Even or Odd Numbers
# Determine whether a number is even or odd.

num = int(input('Write a random number: '))

if num % 2 == 0:
  print(f'{num} is even')
else:
  print(f'{num} is odd')

# 7

# BMI Calculator
# Calculate Body Mass Index (BMI) and provide health feedback.

your_weight = float(input('What is your weight(in kilograms)? '))
your_height = float(input('What is your height(in meters)? '))
bmi = your_weight / (your_height**2)
if bmi < 18.5:
    print("Underweight") 
elif 18.5 <= bmi < 24.9:
    print("Normal weight") 
elif 25 <= bmi < 29.9:
    print("Overweight")
else:
    print("Obesity")

#8

# Weather Advice
# Give advice based on the temperature.

t_temp = float(input('Write today\'s temperature: '))

if t_temp < 0:
    print('Advice: wearing very warm clothes')
elif 0< t_temp <= 10:
    print('Advice: wearing a jacket and warm pants')
elif 10 < t_temp <= 20:
    print('Advice: light warm clothing')
elif 20 < t_temp <= 30:
    print('Advice: It\'s okay to wear light clothes')
else:
    print('Advice: Don\'t wear warm clothes')
# 9

# Online Shopping Cart
# Check if the user qualifies for free shipping:

# Free shipping for orders above $50.

amount_of_order = float(input('Write your amount of order: '))
if amount_of_order < 50:
 print('You can\'t use free shipping option, you should order more 50$')
else:
 print('You can use free shipping')

# 10

# Banking System: Check Account Type
# Provide benefits based on the account type:

# Savings: 4% interest
# Current: No interest
# Fixed Deposit: 6% interest

benefit = str(input('Write your type of account: '))
 
if benefit == 'Savings':
  print('4% interest')
elif benefit == 'Current':
  print('No interest')
elif benefit == 'Deposit':
  print('6% interest')
else:
  print('We don\'t have this type of account')

# 11

# Grade-Based Access
# Allow students access to certain benefits based on their grade.

grade=float(input('tell me your final exam grade'))
if grade>=91:
    print('Your grade is amazing, keep study smart')
elif grade>=80:
    print('not bad, but you should study harder')
elif grade>=56:
    print('You passed exam, but it\'s not good result, you should study hard')
else: 
    print('you must re-take in exam when you will be ready for exam')
