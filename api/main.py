from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from config import ALLOWED_ORIGINS, API_HOST, API_PORT


app = FastAPI(
    title="API Demo MITMProxy",
    description="Recebe um texto e devolve outro texto para demonstrar interceptacao HTTP.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextoEntrada(BaseModel):
    texto: str = Field(..., min_length=1, examples=["Mensagem para interceptar"])


class TextoSaida(BaseModel):
    texto_original: str
    texto_resposta: str
    recebido_em: str


@app.get("/")
def status():
    return {
        "status": "online",
        "mensagem": "API pronta. Envie POST /texto com {'texto': 'sua mensagem'}.",
    }


@app.post("/texto", response_model=TextoSaida)
def receber_texto(payload: TextoEntrada):
    texto_limpo = payload.texto.strip()

    print(TextoSaida(
        texto_original=payload.texto,
        texto_resposta=f"API recebeu: {texto_limpo}",
        recebido_em=datetime.now().isoformat(timespec="seconds"),
    ))

    return TextoSaida(
        texto_original=payload.texto,
        texto_resposta=f"API recebeu: {texto_limpo}",
        recebido_em=datetime.now().isoformat(timespec="seconds"),
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=API_HOST, port=API_PORT)
