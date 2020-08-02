import os

print('start')
secrets_test_key = os.getenv('secrets.TEST_KEY')
print(f'stk: {secrets_test_key}')
test_key = os.getenv('TEST_KEY')
print(f'tk: {test_key+"3"}')
print('end')
