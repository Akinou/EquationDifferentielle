import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def f(x, y):
    """
    Cette fonction dépend de la nature de l'équation différentielle à résoudre.
    Elle doit être définie pour chaque équation différentielle spécifique.
    """
    pass

def solve_ode(f, method, y0, x_span):
    """
    Cette fonction résout une équation différentielle donnée par la fonction f,
    en utilisant la méthode numérique spécifiée par la variable method,
    avec les conditions initiales y0 et l'intervalle de temps x_span.
    """
    if method == "Euler":
        sol = solve_ivp(f, x_span, y0, method='Euler')
    elif method == "RK4":
        sol = solve_ivp(f, x_span, y0, method='RK45')
    elif method == "BDF":
        sol = solve_ivp(f, x_span, y0, method='BDF')
    else:
        raise ValueError("La méthode numérique spécifiée n'est pas prise en charge.")
    
    return sol

def plot_solution(sol):
    """
    Cette fonction trace la solution de l'équation différentielle obtenue
    à l'aide de la fonction solve_ode.
    """
    plt.plot(sol.t, sol.y[0])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

# Exemple d'utilisation

# Equation différentielle : y' = -x^2 + y
def f(x, y):
    return -x**2 + y

# Conditions initiales : y(0) = 1
y0 = [1]

# Intervalle de temps : x ∈ [0, 1]
x_span = [0, 1]

# Résolution de l'équation différentielle avec la méthode d'Euler
sol = solve_ode(f, "Euler", y0, x_span)

# Tracé de la solution
plot_solution(sol)
