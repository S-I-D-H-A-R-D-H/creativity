"""this is the file of codes that i typed on my own!!!"""


def list_asc_sort(l):
    """assign a list to sort it in ascending order."""
    n = 0
    for i in range(len(l)):
        n = 0
        for j in l:
            if l[i] < j:
                l[i], l[n] = l[n], l[i]
            n += 1


def list_dec_sort(l):
    """assign a list to sort it in descending order."""
    n = 0
    for i in range(len(l)):
        n = 0
        for j in l:
            if l[i] > j:
                l[i], l[n] = l[n], l[i]
            n += 1


def is_prime(n):
    """assign a number to check if its a prime number."""
    if n < 2:
        print("not a prime number.")
        return None
    for i in range(2, n // 2):
        if n % i == 0:
            print("not a prime number.")
            break
    else:
        print("it is a prime number.")


def range_prime(a=None, n=None):
    """enter the starting and ending range to get the prime numbers and
    number of prime numbers in the range """
    if a is None:
        a = int(input("enter the starting range: "))
    if n is None:
        n = int(input("enter the ending range: "))
    count = 0
    for i in range(a, n + 1):
        for j in range(2, (i // 2) + 1):
            if i % j == 0:
                break
        else:
            count += 1
            print(i, end=", ")
    print("\nthere are a total of {} prime numbers in the given range".format(count))


def nearest_prime(n=None):
    """assign a number to know its nearest prime."""
    if n is None:
        n = int(input("enter the number: "))
    d = n - 1
    lp = 0
    up = 2
    u = n + 1
    while d < n:
        if d < 2:
            break
        for i in range(2, (d // 2) + 1):
            if d % i == 0:
                break
        else:
            lp = d
            break
        d -= 1
    if lp > 0:
        while u > n:
            for i in range(2, (u // 2) + 1):
                if u % i == 0:
                    break
            else:
                up = u
                break
            u += 1
    if lp == 0:
        print("{} is the nearest prime to {}".format(up, n))
    elif up - n < n - lp:
        print("{} is the nearest prime to {}".format(up, n))
    elif n - lp < up - n:
        print("{} is the nearest prime to {}".format(lp, n))
    else:
        print("both {} and {} are nearest primes to {}".format(lp, up, n))
