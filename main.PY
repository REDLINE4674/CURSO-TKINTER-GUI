import tkinter as tk
from tkinter import messagebox

# ==================================
# 1. CREAR LA VENTANA PRINCIPAL
# ==================================

ventana = tk.Tk()
ventana.title("DataCleaner - Conexión")
ventana.geometry("500x520")
ventana.resizable(False, False)

# ==================================
# 2. CREAR LAS VARIABLES
# ==================================

servidor = tk.StringVar(value="localhost")
puerto = tk.StringVar(value="5432")
base_datos = tk.StringVar()
usuario = tk.StringVar()
contrasena = tk.StringVar()

# ==================================
# 3. CREAR EL TITULO
# ==================================

titulo = tk.Label(
    ventana,
    text="Conexión a PostgreSQL",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=20)

# ==================================
# 4. CREAR EL FORMULARIO
# ==================================

formulario = tk.Frame(ventana)
formulario.pack(padx=30, fill="x")


def crear_campo(texto, variable, ocultar=False):
    etiqueta = tk.Label(
        formulario,
        text=texto,
        anchor="w"
    )
    etiqueta.pack(fill="x", pady=(8, 2))

    entrada = tk.Entry(
        formulario,
        textvariable=variable,
        show="*" if ocultar else ""
    )
    entrada.pack(fill="x", ipady=4)

    return entrada


crear_campo("Servidor:", servidor)
crear_campo("Puerto:", puerto)
crear_campo("Base de datos:", base_datos)
crear_campo("Usuario:", usuario)

crear_campo(
    "Contraseña:",
    contrasena,
    ocultar=True
)

# ==================================
# 5. CREAR LA FUNCION DEL BOTON
# ==================================

def validar_conexion():
    datos = {
        "Servidor": servidor.get().strip(),
        "Puerto": puerto.get().strip(),
        "Base de datos": base_datos.get().strip(),
        "Usuario": usuario.get().strip(),
        "Contraseña": contrasena.get()
    }

    # Verificar campos vacios
    for campo, valor in datos.items():
        if not valor:
            messagebox.showwarning(
                "Campo obligatorio",
                f"El campo {campo} está vacío."
            )
            return

    # Verificar que el puerto sea numerico
    try:
        numero_puerto = int(datos["Puerto"])

        if not 1 <= numero_puerto <= 65535:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Puerto inválido",
            "Introduce un puerto entre 1 y 65535."
        )
        return

    # Mostrar los datos de conexion sin revelar la contraseña
    messagebox.showinfo(
        "Datos validados",
        f"Servidor: {datos['Servidor']}\n"
        f"Puerto: {numero_puerto}\n"
        f"Base de datos: {datos['Base de datos']}\n"
        f"Usuario: {datos['Usuario']}\n\n"
        "Los campos son válidos.\n"
        "Todavía no se ha conectado a PostgreSQL."
    )


# ==================================
# 6. CREAR EL BOTON
# ==================================

boton = tk.Button(
    ventana,
    text="Validar datos",
    command=validar_conexion,
    font=("Arial", 11, "bold"),
    padx=15,
    pady=6
)
boton.pack(pady=20)

# ==================================
# 7. INICIAR LA APLICACION
# ==================================

ventana.mainloop()