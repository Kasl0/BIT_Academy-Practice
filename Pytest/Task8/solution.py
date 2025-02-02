def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def function(n):
    n += 1
    while is_prime(n) == False:
        n += 1
    return n