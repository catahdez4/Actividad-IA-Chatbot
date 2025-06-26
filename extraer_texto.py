import pdfplumber

# Abrir el PDF y extraer texto
texto_completo = ""
with pdfplumber.open("documento.pdf") as pdf:
    for pagina in pdf.pages:
        texto = pagina.extract_text()
        if texto:
            texto_completo += texto + "\n"

# Guardar el texto extraído en archivo .txt
with open("texto_extraido.txt", "w", encoding="utf-8") as archivo:
    archivo.write(texto_completo)