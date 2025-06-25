
from PyPDF2 import PdfReader

# Nombre del archivo PDF (debe estar en la misma carpeta que este script)
nombre_pdf = "documento.pdf"

# Leer el archivo PDF
reader = PdfReader(nombre_pdf)
texto_completo = ""

for pagina in reader.pages:
    texto = pagina.extract_text()
    if texto:
        texto_completo += texto + "\n"

# Guardar el texto extraído en un archivo de texto
with open("texto_extraido.txt", "w", encoding="utf-8") as archivo:
    archivo.write(texto_completo)

print("Texto extraído correctamente.")

