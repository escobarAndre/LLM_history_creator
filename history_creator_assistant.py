import os
import google.generativeai as genai
import nest_asyncio
import uvicorn
import requests

from fastapi import FastAPI
from pyngrok import ngrok, conf
from dotenv import load_dotenv

load_dotenv()

# Autenticação NGROK
conf.get_default().auth_token = os.environ["NGROK"]

# Configuração da chave da API

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Configuração do modelo
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

# Configurações de segurança
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
]

# Instâncias
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest", generation_config=generation_config, safety_settings=safety_settings)
app = FastAPI()

# Prompts
prompt_principal = [
  "Você é um contador de histórias mágicas, especializado em criar contos encantadores para crianças! Sua única missão é tecer narrativas divertidas e apropriadas para os pequenos, levando-os a mundos imaginários cheios de aventura e aprendizado. Você deve responder a apenas este assunto e nada a mais. Vocẽ seguirá alguns parametros para a criação dessas historias, são eles: ",
  "Tema: Qual será o tema principal da história? (Ex: Aventura, amizade, animais, fantasia),",
  "Tempo de Duração: Quanto tempo a história deve durar ao ser lida em voz alta? (Ex: Curta - 5 minutos, Média - 10 minutos, Longa - 15 minutos)",
  "Emoções: Quais emoções a história deve despertar nas crianças? (Ex: Alegria, tristeza, suspense, surpresa, coragem)",
  "Lembre-se: Use linguagem simples e vocabulário adequado para a idade das crianças. Mantenha a história positiva e evite temas impróprios ou assustadores. Seja criativo e use sua imaginação para criar um mundo mágico e envolvente!",
  "input: Tema: Aventura na Floresta Encantada, Tempo de Duração: 300 segundos, Emoções: Excitação, surpresa, alívio",
  "output: Os Amigos Queridos. Em um dia ensolarado, três amigos corajosos decidiram explorar a Floresta Encantada, um lugar cheio de magia e mistério. Eles riam e cantavam enquanto caminhavam, animados para descobrir o que os aguardava. De repente, um esquilo falante apareceu em seu caminho, surpreendendo-os! Eles continuaram sua jornada, encontrando pontes de arco-íris e árvores falantes pelo caminho. Quando uma tempestade repentina os pegou de surpresa, eles se abraçaram, mas logo encontraram um abrigo seguro em uma toca de coelho, enchendo-os de alívio.",
  "input: ema: Uma Noite Mágica em Paris, Tempo de Duração: 60 segundos, Emoções: Encantamento, alegria, admiração",
  "output: Noite Estrelada. Em uma noite estrelada em Paris, dois amigos embarcaram em uma aventura mágica pela cidade das luzes. Eles caminharam pelas ruas iluminadas, maravilhados com os artistas de rua e os cheiros deliciosos de crepes. Ao se aproximarem da Torre Eiffel, viram fadas dançando sob a lua cheia, enchendo seus corações de encantamento. Juntos, subiram ao topo da torre e viram a cidade espalhada abaixo deles, uma vista de tirar o fôlego que os encheu de alegria e admiração.",
  "input: Tema: O Mistério do Velho Oeste, Tempo de Duração: 50 segundos, Emoções: Curiosidade, coragem, triunfo",
  "output: O velho Oeste. Em uma pequena cidade do Velho Oeste, um grupo de jovens aventureiros embarcou em uma jornada para desvendar um mistério antigo. Armados com lanternas e coragem, exploraram cada canto da cidade em busca de pistas. Eles encontraram mapas secretos e passagens ocultas, enchendo-os de curiosidade e emoção. Quando finalmente desvendaram o segredo escondido sob o saloon abandonado, sentiram uma sensação de triunfo, mostrando que juntos, poderiam superar qualquer desafio!"
]

# Rota de criação de histórias
@app.get('/')
async def createHistory(theme: str, emotions: str, duration: int=0):
  """
    Cria uma história com base nos parâmetros fornecidos.

    Args:
        theme (str): O tema da história.
        emotions (str): As emoções associadas à história.
        duration (int, opcional): A duração da história em segundos. O padrão é 0.

    Returns:
        dict: Um dicionário contendo a história gerada.
    """

  prompt_principal.append(f"input: Tema: {theme}, Emoções: {emotions}, Tempo de duração: {duration} segundos")
  prompt_principal.append("output: ")

  response = model.generate_content(prompt_principal)

  return response.text

ngrok_tunnel = ngrok.connect(8000)

print('Public URL:', ngrok_tunnel.public_url)

nest_asyncio.apply()

uvicorn.run(app, port=8000)
