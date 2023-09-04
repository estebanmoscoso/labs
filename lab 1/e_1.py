def lcrm(a, seed, c, m):
    return (a * seed+c) % m


if __name__ == '__main__':
    a = 21; seed = 35; c = 31; m = 100
    for _ in range(5):
        x_i = lcrm(a, seed, c, m)
        print(x_i, end=' ')
        seed = x_i

    a = 2175143; seed = 3553; c = 10653
    m = 1000000
    for _ in range(5):
        x_i = lcrm(a, seed, c, m)
        print(x_i, end=' ')
        seed = x_i