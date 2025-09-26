# -*- coding: utf-8 -*-
"""
Cálculo de dobleces de papel para alcanzar diferentes alturas
¿Cuántas veces hay que doblar un papel para superar el Monte Fuji?
"""

import math
import matplotlib.pyplot as plt

# Constantes
GROSOR_PAPEL = 0.00008  # metros (papel normal)
ALTURA_FUJI = 3776  # metros
DISTANCIA_LUNA = 384400000  # metros (384,400 km)
DISTANCIA_PROXIMA_CENTAURI = 4.0175e16  # metros

def calcular_grosor_after_folds(n, grosor_inicial=GROSOR_PAPEL):
    """
    Calcula el grosor después de n dobleces.
    
    Parameters:
    n (int): Número de dobleces
    grosor_inicial (float): Grosor inicial del papel en metros
    
    Returns:
    float: Grosor después de n dobleces en metros
    """
    return grosor_inicial * (2 ** n)

def encontrar_min_dobleces(altura_objetivo, grosor_inicial=GROSOR_PAPEL):
    """
    Encuentra el número mínimo de dobleces para superar una altura objetivo.
    
    Parameters:
    altura_objetivo (float): Altura objetivo en metros
    grosor_inicial (float): Grosor inicial del papel en metros
    
    Returns:
    int: Número mínimo de dobleces requeridos
    """
    n = 0
    grosor_actual = grosor_inicial
    
    while grosor_actual < altura_objetivo:
        n += 1
        grosor_actual = grosor_inicial * (2 ** n)
    
    return n

def calcular_longitud_papel_necesaria(n, grosor_inicial=GROSOR_PAPEL):
    """
    Calcula la longitud mínima de papel necesaria para realizar n dobleces.
    
    Parameters:
    n (int): Número de dobleces
    grosor_inicial (float): Grosor inicial del papel en metros
    
    Returns:
    float: Longitud mínima de papel necesaria en metros
    """
    if n < 1:
        return 0
    
    # Fórmula: L = (π * t₀ / 6) * (2ⁿ + 4) * (2ⁿ - 1)
    longitud = (math.pi * grosor_inicial / 6) * (2**n + 4) * (2**n - 1)
    return longitud

def problema_1_fuji():
    """Resuelve el problema 1: Dobleces para superar el Monte Fuji"""
    print("=" * 70)
    print("PROBLEMA 1: ¿CUÁNTAS VECES DOBLAR PAPEL PARA SUPERAR EL MONTE FUJI?")
    print("=" * 70)
    
    dobleces_fuji = encontrar_min_dobleces(ALTURA_FUJI)
    grosor_final = calcular_grosor_after_folds(dobleces_fuji)
    
    print(f"Altura del Monte Fuji: {ALTURA_FUJI:,} metros")
    print(f"Grosor del papel inicial: {GROSOR_PAPEL} metros")
    print(f"Dobleces necesarios: {dobleces_fuji}")
    print(f"Grosor final: {grosor_final:,.2f} metros")
    print(f"¿Supera el Fuji? {grosor_final > ALTURA_FUJI}")
    print(f"Exceso: {grosor_final - ALTURA_FUJI:,.2f} metros")
    
    return dobleces_fuji, grosor_final

def problema_2_altura_arbitraria():
    """Resuelve el problema 2: Función para altura arbitraria"""
    print("\n" + "=" * 70)
    print("PROBLEMA 2: FUNCIÓN PARA ALTURA ARBITRARIA")
    print("=" * 70)
    
    # Ejemplo con la Luna
    dobleces_luna = encontrar_min_dobleces(DISTANCIA_LUNA)
    grosor_luna = calcular_grosor_after_folds(dobleces_luna)
    
    print("🌙 PARA ALCANZAR LA LUNA:")
    print(f"Distancia a la Luna: {DISTANCIA_LUNA:,.0f} metros")
    print(f"Dobleces necesarios: {dobleces_luna}")
    print(f"Grosor final: {grosor_luna:,.0f} metros")
    
    # Ejemplo con Próxima Centauri
    dobleces_estrella = encontrar_min_dobleces(DISTANCIA_PROXIMA_CENTAURI)
    grosor_estrella = calcular_grosor_after_folds(dobleces_estrella)
    
    print("\n⭐ PARA ALCANZAR PRÓXIMA CENTAURI:")
    print(f"Distancia: {DISTANCIA_PROXIMA_CENTAURI:.2e} metros")
    print(f"Dobleces necesarios: {dobleces_estrella}")
    print(f"Grosor final: {grosor_estrella:.2e} metros")
    
    # Comparación de distancias cósmicas
    print(f"\n📊 COMPARACIÓN CÓSMICA:")
    print(f"• 1 año luz ≈ {9.461e15:,.0f} metros")
    print(f"• Próxima Centauri ≈ 4.24 años luz")
    print(f"• Vía Láctea diámetro ≈ 100,000 años luz")
    
    return dobleces_luna, dobleces_estrella

def problema_3_longitud_papel():
    """Resuelve el problema 3: Longitud de papel necesaria"""
    print("\n" + "=" * 70)
    print("PROBLEMA 3: LONGITUD DE PAPEL NECESARIA")
    print("=" * 70)
    
    # Calcular dobleces para cada objetivo
    dobleces_fuji = encontrar_min_dobleces(ALTURA_FUJI)
    dobleces_luna = encontrar_min_dobleces(DISTANCIA_LUNA)
    dobleces_estrella = encontrar_min_dobleces(DISTANCIA_PROXIMA_CENTAURI)
    
    # Calcular longitudes necesarias
    longitud_fuji = calcular_longitud_papel_necesaria(dobleces_fuji)
    longitud_luna = calcular_longitud_papel_necesaria(dobleces_luna)
    longitud_estrella = calcular_longitud_papel_necesaria(dobleces_estrella)
    
    print("📏 LONGITUD DE PAPEL NECESARIA:")
    print(f"• Monte Fuji ({dobleces_fuji} dobleces): {longitud_fuji:,.2f} metros")
    print(f"• Luna ({dobleces_luna} dobleces): {longitud_luna:,.2e} metros")
    print(f"• Próxima Centauri ({dobleces_estrella} dobleces): {longitud_estrella:.2e} metros")
    
    # Comparaciones para entender la escala
    print(f"\n🌍 COMPARACIONES DE ESCALA:")
    print(f"• Circunferencia terrestre: ≈ 40,000,000 metros")
    print(f"• Distancia Tierra-Luna: ≈ 384,400,000 metros")
    print(f"• Papel para la Luna: ≈ {longitud_luna/DISTANCIA_LUNA:.1f} veces la distancia Tierra-Luna")
    
    # Conversiones a unidades astronómicas
    metros_anio_luz = 9.461e15
    print(f"• Papel para estrella: ≈ {longitud_estrella/metros_anio_luz:.1f} años luz")
    
    return longitud_fuji, longitud_luna, longitud_estrella

def visualizar_crecimiento_exponencial():
    """Visualiza el crecimiento exponencial del grosor del papel"""
    print("\n" + "=" * 70)
    print("VISUALIZACIÓN DEL CRECIMIENTO EXPONENCIAL")
    print("=" * 70)
    
    # Configuración para CodeSpaces
    plt.switch_backend('Agg')
    
    # Calcular datos para 30 dobleces (para visualización práctica)
    max_dobleces_visual = 30
    dobleces = list(range(0, max_dobleces_visual + 1))
    grosores = [calcular_grosor_after_folds(n) for n in dobleces]
    longitudes = [calcular_longitud_papel_necesaria(n) for n in dobleces if n >= 1]
    
    # Crear figura con múltiples subgráficos
    plt.figure(figsize=(15, 10))
    
    # Gráfico 1: Crecimiento del grosor (escala lineal)
    plt.subplot(2, 2, 1)
    plt.plot(dobleces, grosores, 'b-', linewidth=2, marker='o', markersize=4)
    plt.axhline(y=ALTURA_FUJI, color='red', linestyle='--', label='Monte Fuji')
    plt.title('Crecimiento del Grosor del Papel', fontweight='bold')
    plt.xlabel('Número de Dobleces')
    plt.ylabel('Grosor (metros)')
    plt.yscale('linear')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Gráfico 2: Crecimiento del grosor (escala logarítmica)
    plt.subplot(2, 2, 2)
    plt.plot(dobleces, grosores, 'g-', linewidth=2, marker='s', markersize=4)
    plt.axhline(y=ALTURA_FUJI, color='red', linestyle='--', label='Monte Fuji')
    plt.title('Crecimiento Exponencial (Escala Log)', fontweight='bold')
    plt.xlabel('Número de Dobleces')
    plt.ylabel('Grosor (metros) - Escala log')
    plt.yscale('log')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Gráfico 3: Longitud de papel necesaria
    plt.subplot(2, 2, 3)
    dobleces_longitud = list(range(1, max_dobleces_visual + 1))
    plt.plot(dobleces_longitud, longitudes, 'purple', linewidth=2, marker='^', markersize=4)
    plt.title('Longitud de Papel Necesaria', fontweight='bold')
    plt.xlabel('Número de Dobleces')
    plt.ylabel('Longitud (metros)')
    plt.yscale('log')
    plt.grid(True, alpha=0.3)
    
    # Gráfico 4: Comparación de objetivos
    plt.subplot(2, 2, 4)
    objetivos = ['Fuji', 'Luna', 'Próxima Centauri']
    dobleces_objetivos = [
        encontrar_min_dobleces(ALTURA_FUJI),
        encontrar_min_dobleces(DISTANCIA_LUNA),
        encontrar_min_dobleces(DISTANCIA_PROXIMA_CENTAURI)
    ]
    
    plt.bar(objetivos, dobleces_objetivos, color=['blue', 'green', 'red'])
    plt.title('Dobleces para Diferentes Objetivos', fontweight='bold')
    plt.ylabel('Número de Dobleces')
    plt.grid(True, alpha=0.3)
    
    # Añadir valores en las barras
    for i, v in enumerate(dobleces_objetivos):
        plt.text(i, v + 0.1, str(v), ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig('crecimiento_papel_doblado.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print("✅ Gráfico guardado como 'crecimiento_papel_doblado.png'")

def main():
    """Función principal del programa"""
    print("🗻 CALCULADORA DE DOBLECES DE PAPEL PARA ALCANZAR OBJETIVOS")
    print("=" * 70)
    
    try:
        # Resolver los tres problemas
        dobleces_fuji, grosor_fuji = problema_1_fuji()
        dobleces_luna, dobleces_estrella = problema_2_altura_arbitraria()
        long_fuji, long_luna, long_estrella = problema_3_longitud_papel()
        
        # Visualización
        visualizar_crecimiento_exponencial()
        
        # Resumen ejecutivo
        print("\n" + "=" * 70)
        print("RESUMEN EJECUTIVO")
        print("=" * 70)
        
        print(f"🎯 DOBLECES NECESARIOS:")
        print(f"• Monte Fuji (3,776 m): {dobleces_fuji} dobleces")
        print(f"• Luna (384,400 km): {dobleces_luna} dobleces")
        print(f"• Próxima Centauri (4.24 años luz): {dobleces_estrella} dobleces")
        
        print(f"\n📏 LONGITUDES DE PAPEL (aproximadas):")
        print(f"• Para Fuji: {long_fuji:,.0f} metros")
        print(f"• Para Luna: {long_luna:.2e} metros")
        print(f"• Para estrella: {long_estrella:.2e} metros")
        
        print(f"\n💡 DATOS INTERESANTES:")
        print(f"• El papel no se puede doblar más de 7-8 veces en la práctica")
        print(f"• El récord mundial es de 13 dobleces (papel especial)")
        print(f"• Estos cálculos muestran el poder del crecimiento exponencial")
        
        # Verificación física
        print(f"\n🔍 VERIFICACIÓN FÍSICA:")
        print(f"• ¿Es realista? NO - es una demostración matemática")
        print(f"• Pero muestra cómo funciona el crecimiento exponencial")
        print(f"• Aplicable a: tecnología, población, datos, etc.")
        
    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")

# Ejecutar el programa
if __name__ == "__main__":
    main()
