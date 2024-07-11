import request
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = request.get(url)

if response.status_code() == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for dado in dados_json:
        nome_restaurante = dado['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []
        dados_restaurante[nome_restaurante].append({
            "item":dado['Item'],
            "preco":dado['price'],
            "descricao":dado['description']
        })
        
else:
    print('Erro de request')
    
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_arquivo = f'{nome_restaurante}.json'
    with open(nome_arquivo,'w') as file:
        json.dump(dados,file,indent=4)