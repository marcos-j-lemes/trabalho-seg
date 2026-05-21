# trabalho-seg
mitmproxy


## Comandos para rodar o docker:


Configuração dockerfile:

[imagem docker](./mimtproxy/dockerfile)

```bash
   18  cd mitmproxy
   19  docker build -t mitmweb .
   20  docker run -it --rm   --name mitmweb   -p 8080:8080   -p 8081:8081   -v $(pwd):/workspace   mitmweb
   21  history

```


Após rodar o docker ele vai mostrar um token no terminal:

```bash
http://0.0.0.0:8081/?token=a723fff611f2d3d81ad03ef845716f4d

```


> A configuração do mitmproxy está pronta!!


## Servidor 

### API FastAPI

A API recebe um texto via `POST /texto` e retorna um JSON com o texto original,
uma resposta e o horario do recebimento.

Configuracao facil do IP/porta da API:

- Arquivo: `api/config.py`
- Padrao: `API_HOST = "0.0.0.0"` e `API_PORT = 8000`

```bash
cd api
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

Para testar direto:

```bash
curl -X POST http://127.0.0.1:8000/texto \
  -H "Content-Type: application/json" \
  -d '{"texto":"Mensagem de teste"}'
```

### Front

O front permite trocar o IP e a porta da API pela tela. Tambem da para trocar
os valores padrao no comeco do script em `servidor/index.html`:

- `DEFAULT_API_HOST`
- `DEFAULT_API_PORT`

Para subir:

```bash

cd servidor

ls

index.html


# comando para rodar o servidor:

 python3 -m http.server 5500


```

Acesse:

```text
http://127.0.0.1:5500
```


## Configuração na web:

Procura o ip da máquina

`ifconfig`

e coloca nas configurações do mitmproxy

![Imagem para explicar](./img/webMITM.png)


## Após todas as configuração o sistema ficará assim:


![a](./img/proxy.png)
