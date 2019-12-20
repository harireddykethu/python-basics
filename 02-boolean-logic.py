x = True
y = False

# Or operator
if x or y:
    print(f'Logical OR operator: {x} or {y}')

# And operator
if x and y:
    print('I don\'t see this')
else:
    print(f'Else block for {x} and {y}')

# Not operator
if not y:
    print('Inverting y')

# Complex expression
if (x or y) and (not y):
    print('Learning complex boolean expressions')


# Operators:

a = 100
b = 70

if (a >= 90) and (b != 60):
    print('Comparison operators')

# Available operators: ==, >, <, >=, <=, !=


# if elif else

x = 100

# No switch construct in Python
if x > 100:
    print(f'x > {100}')
elif x > 70:    # not else if
    print(f'x > {70}')
else:
    print(f'x <= {70}')

# In any suite, pass can be used to take no action
