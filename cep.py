import requests

integrantes = {
    "Mario": "11635708",
    "Dione": "11633422",
    "Cecilia": "04013001"
}

for nome, cep in integrantes.items():
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        cidade = dados.get("localidade", "cidade não encontrada")
        print(f"{nome} mora em {cidade}")

else:
    print (f"não foi possivel localizar os dados de {nome}.")