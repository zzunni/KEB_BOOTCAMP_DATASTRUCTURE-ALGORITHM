def factorial(number) -> int :
    pass

def nCr(n, r) -> int :
    '''
    조합함수
    :param n:
    :param r:
    :return: 경우의 수
    '''

    numerate = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return numerate / denominator


if __name__ == "__main__":
    n = int(input("Input n : "))
    r = int(input("Input r : "))
    print(f"{n}C{r} = {nCr(n, r)}")
