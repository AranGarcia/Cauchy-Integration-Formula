import math
import cmath

def distancia_compleja(z1,z2):
    return math.sqrt( (z1.real - z2.real) ** 2 + (z1.imag - z2.imag) ** 2)

def verificar_tic(z0, radio, centro = (0,0)):
    """
    verificar_tic(z, r, c) -> bolean

    Verifica que cumpla con el Teorema de Integración
    de Cauchy. Si un número complejo pertenece a la 
    región circular gama, no cumple con el teorema.

    Argumentos:
    z0 = numero complejo a verificar si pertenece a la region circular
    radio = radio de la region circular
    centro = centro de la region circular
    """
    d = distancia_compleja(z0, 0)
    
    if d == radio:
        return None
    
    return d < radio
# Fin función verificar_tic

def calc_int_cauchy(fz, z, indice = None):
    """
    calc_int_cauchy(fz) -> (2 * pi * fz(z))

    Funcion matemática que calcula la integral que
    cumpla las condiciones de integración de Cauchy
    con funciones predeterminadas.
    """

    ipi2 = 2j * math.pi

    if indice:
        return ipi2 * (z ** indice)

    if fz == 1:
        return ipi2 * cmath.sin(z)

    elif fz == 2:
        return ipi2 * cmath.cos(z)

    elif fz == 3:
        return ipi2 * cmath.exp(z)

    elif fz == 5:
        return ipi2 * cmath.cosh(z)

    elif fz == 6:
        return ipi2 * cmath.sinh(z)

    else:
        return None