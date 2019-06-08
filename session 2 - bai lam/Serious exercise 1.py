#1.	Write a program that asks user their height (cm) and weight (kg), and then calculate their BMI (Body Mass Index):

H = int(input('Please input your height in cm: '))/100
W = int(input('Please input your weight: '))
if W/(H**2) < 16:
    print('Severely underweight')
elif W/(H**2) < 18.5:
    print('underweight')
elif W/(H**2) < 25:
    print('Normal')
elif W/(H**2) < 30:
    print('Overweight')
else:
    print('Obese')