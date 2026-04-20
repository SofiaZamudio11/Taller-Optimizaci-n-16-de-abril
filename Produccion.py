# Ejercicio: Producción de mesas y sillas

# 1. Importar librería
import numpy as np

# 2. Condiciones iniciales
S0 = 200   # sillas
M0 = 80    # mesas

# 3. Número de semanas a simular
n = 2

# 4. Crear listas para guardar resultados
S = [S0]
M = [M0]

# 5. Modelo
# S(n+1) = 0.6*S(n) + 0.2*M(n) + 40
# M(n+1) = 0.1*S(n) + 0.5*M(n) + 20

for i in range(n):
    S_siguiente = 0.6*S[i] + 0.2*M[i] + 40
    M_siguiente = 0.1*S[i] + 0.5*M[i] + 20

    S.append(S_siguiente)
    M.append(M_siguiente)

# 6. Imprimir resultados
print("=" * 45)
print("PRODUCCIÓN POR SEMANA:\n")
for i in range(n + 1):
    print(f"Semana {i}: Sillas = {S[i]:.1f}, Mesas = {M[i]:.1f}")
print("=" * 45)
