## Histórias Mágicas: Crie Contos Infantis com Inteligência Artificial

**Introdução**

Este projeto foi criado para a imersão da Alura com o Google, utilizando o Gemini para gerar histórias infantis. O projeto usa Ngrok para criar um túnel público para a API FastAPI, permitindo que você acesse e teste a funcionalidade da ferramenta de forma fácil.

**Funcionalidades**

* Gera histórias infantis personalizadas com base em tema, emoções e tempo de duração.
* Utiliza o modelo de linguagem Gemini-1.5-Pro-Latest para garantir alta qualidade e segurança.
* Implementa configurações de segurança para evitar conteúdo prejudicial.
* Oferece uma interface de linha de comando amigável para interação.
* Possui um endpoint API RESTful para integração com outras aplicações.

**Destaques**

* **Criatividade:** Gere histórias infantis únicas e envolventes para encantar as crianças.
* **Personalização:** Adapte as histórias aos interesses e necessidades do seu público.
* **Segurança:** Tenha a tranquilidade de saber que o conteúdo gerado é adequado para todas as idades.
* **Acessibilidade:** Utilize a API para interagir com a ferramenta facilmente.
* **Escalabilidade:** Integre a ferramenta em seus próprios projetos e aplicações com facilidade.

**Começando**

1. **Clone o repositório:** 

```bash
git clone https://github.com/topics/imersao-ia-alura-google
```

2. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

3. **Execute o script principal:**

```bash
python main.py
```

4. **Acesse a ferramenta:**

* **API RESTful:** Utilize o endpoint `/` para enviar solicitações de geração de história com parâmetros JSON.

## Acessando a API RESTful do Seu Contador de Histórias Mágicas

**1. Obtenha o URL da API:**

* **Ngrok:** Se você estiver usando o Ngrok, o URL público da API estará disponível no console do Ngrok após iniciar o script principal.
* **Execução local:** Se você estiver executando o projeto localmente, o URL da API será `http://localhost:8000`.

**2. Prepare os Parâmetros JSON:**

Crie um objeto JSON com os seguintes parâmetros:

* **`theme` (obrigatório):** O tema da história (ex: "Aventura na Floresta Encantada").
* **`emotions` (obrigatório):** As emoções que a história deve despertar (ex: "Excitação, surpresa, alívio").
* **`duration` (opcional):** A duração da história em segundos (padrão: 0).

**Exemplo de parâmetros JSON:**

```json
{
  "theme": "Aventura na Floresta Encantada",
  "emotions": "Excitação, surpresa, alívio",
  "duration": 300
}
```

**3. Envie a Solicitação HTTP:**

Utilize uma ferramenta como `curl` ou um cliente HTTP em sua linguagem de programação favorita para enviar uma solicitação POST para o endpoint `/` da API com os parâmetros JSON no corpo da solicitação.

**Exemplo de solicitação com `curl`:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "theme": "Aventura na Floresta Encantada",
  "emotions": "Excitação, surpresa, alívio",
  "duration": 300
}' https://dawadocs.dataforsyningen.dk/dok/api
```

**4. Receba a Resposta:**

A resposta da API será um texto contendo a história gerada.

**Exemplo de resposta JSON:**

```json
"Os Amigos Queridos. Em um dia ensolarado, três amigos corajosos decidiram explorar a Floresta Encantada, um lugar cheio de magia e mistério. Eles riam e cantavam enquanto caminhavam, animados para descobrir o que os aguardava. De repente, um esquilo falante apareceu em seu caminho, surpreendendo-os! Eles continuaram sua jornada, encontrando pontes de arco-íris e árvores falantes pelo caminho. Quando uma tempestade repentina os pegou de surpresa, eles se abraçaram, mas logo encontraram um abrigo seguro em uma toca de coelho, enchendo-os de alívio."
```

**Dicas Adicionais:**

* Você pode usar ferramentas como Postman ou Insomnia para testar e explorar a API de forma interativa.
* A documentação completa da API está disponível em [https://www.linguee.es/portugues-espanol/traduccion/documenta%C3%A7%C3%A3o.html](https://www.linguee.es/portugues-espanol/traduccion/documenta%C3%A7%C3%A3o.html).
* Consulte a seção "Exemplos de Uso" no README para obter ideias de como usar a API para criar histórias incríveis.

**Exemplos de Uso**

* Gere uma história sobre um dragão amigável que ajuda crianças perdidas na floresta.
* Crie um conto de fadas sobre uma princesa corajosa que enfrenta um bruxo malvado.
* Escreva uma história inspiradora sobre um grupo de amigos que supera um desafio juntos.

## Conclusão

Este projeto oferece uma ferramenta poderosa e versátil para gerar histórias infantis criativas e educativas. Com sua interface amigável, recursos personalizáveis ​​e opções de integração, o projeto é ideal para educadores, desenvolvedores e qualquer pessoa que queira criar histórias mágicas para as crianças.

**Espero que você aproveite o projeto!**
