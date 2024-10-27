def is_prime(sum_three):
    def wrapper(*args, **kwargs):
        result = sum_three(*args, **kwargs)
        for i in range(2, result):
            if result % i:
                print('Простое')
                return result
            else:
                print('Cоставное')
                break
    return wrapper

@is_prime
def sum_three(a,b,c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)