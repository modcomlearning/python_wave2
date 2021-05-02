# a data type - stores multiple values in a single variable
# a list can be changed
programs = ['IT','Business','Management','Tours','Hositality','Theology']
print(programs)
print(programs[2])

programs.append('Engineering')
programs.remove('IT')

for program in programs:
    print(program)

# difference between a list and a tuple
# a list uses []
# a tuple used the brackets ()

# a tuple cannot changed once defined
# a list can be changed ...