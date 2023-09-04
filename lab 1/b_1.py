def gcd(a, b):
    result = max([i if (a % i == 0) and (b % i == 0) else 0 for i in range(1, min(a, b) + 1)])
    return result


if __name__ == '__main__':
    print('4105 and 10:', gcd(4105, 10))
    print('4539 and 6:', gcd(4539, 6))
