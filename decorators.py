def log_decorator(func):
    def wrap():
        print(f'Calling func {func}')
        func()
        print(f'Func {func} finished work')
    return wrap

@log_decorator
def printhello():
    print('Hello')

printhello()
print(help(printhello))

#чтобы прокидывались все свойства от основной функции надо импортировать декоратор @wraps
from functools import wraps

def log_decorator2(func):
    @wraps
    def wrap(*args, **kwargs):
        print(f'Calling func {func}')
        func()
        print(f'Func {func} finished work')
    return wrap

@log_decorator2
def printhello():
    print('Hello')

print(help(printhello))