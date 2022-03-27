def my_function(a, b, c, d, e):
    return a + b + c


returned_value = my_function(1, 5, -3, 'abc', [12, 56, 'cad'])
print('sum of numbers =', returned_value)


def my_function(a, b, c, d, e):
    return 0


print(my_function(1, 5, -3, 'abc', [12, 56, 'cad']))


def my_function(a, b, c, param_1):
    return a + b


returned_value = my_function(2, 4, 'abc', param_1=2)
print('sum of numbers =', returned_value)


def s(n):
    if n == 0:
        return n
    return n + s(n - 1)


result = s(10)
print(f'sum of 10 =', result)


def s(n):
    if n == 0:
        return n
    if n % 2 == 1:
        return s(n - 1)
    return n + s(n - 1)


result = s(10)
print(f'sum of even of 10 =', result)


def s(n):
    if n == 0:
        return n
    if n % 2 == 0:
        return s(n - 1)
    return n + s(n - 1)


result = s(10)
print(f'sum of odd of 10 =', result)


def work():
    while True:
        try:
            data = int(input("Enter an integer: "))
            print("You entered: ", data)
            break
        except ValueError as e:
            data = 0
            print('This is not an integer:', data)
            break


work()

