

start = 0
while start < 10:
    # do code to be repeated here, bmi here
    weight = float(input('Your Weight in kgs'))
    height = float(input('Your Height in meters'))
    bmi = weight/pow(height, 2)
    print('BMI is ', bmi)
    print()
    start = start + 1  # increment/update