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
    조합함수
    :param n:
    :param r:
    :return: 경우의 수
    '''
    numerate = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return int(numerate / denominator)


if __name__ == "__main__":
    # n = int(input("Input n : "))
    # r = int(input("Input r : "))
    # print(f"{n}C{r} = {nCr(n, r)}")
    f = int(input())
    print(factorial(f))
