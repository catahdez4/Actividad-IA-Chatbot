import pickle
import faiss
from sentence_transformers import SentenceTransformer

# Cargar el modelo
modelo = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Cargar los fragmentos
with open("fragmentos.pkl", "rb") as f:
    fragmentos = pickle.load(f)

# Cargar el índice
index = faiss.read_index("indice.faiss")

# Chat loop
while True:
    pregunta = input(">> ")
    if pregunta.lower() == "salir":
        break

    vector_pregunta = modelo.encode([pregunta])
    distancias, indices = index.search(vector_pregunta, k=1)
    respuesta = fragmentos[indices[0][0]]

    print("\nRespuesta probable:\n", respuesta)
