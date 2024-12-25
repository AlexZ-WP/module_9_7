def is_prime(func):
    def true_prime(*args, **kwargs):
        number = func(*args, **kwargs)
        if number < 2:
            print("Составное")
            return number
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
               print("Составное")
               break

        else:
            print("Простое")
        return number
    return true_prime


@is_prime
def sum_three(*args):
   return sum(args)

result = sum_three(2, 3, 6)
print(result)