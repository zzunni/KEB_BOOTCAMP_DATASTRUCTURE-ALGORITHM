#def factorial(number) -> int :
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


def nCr(n, r) -> int :
    '''
    combination
    :param n:
    :param r:
    :return: 경우의 수
    '''
    numerate = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return int(numerate / denominator)

