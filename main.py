import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter

# ---------------------------
# Configuración de la ventana principal
# ---------------------------
ventana = tk.Tk()
ventana.title("Editor de Imágenes")
ventana.configure(bg="#f0f0f0")  # Fondo gris claro
ventana.resizable(False, False)

# ---------------------------
# Variables globales para la imagen
# ---------------------------
imagen_original = None  # Imagen cargada, sin modificar
imagen_tk = None       # Imagen en formato Tkinter para mostrar en GUI

# ---------------------------
# Función para mostrar la imagen en la GUI
# ---------------------------
def mostrar_imagen(imagen):
    """
    Recibe una imagen PIL y la muestra en el Label de la GUI.
    Redimensiona la imagen para que quepa en la ventana.
    """
    global imagen_tk
    imagen_mostrar = imagen.copy()
    imagen_mostrar.thumbnail((500, 500))  # Ajuste de tamaño máximo
    imagen_tk = ImageTk.PhotoImage(imagen_mostrar)
    etiqueta_imagen.config(image=imagen_tk)

# ---------------------------
# Función para cargar imagen desde archivo
# ---------------------------
def cargar_imagen():
    """
    Abre un cuadro de diálogo para seleccionar una imagen.
    La imagen se guarda en 'imagen_original' y se muestra en la GUI.
    """
    global imagen_original
    ruta = filedialog.askopenfilename(
        filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if ruta:
        imagen_original = Image.open(ruta)
        mostrar_imagen(imagen_original)

# ---------------------------
# Funciones para filtros
# ---------------------------
def aplicar_desenfoque():
    """Aplica un filtro de desenfoque (blur) a la imagen original"""
    global imagen_original
    if imagen_original:
        imagen_filtrada = imagen_original.filter(ImageFilter.BLUR)
        mostrar_imagen(imagen_filtrada)

def aplicar_enfoque():
    """Aplica un filtro de enfoque (sharpen) a la imagen original"""
    global imagen_original
    if imagen_original:
        imagen_filtrada = imagen_original.filter(ImageFilter.SHARPEN)
        mostrar_imagen(imagen_filtrada)

def aplicar_grises():
    """Convierte la imagen original a escala de grises"""
    global imagen_original
    if imagen_original:
        imagen_filtrada = imagen_original.convert("L")
        mostrar_imagen(imagen_filtrada)

def rotar_imagen():
    """Rota la imagen original 90 grados a la derecha"""
    global imagen_original
    if imagen_original:
        imagen_filtrada = imagen_original.rotate(-90, expand=True)
        mostrar_imagen(imagen_filtrada)

# ---------------------------
# Función para guardar la imagen
# ---------------------------
def guardar_imagen():
    """
    Abre un cuadro de diálogo para guardar la imagen modificada.
    Permite guardar en PNG o JPEG.
    """
    global imagen_original
    if imagen_original:
        ruta = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Archivo PNG", "*.png"), ("JPEG", "*.jpg"), ("Todos los archivos", "*.*")]
        )
        if ruta:
            # Guardar la imagen original (sin redimensionar)
            imagen_original.save(ruta)

# ---------------------------
# Widgets de la GUI
# ---------------------------

# Botón para cargar imagen
boton_cargar = tk.Button(
    ventana,
    text="Cargar Imagen",
    font=("Arial", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=20,
    pady=10,
    command=cargar_imagen
)
boton_cargar.pack(pady=20)

# Etiqueta donde se mostrará la imagen
etiqueta_imagen = tk.Label(ventana, bg="#f0f0f0")
etiqueta_imagen.pack(pady=10)

# Botones de filtros y acciones
boton_desenfoque = tk.Button(
    ventana,
    text="Desenfocar",
    font=("Arial", 12, "bold"),
    bg="#FF9800",
    fg="white",
    command=aplicar_desenfoque
)
boton_desenfoque.pack(pady=5)

boton_enfoque = tk.Button(
    ventana,
    text="Enfocar",
    font=("Arial", 12, "bold"),
    bg="#03A9F4",
    fg="white",
    command=aplicar_enfoque
)
boton_enfoque.pack(pady=5)

boton_grises = tk.Button(
    ventana,
    text="Escala de Grises",
    font=("Arial", 12, "bold"),
    bg="#9C27B0",
    fg="white",
    command=aplicar_grises
)
boton_grises.pack(pady=5)

boton_rotar = tk.Button(
    ventana,
    text="Rotar 90°",
    font=("Arial", 12, "bold"),
    bg="#FF5722",
    fg="white",
    command=rotar_imagen
)
boton_rotar.pack(pady=5)

boton_guardar = tk.Button(
    ventana,
    text="Guardar Imagen",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=guardar_imagen
)
boton_guardar.pack(pady=10)

# ---------------------------
# Ejecutar la ventana
# ---------------------------
ventana.mainloop()
