import requests 

cnpj = input("Insira um cnpj: ") 
url = "https://www.receitaws.com.br/v1/cnpj/" + cnpj

resposta = requests.get(url) 
data = resposta.json() 
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
