import random

def random_float(min_value, max_value):
    return random.uniform(min_value, max_value)

# Использование функции
min_val = 1
max_val = 15
print(f"Случайное число с плавающей точкой между {min_val} и {max_val}: {random_float(min_val, max_val)}")
