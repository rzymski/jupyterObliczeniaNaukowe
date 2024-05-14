import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')


def t1(func, Nn, x0):
    skladowe = []
    szeregTaylora = 0

    for n in range(Nn + 1):
        pochodna = sp.diff(func, x, n)
        pochodnaX = pochodna.subs(x, x0)
        skladowa = pochodnaX / sp.factorial(n) * ((x - x0) ** n)
        skladowe.append(skladowa)
        szeregTaylora += skladowa

    funcLambda = sp.lambdify(x, func, modules=['numpy'])
    taylorLambda = sp.lambdify(x, szeregTaylora, modules=['numpy'])
    skladoweLambda = [sp.lambdify(x, sklad, modules=['numpy']) for sklad in skladowe]

    plt.figure(figsize=(10, 6))
    x_vals = np.linspace(-4, 4, 400)
    # Wykres funkcji f(x)
    plt.plot(x_vals, funcLambda(x_vals), label='f(x)')

    # Wykres N-tego przybliżenia funkcji f(x) szeregiem Taylora
    plt.plot(x_vals, taylorLambda(x_vals), label=f'N-te przybliżenie (N={Nn})')

    # Wykres składowych N-tego przybliżenia
    for i, sklad in enumerate(skladoweLambda):
        plt.plot(x_vals, sklad(x_vals), linestyle='--', label=f'a{i}(x)')

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Przybliżenie funkcji szeregiem Taylora')
    plt.grid(True)
    plt.show()

    return skladowe, szeregTaylora


# Przykładowe użycie
t1(sp.sin(x), 5, 0)
