def sum(*result,**param):
    n = 0
    for number in result:
        if type(number) in (int, float,):
            n = n + number
    return n


print(sum(1,4.3, 5, -3, 'abc', [12, 56, 'cad'],param_1=2))


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
        try:
            data = int(input("Enter an integer: "))
            print("You entered: ", data)
        except ValueError as e:
            data = 0
            print('This is not an integer:', data)


work()

