import matplotlib.pyplot as plt

def graficar_region(z, r, h = (0,0), titulo = None):

    # Preparación de la figura
    fig = plt.gcf()
    fig.canvas.set_window_title("Teorema de Integración de Cauchy")
    plt.xlabel("Reales")
    plt.ylabel("Imaginarios")
    if titulo:
        plt.title(titulo, fontsize = 18, y=1.08)

    # Convierte numero complejo a cadena con signo adecuado
    z_str = "%.2f" % z.real
    if z.imag < 0:
        z_str += "%.2f" % z.imag
    else:
        z_str += "+%.2f" % z.imag
    z_str += "j"
        
    # Grafica z0
    plt.plot(z.real, z.imag, label = "$z_0$ = " + z_str, marker = "o")
    
    # Grafica gama de t
    circle = plt.Circle((0, 0), color = "r",radius = r, alpha = .5, label = "$\gamma$(t), [0,2$\pi$]")
    plt.gca().add_patch(circle)

    # Ajusta y termina detalles
    plt.axis('equal')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

