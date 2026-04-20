# Ejercicio: Epidemia en una ciudad

# 1. Importar librerias
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# 2. Parámetros del modelo
beta  = 0.00003   # tasa de contagio
gamma = 0.1       # tasa de recuperación
P     = 10000     # población total


# 3. Definir la EDO
# dI/dt = β·(P - I)·I - γ·I
# t es el tiempo, y[0] es I(t)

def modelo(t, y):
    I = y[0]
    dIdt = beta * (P - I) * I - gamma * I
    return [dIdt]

# 4. Condición inicial e intervalo de tiempo
I0 = [50]              # I(0) = 50 infectados
t_inicio = 0
t_fin    = 200         # simulación de 200 días
t_eval   = np.linspace(t_inicio, t_fin, 1000)  # 1000 puntos

# 5. Resolver la EDO
resultado = solve_ivp(modelo, [t_inicio, t_fin], I0, t_eval=t_eval, method='RK45')

# 6. Extraer resultados
t = resultado.t
I = resultado.y[0]
S = P - I               # Población susceptible

# 7. Imprimir 
print("=" * 45)
print("MODELO EPIDEMIA")
print()
print(f"Infectados iniciales:   {I0[0]}")
print(f"Valor máximo alcanzado: {max(I):.1f} personas (día {t[np.argmax(I)]:.1f})")
print(f"Equilibrio endémico:    {I[-1]:.1f} personas")
print(f"Equilibrio teórico I*:  {P - gamma/beta:.1f} personas")
print("=" * 45)


# 8. Graficar
plt.figure(figsize=(10, 5))
plt.plot(t, I, color='red',  label='Infectados I(t)')
plt.plot(t, S, color='blue', label='Susceptibles S(t)')
plt.axhline(y=P - gamma/beta, color='green', linestyle='--', label=f'Equilibrio I* = {P - gamma/beta:.0f}')
plt.xlabel("Tiempo (días)")
plt.ylabel("Número de personas")
plt.title("Modelo SIS - Propagación de enfermedad")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
