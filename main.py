import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from pdfrw import PdfReader, PdfWriter

# Función para seleccionar los archivos PDF
def select_files():
    # Abrir el cuadro de diálogo de selección de archivos
    files = filedialog.askopenfilenames(
        title="Seleccionar archivos PDF",
        filetypes=[("Archivos PDF", "*.pdf")]
    )
    # Convertir los archivos seleccionados a una lista
    files_list = list(files)
    # Procesar los archivos PDF seleccionados
    process_files(files_list)

# Función para procesar los archivos PDF
def process_files(files_list):
    # Recorrer todos los archivos PDF seleccionados
    for input_pdf in files_list:
        # Cargar el archivo PDF en un objeto PdfReader
        pdf_reader = PdfReader(input_pdf)
        # Obtener el número total de páginas del PDF
        num_pages = len(pdf_reader.pages)

        # Recorrer todas las páginas del PDF
        for page_num in range(num_pages):
            # Crear un objeto PdfWriter para cada página
            pdf_writer = PdfWriter()
            # Obtener la página actual del PDF
            page = pdf_reader.pages[page_num]
            # Agregar la página actual al objeto PdfWriter
            pdf_writer.addpage(page)
            # Crear un archivo de salida para la página actual
            input_file_name = Path(input_pdf).stem
            output_file = f"{input_file_name}_pagina_{page_num+1}.pdf"
            # Escribir la página actual en el archivo de salida
            pdf_writer.write(output_file)

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Dividir archivos PDF")

# Crear un botón para seleccionar los archivos PDF
select_button = tk.Button(root, text="Seleccionar archivos", command=select_files)
select_button.pack(padx=20, pady=20)

# Iniciar el bucle de eventos de la ventana
root.mainloop()