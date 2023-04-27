#Coeficientes
a = float(input('Coeficiente a: '))
b = float(input('Coeficiente b: '))
c = float(input('Coeficiente c: '))
Delta = b**2 - 4 * a * c
x1 = (-b + Delta**0.5) / (2 * a)
x2 = (-b - Delta**0.5) / (2 * a)
print('Os Coeficientes são: ', a, b, c)
print('Delta = ', Delta)
print('Soluções: x1 = ', x1, 'x2 = ', x2)