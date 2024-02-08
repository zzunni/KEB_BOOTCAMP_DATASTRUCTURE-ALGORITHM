import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"time elapse: {end - start}")
        return result
    return wrapper


# def factorial(number) -> int :
#   '''
#    factorial by reprtition
#    :param number: number (int)
#    :return: factorial result (int)
#    '''
#    result = 1
#    for i in range(1, number+1):
#        result = result * i
#    return result

def factorial(number) -> int:
    '''
    factorial by recursion
    :param number: number (int)
    :return: factorial result (int)
    '''
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


@timer
def nCr(n, r) -> int : # SRP, OCP violation
    '''
    combination
    :param n:
    :param r:
    :return: 경우의 수
    '''
    numerate = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return int(numerate / denominator)

#위의 조합 함수는 단일책임법칙 위반, 데코레이터 함수 필요

