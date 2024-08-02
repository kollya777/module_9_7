def is_prime(func):
    def wrapper(*args):
        x = func(*args)
        k = 0
        for i in range(2, (x//2)+1):
            if x % i == 0:
                k += 1
        if k == 0:
            print("Простое")
        else:
            print("Составное")
        return x
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)