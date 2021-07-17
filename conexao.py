from db import EmpresaCrud, criarBD
import requests
import os.path

def buscarCadastrarEmpresa():
    cnpj = input("Insira um cnpj: ")
    url = "https://www.receitaws.com.br/v1/cnpj/" + cnpj 

    resposta = requests.get(url) 
    data = resposta.json()
    if(data["status"] == "ERROR"):
        print("Cnpj Invalido")
    else:
        ap = data["atividade_principal"][0]  
        ativs_sec = data["atividades_secundarias"] 

        EmpresaCrud.add(data)  
        print("Empresa cadastrada")

if not os.path.exists('empresas.db'):
    print('criou db')
    criarBD()
else:
    print('não criou db')

while True:
    print("""
        Opções:

        0 - Sair
        1 - Cadastrar Empresa
        2 - Listas Empresas
        3 - Deletar empresa
        4 - Atualizar dados da empresa
        5 - serviços

    """)        
    opcao = input('Insira a opcao: ')

    if(opcao == "0"):
        break # Sai do while e o programa para
    elif(opcao == "1"):
        print("""
        Opções de Cadastro:
            1 - Buscar por cnpj 
            2 - Manual
        """)
        opCadastro = input("Insira a opção: ")
        if(opCadastro == "1"):
            buscarCadastrarEmpresa()
        elif(opCadastro == "2"):
            cnpj = input("Digite seu cnpj: ")
            nome = input("Digite seu nome: ")
            uf = input("Digite seu UF: ")
            telefone = input("Digite seu telefone: ")
            email = input ("Digite seu email: ")

            objCadastro = {
                "nome": nome,
                "cnpj": cnpj,
                "uf": uf,
                "telefone": telefone,
                "email": email
            }

            EmpresaCrud.add(objCadastro)

    elif(opcao == "2"):
        EmpresaCrud.listar()
    elif(opcao == "3"):
        EmpresaCrud.listar()
        empresa_id = input ("Digite o Id da empresa: ")
        EmpresaCrud.deletar(empresa_id) 
        print("Empresa deletada")

