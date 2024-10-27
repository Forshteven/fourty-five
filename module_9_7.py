def is_prime(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
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

@is_prime
def multiple_three(a, b, c):
    return a * b * c

result = sum_three(4, 3, 6)
print(result)

result2 = multiple_three(1, 1, 7)
print(result2)