"""
Escriba un programa que retorne un número con su valor invertido. Por ejemplo:

Input: 123456

Output: 654321

"""
n = int(input("n: "))

inverso = 0
while n > 0:
    inverso = (inverso * 10) + (n % 10)
    n //= 10

print(inverso)
