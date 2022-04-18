from time import time

def timer(function):
    def wrapper(*args, **kwargs):
        start = time()
        function(*args, **kwargs)
        end = time()
        print(f'It took {(end-start):.3f} seconds')

    return wrapper

@timer
def main_func():
    for i in range(1000000):
        continue

main_func()