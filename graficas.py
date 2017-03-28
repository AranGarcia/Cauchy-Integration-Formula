import matplotlib.pyplot as plt

def graficar_region(z, r, h = (0,0), titulo = None):
    fig = plt.gcf()

    fig.canvas.set_window_title("Teorema de Integración de Cauchy")
    plt.xlabel("Reales")
    plt.ylabel("Imaginarios")

    if titulo:
        plt.title(titulo)

    # Convierte numero complejo a cadena con signo adecuado
    z_str = "%.2f" % z.real
    if z.imag < 0:
        z_str += "%.2f" % z.imag
    else:
        z_str += "+%.2f" % z.imag
    z_str += "j"
        
    plt.plot(z.real, z.imag, label = "$z_0$ = " + z_str, marker = "o")
    
    circle = plt.Circle((0, 0), color = "r",radius = r, alpha = .5, label = "$\gamma$(t), [0,2$\pi$]")
    plt.gca().add_patch(circle)

    plt.axis('equal')
    plt.legend()
    plt.grid()
    plt.show()

