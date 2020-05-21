def wrap_log(func):
    def wrap():
        print('Start')
        func()
        print('End')

    return wrap


@wrap_log
def printhello():
    print('Hello')


a = [1, 2, 3, 4, 5]
b = [6, 0, 8, 9]
a += b
c = sorted(a)
print(a)
print(c)
a.sort()
print(a)
