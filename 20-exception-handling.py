def api_function():
    country = 'India'
    return country[100]


try:
    result = api_function()
    print(f'Result: {result}')

except ZeroDivisionError as zde:
    print(f'Zero Division Exception handled: {zde}')
except ValueError as ve:
    print(f'Value Error handled: {ve}')
except IndexError as ie:
    print(f'Index Error handled: {ie}')
except Exception as e:
    print(f'Exception: {e}')
finally:
    print('Finally')
