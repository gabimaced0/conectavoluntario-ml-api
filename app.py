from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Carregar modelo treinado
modelo = joblib.load("classificador_prioridade.pkl")

# Inicializar app FastAPI
app = FastAPI()

# Modelo de entrada
class Pedido(BaseModel):
    texto: str

# Endpoint para classificar prioridade
@app.post("/classificar")
def classificar_pedido(pedido: Pedido):
    pred = modelo.predict([pedido.texto])
    return {"prioridade": pred[0]}
