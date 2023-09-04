from math import sqrt


def is_prime(p):
    for i in range(2, int(sqrt(p))+1):
        if p % i == 0:
            return False
    return True


def mod_exp(M, e, p):
    if not is_prime(p):
        print('The number p is not prime')
    else:
        result = 1
        M = M % p  # Reduce base modulo p
        while e > 0:
            # If e is odd, multiply result by M
            if e % 2 == 1:
                result = (result * M) % p
            # Square the base and reduce e by half
            M = (M * M) % p
            e //= 2
        return result


if __name__ == '__main__':
    print('Is the result of 8^5 mod 269 equal to 219?')
    print('Yes' if mod_exp(8, 5, 269) == 219 else 'No')

    print(mod_exp(5,5,53),51)
    print(mod_exp(4,11,79),36)
    print(mod_exp(101,7,293),176)

