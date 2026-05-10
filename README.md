# MyFirstAPICall
OPT

# OPT - Your First API Call

## Informació del curs

- **Cicle:** ASIX - Administració de Sistemes Informàtics en Xarxa
- **Mòdul:** OPT. Mòdul Optatiu
- **RA5:** Prototipa solucions d’intel·ligència artificial en aplicacions empresarials.

---

# Entorn de desenvolupament

Primer es va crear una carpeta per al projecte:

```bash
mkdir langchain-hf
cd langchain-hf
```

Seguidament, es va crear l’entorn virtual de Python:

```bash
python -m venv venv
```

I, per últim, es va activar l’entorn virtual:

```bash
source venv/bin/activate
```

---

# Instal·lació de dependències

Per instal·lar les llibreries necessàries es van executar les següents ordres:

```bash
pip install langchain huggingface_hub
```

---

# Configuració de Hugging Face

Es va crear un compte gratuït a la plataforma Hugging Face:

https://huggingface.co/

Posteriorment es va generar un token d’accés des de la configuració del compte.

Aquest token és necessari per autenticar les peticions API realitzades des del programa Python.

El token s’ha guardat com una variable d’entorn perquè, a l’hora de pujar el codi a GitHub, sigui més segur i no quedi visible el token personal.

```bash
export HF_TOKEN="TOKEN_PERSONAL"
```

---

# Selecció del model

El model seleccionat ha estat:

https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct

Aquest model s’ha escollit perquè:

- És gratuït.
- És compatible amb Hugging Face Inference API.
- No requereix execució local amb GPU.

---

# Primera crida API amb LangChain

Es va crear el fitxer `main.py`.

La classe `InferenceClient` permet connectar Python amb la API d’Hugging Face utilitzant inferència remota.

## Paràmetres principals

- `provider`: especifica el proveïdor d’inferència utilitzat.
- `api_key`: token personal d’autenticació.
- `model`: model utilitzat per generar text.
- `messages`: missatges enviats al model seguint format conversacional.
- `max_tokens`: nombre màxim de tokens generats.

## Codi utilitzat

```python
import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="featherless-ai",
    api_key=os.environ["HF_TOKEN"],
)

response = client.chat_completion(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    messages=[
        {
            "role": "user",
            "content": "Explica’m què és la intel·ligència artificial."
        }
    ],
    max_tokens=100,
)

print(response.choices[0].message.content)
```

---

# Execució del programa

Per executar el programa es va utilitzar:

```bash
python main.py
```

## Resposta generada pel model

```text
Artificial intelligence is a type of technology that allows computers
to learn, reason, and solve problems similarly to humans.
```

---

# Configuració alternativa de paràmetres

S’ha creat un codi alternatiu modificant la temperatura del model perquè sigui més precís i menys creatiu. També s’ha augmentat el nombre màxim de tokens perquè la resposta fos més clara.

## Diferències principals

- `InferenceClient` connecta el programa Python amb la API d’Hugging Face.
- `temperature` controla el nivell de creativitat i variabilitat de la resposta generada.

## Exemple alternatiu

```python
import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="featherless-ai",
    api_key=os.environ["HF_TOKEN"],
)

response = client.chat_completion(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    messages=[
        {
            "role": "user",
            "content": "Write a short paragraph about machine learning."
        }
    ],
    max_tokens=200,
    temperature=0.2,
)

print(response.choices[0].message.content)
```

---
# Proves


https://github.com/user-attachments/assets/db7d0d31-5b6a-4f8e-bd41-9c0d14026548

