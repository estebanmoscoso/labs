def is_prime(k):
    from math import sqrt
    for i in range(2, int(sqrt(k))+1):
        if k % i == 0:
            return False
    return True


if __name__ == '__main__':
    for n in range(2, 1001):
        if is_prime(n):
            print(n, end=' ')
