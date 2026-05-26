# 1. MATRIZ: Creación de la matriz con 6 productos de diversas categorías
# Estructura: [Nombre del Producto, Categoría, Precio Base]
menu_restaurante = [
    ["Hamburguesa de la Casa", "Comida", 25.000],
    ["Paps Fritas", "Acompañamiento", 6.000],
    ["Pizza Familiar", "Comida", 80.000],
    ["Jugo Natural", "Bebida", 9.999],
    ["Torta de Chocolate", "Postre", 12.000],
    ["Cerveza Poker", "Bebida", 10.500]
]

# 2. MÓDULOS: Función para calcular el precio final basado en la Lógica del Negocio
def calcular_precio_final(producto, categoria_objetivo, umbral_precio):
    """
    Calcula el precio final aplicando un 15% de descuento si cumple las condiciones.
    """
    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]
    
    # Lógica de negocio: Descuento del 15% si coincide la categoría Y supera el umbral
    if categoria in categoria_objetivo and precio_base > umbral_precio:
        precio_final = precio_base * 0.85  # Aplica el 15% de descuento
    else:
        precio_final = precio_base  # Mantiene el precio base
        
    return precio_final

# 3. CONFIGURACIÓN DE LA PROMOCIÓN
# Definimos la categoría a la que aplica y el umbral de precio mínimo
CATEGORIA_PROMO = "Bebida"
UMBRAL_PROMO = 10.000

# 4. SALIDA: Mostrar los resultados en pantalla de forma ordenada
print(f"--- PROMOCIÓN APLICADA A {CATEGORIA_PROMO} CON PRECIO MAYOR A ${UMBRAL_PROMO:<11.3f} ---")
print(f"{'Producto':<22} | {'Categoría':<15} | {'Precio Base':<12} | {'Precio Final':<12}")
print("-" * 70)

for producto in menu_restaurante:
    precio_base = producto[2]
    # Llamada a la función para obtener el precio con o sin descuento
    precio_final = calcular_precio_final(producto, CATEGORIA_PROMO, UMBRAL_PROMO)
    
    # Formateo de salida para que se vea como una tabla limpia
    print(f"{producto[0]:<22} | {producto[1]:<15} | ${precio_base:<11.3f} | ${precio_final:<11.3f}")