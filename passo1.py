import requests #importar a biblioteca 

cnpj = input("Insira um cnpj: ") #input para pedir cnpj
url = "https://www.receitaws.com.br/v1/cnpj/" + cnpj #requisição da url para consultar o cnpj

resposta = requests.get(url) #buscar na url cnpj
data = resposta.json() #trazer a resposta num formato json
print(resposta)
print(data)
if(data["status"] == "ERROR"):
    print("Cnpj Invalido")
else: 
    print("Nome =", data["nome"])
    print("Telefone =", data["telefone"])
    print("Email =", data["email"])
    print("UF =", data["uf"])
    print("Data de Abertura =", data["abertura"]) 

    ap = data["atividade_principal"][0]

    print("Atividade Principal")
    print("\t",ap["code"],"-",ap["text"])




    ativs_sec = data["atividades_secundarias"]
    print("Atividade Secundaria")
    for atividade in ativs_sec:
        print("\t",atividade["code"],"-",atividade["text"]) 