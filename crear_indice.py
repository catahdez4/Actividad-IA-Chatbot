from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

# Leer el texto extraído
with open("texto_extraido.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read()


# Dividir en fragmentos
fragmentos = texto.split("\n\n")  # Puedes ajustar esto si lo deseas más fino

# Cargar el modelo
modelo = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Convertir fragmentos en vectores
vectores = modelo.encode(fragmentos)

# Crear el índice FAISS
index = faiss.IndexFlatL2(vectores.shape[1])
index.add(np.array(vectores))

# Guardar los fragmentos y el índice
with open("fragmentos.pkl", "wb") as f:
    pickle.dump(fragmentos, f)

faiss.write_index(index, "indice.faiss")


print("Índice y fragmentos guardados correctamente.")