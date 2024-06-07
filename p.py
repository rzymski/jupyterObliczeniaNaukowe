# from sympy import symbols, Function, dsolve, Eq, exp
#
# # Definicja zmiennych i funkcji
# x = symbols('x')
# y = Function('y')
#
# yPrim = y(x).diff(x)
#
# # Definicja równania różniczkowego
# diffEq = Eq(yPrim, 2 * y(x) + exp(x) - x)
#
# # Warunek początkowy
# initialCondition = {y(0): 1 / 4}
#
# # Rozwiązanie równania różniczkowego
# solution = dsolve(diffEq, y(x), ics=initialCondition)
# solution = solution.simplify()
#
# print(solution)
#
# points = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
# values = [solution.rhs.subs(x, p) for p in points]
#
# for p, v in zip(points, values):
#     print(f'y({p}) = {v}')
#
#
# # diffEq2 = Eq(yPrim, x - 1 + (x + 1) * y(x))
# diffEq2 = Eq(y(x).diff(x) - (x + 1)*y(x), x - 1)
# initialCondition2 = {y(0): 0}
# solution2 = dsolve(diffEq2, y(x), ics=initialCondition2)
# solution2 = solution2.simplify()
# print(solution2)
#
# values2 = [round(solution2.rhs.subs(x, p).evalf(10), 5) for p in points]
#
# for p, v in zip(points, values2):
#     print(f'y({p}) = {v}')

from sympy import *
from icecream import ic
x = symbols('x')
y = Function('y')(x)
func = 2 * x**2 * y + exp(x)
x0 = 2
y0 = 1

print(func)

y1 = func.subs(y, y0).subs(x, x0)

ic(y1)

ic(diff(func))

y2 = diff(func, x).subs({y: y0, x: x0,  diff(y): y1})

ic(y2)

y3 = diff(func, x, 2).subs({y: y0, x: x0,  diff(y): y1, diff(y, x, 2): y2})

ic(y3)

y4 = diff(func, x, 3).subs({y: y0, x: x0,  diff(y): y1, diff(y, x, 2): y2, diff(y, x, 3): y3})

ic(y4)

print("\n\n\n")





from sympy import symbols, Function, exp, diff, sympify
def compute_n_derivatives(func, x0, y0, N):
    # Definiujemy zmienne
    x = symbols('x')
    y = Function('y')(x)

    # Przygotowujemy listę do przechowywania wartości pochodnych
    derivatives = []

    # Pierwsza pochodna
    y1 = func.subs(y, y0).subs(x, x0)
    derivatives.append(y1)

    # Iteracyjnie obliczamy kolejne pochodne
    for n in range(1, N):
        func = diff(func, x)
        # Użyj poprzednich wartości pochodnych jako zamienników
        subs_dict = {y: y0, x: x0}
        for i in range(1, n + 1):
            ic(diff(y, x, i))
            subs_dict[diff(y, x, i)] = derivatives[i - 1]
        yn = func.subs(subs_dict)
        derivatives.append(yn)

    return derivatives
# Przykład użycia funkcji
# func = 2 * x ** 2 * y + exp(x)
# x0 = 2
# y0 = 1
# N = 7

func = 2 * y + exp(x) - x
x0 = 1 / 4
y0 = 0
N = 5

results = compute_n_derivatives(func, x0, y0, N)
for i, res in enumerate(results, 1):
    ic(f'y{i} = {res}')

# import sympy as sp
#
# # Definiujemy zmienne
# x = sp.symbols('x')
# y = sp.Function('y')(x)
#
# # Definiujemy równanie różniczkowe
# ode = sp.Eq(y.diff(x), 2*x**2*y + sp.exp(x))
#
# # Obliczamy pierwszą pochodną y'(x) przy x=2, y=1
# y_prime_value = ode.rhs.subs({x: 2, y: 1})
#
# # Obliczamy drugą pochodną y''(x) przy x=2, y=1, y'(2) = y_prime_value
# y_prime = 2*x**2*y + sp.exp(x)
# y_double_prime = sp.diff(y_prime, x).subs({x: 2, y: 1, sp.Derivative(y, x): y_prime_value})
#
# # Obliczamy trzecią pochodną y'''(x) przy x=2, y=1, y'(2) = y_prime_value, y''(2) = y_double_prime
# y_double_prime_expr = 2*x**2*sp.Derivative(y, x) + 4*x*y + sp.exp(x)
# y_triple_prime = sp.diff(y_double_prime_expr, x).subs({x: 2, y: 1, sp.Derivative(y, x): y_prime_value, sp.Derivative(y, (x, 2)): y_double_prime})
#
# print(y_prime)
# print(y_double_prime)
# print(y_triple_prime)
