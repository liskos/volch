def gipot(a, b):
    """функция с параметрами и возвращающая результат,
       гипотенузу в прямоугольном треугольнике с катетами a и b"""
    c = a * a + b * b
    return c ** 0.5


print(gipot(3, 4))
