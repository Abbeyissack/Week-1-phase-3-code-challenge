def add_numbers(num1, num2):
    sum = num1+num2

    return sum


print(add_numbers(5, 5))


def is_even(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is not even")


is_even(4)


def reverse_string(text):

  return text[-1]


print('reverse_string')


def count_vowels(text):
    vowels = 'aeiou'
    text = text.lower()
    return sum(1 for char in text if char in vowels)


print('count_vowels')


def calculate_factorial(n):
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)


print('calculate_factorial')


def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper


def apply_decorator(func):
    return decorator_func(func)


print('decorator_func')


def sort_by_age(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])


print('sort_by_age')


def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged


print('merge_dicts')


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")



        print()

car = Car('Toyota', 'Hilux', 2000)

car.display_info()






    

