# Ejercicio: Modelo logistico de pesca

# 1. Parámetros del modelo y condición inicial
K  = 1000   # capacidad máxima de la laguna
r  = 0.4    # tasa de crecimiento
H  = 80     # peces extraídos por año
P0 = 400    # población inicial

# 2. Función del modelo
# P(n+1) = P(n) + r * P(n) * (1 - P(n)/K) - H
def siguiente_año(P):
    return P + r * P * (1 - P/K) - H

# 3. Calcular año 1 y año 2
P1 = siguiente_año(P0)
P2 = siguiente_año(P1)

# 4. Imprimir resultados
print("=" * 45)
print("PESCA SOSTENIBLE")
print()
print(f"Población inicial (año 0): {P0:.1f} peces")
print(f"Población año 1:           {P1:.1f} peces")
print(f"Población año 2:           {P2:.1f} peces")
print("=" * 45)
