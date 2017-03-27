#!/usr/bin/python
import graficas
import sys
import teorema_int_cauchy as tic

print("Formula integral de Cauchy\n\u222b(f(z)/(z - z0))dz en "
     "una región circular \u03b3(t) de radio r\n")

# Validación de entradas
funciones = {1 : "sen(z)", 2 : "cos(z)", 3 : "e^z",
    4 : "z^n", 5 : "senh(z)", 6 : "cosh(z)"}
try:
    radio = float(input("Radio = "))
    z0 = complex(input("z0 = "))

    ok = False
    print("Elige una función:\n")
    for f in funciones:
        print(f ,".-",funciones[f])
    num_fun = int(input("f(z) = "))

    if num_fun not in funciones:
            raise ValueError("Opcion invalida (" + str(num_fun) + ")")

    # Si se eligió z ^ n ...
    if num_fun == 4:
        indice = int(input("Defina el exponente 'n' = "))

except ValueError as err:
    print("Error: Entrada inválida (" + str(err) + ").")
    sys.exit(1)
except EOFError:
    print("\n\nEjecución terminada.")
    sys.exit(0)
# Fin validación entradas

# Verifica si cumple el Teorema de Integracion de Cauchy
cumple_teorema = tic.verificar_tic(z0, radio)

if cumple_teorema:
    if num_fun == 4:
        resultado = tic.calc_int_cauchy(num_fun, z0, indice)
    else:
        resultado = tic.calc_int_cauchy(num_fun,z0)
else:
    resultado = 0

# Convierte numero complejo a cadena con signo adecuado
z_str = "%.2f" % resultado.real
if resultado.imag < 0:
    z_str += "%.2f" % resultado.imag
else:
    z_str += "+%.2f" % resultado.imag
z_str += "j"

# Organiza la cadena para el título de gráfica
if num_fun == 4:
    funciones[num_fun] = "z^" + str(indice)
ti = "Integral de\n" + funciones[num_fun] + "/ (z - " + str(z0) + ") = " + z_str
graficas.graficar_region(z0, radio, titulo = ti)
