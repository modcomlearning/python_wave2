
marks = float(input('Enter Marks: '))

if marks < 0 or marks > 100:
    print('Invalid')

elif marks >= 0 and marks < 30:
    print('You got below average')

elif marks >=30 and marks < 48:
    print('You got an average mark')

elif marks >= 48 and marks < 70:
    print('You have an above average')

elif marks >=70 and marks <=100:
    print('Excellent!')