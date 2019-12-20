def api_function():
    raise Exception('Manually raising an exception')
    return 100 / 10


try:
    result = api_function()
    print(f'Result: {result}')

except ZeroDivisionError as zde:
    print(f'Zero Division Exception handled: {zde}')
except ValueError as ve:
    print(f'Value Error handled: {ve}')
except Exception as e:
    print(f'Exception: {e}')
finally:
    print('Finally')
