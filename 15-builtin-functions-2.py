numbers = [100, 52, 69, 87, 85, 639]

result_list = filter(lambda x: x >= 100, numbers)

# for i in result_list:
#     print(i)


map_result = map(lambda x: x ** 2, range(15))

for n in map_result:
    print(n)
