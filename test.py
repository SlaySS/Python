
def log_function(func):
    def wrap():
        print(f'Start {func}')
        func()
        print(f'End {func}')
    return wrap


@log_function
def hello():
    print('Hello')


hello()
