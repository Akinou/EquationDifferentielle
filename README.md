# EquationDifferentielle
Ce script utilise la bibliothèque scipy et permet de résoudre les équations différentielles du premier ordre sous la forme y' = f(x, y), où f est une fonction dépendant de x et y.


Le script est conçu pour résoudre des équations différentielles du premier ordre de la forme y' = f(x, y), où f est une fonction dépendant de x et y. Le script utilise la bibliothèque scipy pour résoudre numériquement les équations différentielles.

La fonction solve_ode est la fonction principale qui résout l'équation différentielle. Elle prend quatre arguments :

f : la fonction qui définit l'équation différentielle à résoudre.
method : la méthode numérique à utiliser pour résoudre l'équation différentielle. Le script prend en charge trois méthodes : la méthode d'Euler, la méthode de Runge-Kutta d'ordre 4 (RK4) et la méthode de différences finies à backward differentiation formula (BDF).
y0 : les conditions initiales de l'équation différentielle, c'est-à-dire la valeur de y pour une valeur initiale de x.
x_span : l'intervalle de temps sur lequel l'équation différentielle doit être résolue.
La fonction solve_ode utilise la méthode numérique spécifiée pour résoudre l'équation différentielle et renvoie la solution sous la forme d'un objet scipy.integrate.OdeResult.

La fonction plot_solution est utilisée pour tracer la solution de l'équation différentielle obtenue à l'aide de la fonction solve_ode. Elle prend en entrée un objet OdeResult et trace la solution y en fonction de x.

Pour utiliser le script pour résoudre une équation différentielle spécifique, vous devez d'abord définir la fonction f pour l'équation différentielle. Ensuite, vous devez définir les conditions initiales y0 et l'intervalle de temps x_span pour l'équation différentielle. Enfin, vous devez appeler la fonction solve_ode avec la méthode numérique souhaitée et les arguments appropriés. 
La fonction solve_ode renverra un objet OdeResult, que vous pouvez passer à la fonction plot_solution pour tracer la solution de l'équation différentielle.
