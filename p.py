from sympy import symbols, Function, dsolve, Eq, exp

# Definicja zmiennych i funkcji
x = symbols('x')
y = Function('y')

yPrim = y(x).diff(x)

# Definicja równania różniczkowego
diffEq = Eq(yPrim, 2 * y(x) + exp(x) - x)

# Warunek początkowy
initialCondition = {y(0): 1 / 4}

# Rozwiązanie równania różniczkowego
solution = dsolve(diffEq, y(x), ics=initialCondition)
solution = solution.simplify()

print(solution)

points = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
values = [solution.rhs.subs(x, p) for p in points]

for p, v in zip(points, values):
    print(f'y({p}) = {v}')


# diffEq2 = Eq(yPrim, x - 1 + (x + 1) * y(x))
diffEq2 = Eq(y(x).diff(x) - (x + 1)*y(x), x - 1)
initialCondition2 = {y(0): 0}
solution2 = dsolve(diffEq2, y(x), ics=initialCondition2)
solution2 = solution2.simplify()
print(solution2)

values2 = [round(solution2.rhs.subs(x, p).evalf(10), 5) for p in points]

for p, v in zip(points, values2):
    print(f'y({p}) = {v}')
