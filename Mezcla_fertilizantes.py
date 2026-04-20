#Ejercicio: mezcla de fertilizantes con scipy

#1. Importar librerias
from scipy.optimize import linprog

#2. Definir la función objetivo
# max Z = 180X1 + 220X2

c = [-180,-220]

#3.Definir restricciones
# Compuesto A: 3x1 + 4x2 <= 120
# Compuesto B: 2x1 + x2 <= 80
# Compuesto C: 5x1 + 3x2 <= 150
A = [
    [3, 4],  #Coeficientes del compuesto A requerido para el fertilizante 1 y 2 respectivamente
    [2, 1],  #Coeficientes del compuesto B requerido para el fertilizante 1 y 2 respectivamente
    [5, 3],  #Coeficientes del compuesto C requerido para el fertilizante 1 y 2 respectivamente
]


B = [120, 80, 150]  #Disponibilidad de cada compuesto


#4:Restricciones de las variables
# xn >= 0; n=1,2
limites = [(0, None), (0, None)]

#5:Resolver
resultado = linprog(c, A_ub = A, b_ub = B, bounds = limites, method = 'highs')

#6:Imprimir
print("=" * 45)
print("MEZCLA DE FERTILIZANTES-Resultado con Scipy")
print(f"Estado : {resultado.message}")
print()
print(f"X1 = {resultado.x[0]:.4f} toneladas de fertilizante 1")
print(f"X2 = {resultado.x[1]:.4f} toneladas de fertilizante 2")
print()
print(f"Ganancia máxima = ${-resultado.fun:.4f}")
print("=" * 45)


#Ejercicio: mezcla de fertilizantes con PuLP

# 1. Importar librería
!pip install pulp
import pulp

# 2. Definir el problema
# sense=pulp.const.LpMaximize sirve para maximizar
problema = pulp.LpProblem("Mezcla_Fertilizantes", sense=pulp.const.LpMaximize)

# 3. Definir variables de decisión
# lowBound=0 reemplaza los limites [(0,None)] de linprog
x1 = pulp.LpVariable("Fertilizante_1", lowBound=0)
x2 = pulp.LpVariable("Fertilizante_2", lowBound=0)

# 4. Definir función objetivo
problema += 180*x1 + 220*x2, "Ganancia"

# 5. Definir restricciones
problema += 3*x1 + 4*x2 <= 120, "Compuesto_A"
problema += 2*x1 + 1*x2 <= 80,  "Compuesto_B"
problema += 5*x1 + 3*x2 <= 150, "Compuesto_C"

# 6. Resolver
problema.solve(pulp.PULP_CBC_CMD(msg=0))  # msg=0 suprime mensajes internos

# 7. Imprimir 
print("=" * 45)
print("MEZCLA DE FERTILIZANTES -Resultado con PuLP")
print(f"Estado: {pulp.LpStatus[problema.status]}")
print()
print(f"X1 = {pulp.value(x1):.4f} toneladas de fertilizante 1")
print(f"X2 = {pulp.value(x2):.4f} toneladas de fertilizante 2")
print()
print(f"Ganancia máxima = ${pulp.value(problema.objective):.4f}")
print("=" * 45)
