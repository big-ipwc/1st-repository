from math import sqrt
print("Введите число, чтобы проверить, является ли оно числом Фибоначчи:")
print('Введите "-1", чтобы завершить выполнение программы')
num = 1

while True:
    num = int(input())

    def is_fib(n):
        return sqrt(5 *(n**2) + 4) % 1 == 0 or sqrt(5 * (n**2) - 4) % 1 == 0

    if num == -1:
        break
    
    print(is_fib(num))
    
    

    
