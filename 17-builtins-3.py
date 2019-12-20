list_numbers = [0, 2, 4566, 3322, 11223, 100, -1]

print(min(list_numbers))
print(max(list_numbers))
print(sum(list_numbers))

for line in ((n ** 3) for n in range(10)):
    print(line)
