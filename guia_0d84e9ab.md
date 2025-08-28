# Funciones continuas

## Definición
Una función f es continua en un punto x₀ si el límite de f(x) cuando x tiende a x₀ es igual a f(x₀). [PAG 1]  Formalmente: lim_(x→x₀) f(x) = f(x₀).  Esto significa que la función no presenta "saltos" o "agujeros" en el punto x₀.  La gráfica de una función continua se puede dibujar sin levantar el lápiz del papel.

## Ejemplo sencillo (paso a paso)
- **Planteamiento:** Determinar si la función f(x) = 2x + 1 es continua en x₀ = 3.
- **Desarrollo:**
    1. Calculamos f(x₀): f(3) = 2(3) + 1 = 7.
    2. Calculamos el límite de f(x) cuando x tiende a 3: lim_(x→3) (2x + 1) = 2(3) + 1 = 7.
- **Resultado:** Dado que lim_(x→3) f(x) = f(3) = 7, la función f(x) = 2x + 1 es continua en x₀ = 3. [PAG 1]

## Ejemplo avanzado (paso a paso)
- **Planteamiento:** Determinar si la función f(x) = (x² - 1)/(x - 1) es continua en x₀ = 1.
- **Desarrollo:**
    1. Observamos que f(1) no está definida, ya que se produce una división por cero.
    2. Calculamos el límite de f(x) cuando x tiende a 1: lim_(x→1) (x² - 1)/(x - 1) = lim_(x→1) (x + 1)(x - 1)/(x - 1) = lim_(x→1) (x + 1) = 2.
- **Resultado:** Aunque el límite existe y es igual a 2, f(1) no está definida. Por lo tanto, la función f(x) no es continua en x₀ = 1. [PAG 1]  Si definimos f(1) = 2, entonces la función sería continua en x₀ = 1.

## 3 ejercicios propuestos
1) Determinar si la función f(x) = x³ - 2x + 1 es continua en x₀ = 0.
2) Determinar si la función f(x) = |x| es continua en x₀ = 0.
3) Determinar si la función f(x) = (x² - 4)/(x + 2) es continua en x₀ = -2.

## Soluciones
- **Ejercicio 1:** f(0) = 0³ - 2(0) + 1 = 1. lim_(x→0) (x³ - 2x + 1) = 1.  Como f(0) = lim_(x→0) f(x) = 1, la función es continua en x₀ = 0.
- **Ejercicio 2:** f(0) = |0| = 0. lim_(x→0) |x| = 0. Como f(0) = lim_(x→0) f(x) = 0, la función es continua en x₀ = 0.
- **Ejercicio 3:** f(-2) no está definida. lim_(x→-2) (x² - 4)/(x + 2) = lim_(x→-2) (x - 2)(x + 2)/(x + 2) = lim_(x→-2) (x - 2) = -4.  Como f(-2) no está definida, la función no es continua en x₀ = -2. Si definimos f(-2) = -4, entonces la función sería continua en x₀ = -2.