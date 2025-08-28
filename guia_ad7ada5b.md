# Funciones continuas

## Definición
Una función f es continua en un punto x₀ si el límite de f(x) cuando x tiende a x₀ es igual a f(x₀). [PAG 1]
Formalmente: lim_(x→x₀) f(x) = f(x₀).  Esto significa que la función no presenta "saltos" o "agujeros" en el punto x₀.  La función se acerca al mismo valor tanto por la izquierda como por la derecha de x₀, y ese valor coincide con f(x₀).

## Ejemplo sencillo (paso a paso)
- **Planteamiento:** Determinar si la función f(x) = 2x + 1 es continua en x₀ = 3.
- **Desarrollo:**
    1. Calculamos f(x₀): f(3) = 2(3) + 1 = 7.
    2. Calculamos el límite de f(x) cuando x tiende a 3: lim_(x→3) (2x + 1) = 2(3) + 1 = 7.
- **Resultado:** Dado que lim_(x→3) f(x) = f(3) = 7, la función f(x) = 2x + 1 es continua en x₀ = 3.

## Ejemplo avanzado (paso a paso)
- **Planteamiento:** Determinar si la función f(x) = (x² - 1)/(x - 1) es continua en x₀ = 1.
- **Desarrollo:**
    1.  Si intentamos calcular f(1) directamente, obtenemos una indeterminación 0/0.
    2.  Simplificamos la función: f(x) = (x-1)(x+1)/(x-1) = x+1 para x ≠ 1.
    3.  Calculamos el límite de f(x) cuando x tiende a 1: lim_(x→1) (x+1) = 1+1 = 2.
- **Resultado:** Aunque f(1) no está definida, el límite de f(x) cuando x tiende a 1 existe y es igual a 2.  Por lo tanto, la función presenta una discontinuidad evitable en x₀ = 1.  Podríamos redefinir la función como f(x) = x+1 para todo x, y entonces sería continua en x₀ = 1.


## 3 ejercicios propuestos
1) Determinar si la función f(x) = |x| es continua en x₀ = 0.
2) Determinar si la función f(x) = {x si x<1; 2 si x=1; x+1 si x>1} es continua en x₀ = 1.
3) Determinar si la función f(x) = 1/x es continua en x₀ = 0.

## Soluciones
- **Ejercicio 1:**  El límite por la izquierda es lim_(x→0⁻) |x| = lim_(x→0⁻) -x = 0. El límite por la derecha es lim_(x→0⁺) |x| = lim_(x→0⁺) x = 0.  f(0) = |0| = 0.  Como los límites laterales y f(0) coinciden, la función es continua en x₀ = 0.
- **Ejercicio 2:** El límite por la izquierda es lim_(x→1⁻) x = 1. El límite por la derecha es lim_(x→1⁺) (x+1) = 2.  f(1) = 2.  Como los límites laterales no coinciden, la función no es continua en x₀ = 1.
- **Ejercicio 3:** f(0) no está definida. Además, los límites laterales en x₀ = 0 tienden a infinito (lim_(x→0⁻) 1/x = -∞ y lim_(x→0⁺) 1/x = ∞). Por lo tanto, la función no es continua en x₀ = 0.