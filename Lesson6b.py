

# create a function that finds simple interest
def simple_interest():
    principle = 50000
    rate = 1.5
    time = 6

    si = (principle * rate *time)/100
    print('Simple interest is ', si)


#simple_interest() # call

# another
def area():
    radius = 0
    answer = 3.14 * radius * radius
    print('Area is ', answer)

    if answer == 0:
        print('Invalid')

    else:
        print('The area is valid')

# area()


