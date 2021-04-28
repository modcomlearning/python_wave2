

# bmi without a loop
for x in range(0, 10, 1):
    weight = float(input('What is your weight in kgs:'))
    height = float(input('What is your height in meters:'))
    bmi = weight/pow(height, 2)
    print('BMI is ', bmi)
    print()

#  for will always stop at some point