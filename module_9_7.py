def is_prime(sum_three):
    def wrapper(*args, **kwargs):
        result = sum_three(*args, **kwargs)
        if result % 2 == 0 or result % 3 == 0:
            print('Составное')

        elif result % result ** 0.5 == 0:
            print('Составное')

        else:
            print('Простое')
            return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(9, 3, 6)
print(result)
