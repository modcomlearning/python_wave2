
for x in range(0, 10,1):
    marks = float(input('Enter Marks: '))
    # calculate
    if marks < 0 or marks > 100:
        print('Invalid')

    elif marks >= 0 and marks < 30:
        print('You got below average')

    elif marks >=30 and marks < 48:
        print('You got an average mark')

    elif marks >= 48 and marks < 70:
        print('You have an above average')

    elif marks >=70 and marks <= 100:
        print('Excellent!')

    else:
        print('Something went wrong..')
