# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def pow_rec(a,b):
    if b == 0:
        return 1
    return  pow_rec(a,b - 1) * a

num_A = int(input('A: '))
num_B = int(input('B: '))
print(f'A в степени B равно: {pow_rec(num_A,num_B)}')