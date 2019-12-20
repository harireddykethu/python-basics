# https://docs.python.org/3/library/stdtypes.html?highlight=range#range

# using range(end)

for i in range(100):
    print(i)


# using range(start, end, step)

for i in range(1, 50, 3):   # range(step = 3, end = 50, start=1)
    print(i)


x = -1.2

print('-------------------------')
print(abs(x))

for name in dir():
    print(name)

number_list = [1, 2, 3, 4, 0]
print(len(number_list))

# string is a collection

title = 'Hi there friends!'

for ch in title:
    print(ch)


print('-------------------------')
print(title[5:9])
