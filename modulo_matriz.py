import json
import requests
from random import randint



def cadastroEnfermeiros() -> None:
    """
    Função que pede os dados do cuidados, para efetuar seu cadastro no programa, deixando o usuário cadastrado logar com suas informações na parte do login. A senha aleatória é gerada por uma API que gera uma senha aleatória com o comprimento de 16 caracteres. Observação: se o usuário escolher por gerar a senha aleatóriamente, ele deve pegar a senha no arquivo json e digitar no terminal para efetuar o login.
    """
    while True:
        profissional = {}
        print("Página de Cadastro")

        nome = input("Escolha seu nome de usuário: ").upper().strip()
        while nome == "":
            print("Campo em branco!")
            nome = input("Escolha seu nome de usuário: ").upper().strip()
        senha = input("Escolha sua senha (00 para gerar uma senha forte: ")
        if senha == "00":
            length = '16'
            api_url = 'https://api.api-ninjas.com/v1/passwordgenerator?length={}'.format(length)
            response = requests.get(api_url, headers={'X-Api-Key': 'RWg4SA2qGApINIIpaRisDQ==zay7vlJQ2kSpFBzd'})
            if response.status_code == requests.codes.ok:
                password = response.json()
                for value in password.values():
                    senha = value
            else:
                print("Error:", response.status_code, response.text)
                print("Digite sua senha manualmente!")
        while senha == "":
            print("Campo em branco!")
            senha = input("Escolha sua senha (00 para gerar uma senha forte): ")
            if senha == "00":
                length = '16'
                api_url = f'https://api.api-ninjas.com/v1/passwordgenerator?length={length}'.format(length)
                response = requests.get(api_url, headers={'X-Api-Key':     'RWg4SA2qGApINIIpaRisDQ==zay7vlJQ2kSpFBzd'})
                if response.status_code == requests.codes.ok:
                    password = response.json()
                    for value in password.values():
                        senha = value
                else:
                    print("Error:", response.status_code, response.text)
                    print("Digite sua senha manualmente!")


        profissional = {"nome de usuario": nome, "senha": senha}

        with open("mudanca_decubito.json","r",encoding="utf-8") as file:
            cadastros = json.load(file)

            for key,lista in cadastros.items():
                if key == "profissionais":
                    lista.append(profissional)

                    with open("mudanca_decubito.json","w",encoding="utf-8") as file:
                        json.dump(cadastros,file,indent=4,ensure_ascii=False)
        
        print("Cadastro do(a) cuidador(a) realizado com sucesso!")
        break
    


def infoPaciente() -> None:
    """
    Função que pede ao usuário o nome do paciente que deseja verificar informações, informando seus dados pessoais e informações sobre sua situação relacionada a mudança de decúbito. Caso o nome digitado não seja encontrado, imprime a mensagem no terminal. Biblioteca random utilizada para simular o tempo marcado desde a última mudança de decúbito.
    """
    nome = input("Nome do paciente: ").upper().strip()

    with open("mudanca_decubito.json","r",encoding="utf-8") as file:
        dicionario = json.load(file)

        hora = randint(0,4)  # gera o valor da hora entre 0 e 4
        minuto = randint(0,59)  # gera o valor do minuto entre 0 e 59

        cont = 0
        for chave,lista in dicionario.items():
            if chave == "pacientes":
                for paciente in lista:
                    for chave, valor in paciente.items():
                        if chave == "nome" and valor == nome:
                            cont += 1
                            if hora == 0 and minuto == 0: # 0:00h
                                print("Mudança de posição acabou de ser feita! Realizar daqui 2 horas.")
                            elif hora >= 0 and hora < 2: # > 0:00h and < 2:00h
                                print(f"""
Nome do(a) paciente: {paciente['nome']}

Idade do(a) paciente: {paciente['idade']}

Peso do(a) paciente {paciente['peso']}

Tempo percorrido desde a última mudança de decúbito realizada: {hora}:{minuto}h

Tempo até a próxima mudança: {1 - hora}:{60 - minuto}h

\033[1;32mNão é necessário a mudança de posição do paciente!\033[m
""")    
                            elif hora == 2 and minuto == 0:  # 2:00h
                                print("Hora de realizar a mudança de decúbito")
                            elif hora >= 2 and minuto > 0:  # > 2:00h
                                print(f"""
Nome do(a) paciente: {paciente['nome']}

Idade do(a) paciente: {paciente['idade']}

Peso do(a) paciente {paciente['peso']}

Tempo percorrido desde a última mudança de decúbito realizada: {hora}:{minuto}h

Tempo de atraso para realizar a troca de posição: {hora - 2}:{minuto}h

\033[1;31mTrocar o paciente de posição!\033[m
""")               
                if cont == 0:
                    print("Não foi encontrado nenhum paciente com esse nome!")



def listarPaciente() -> None:
    """
    Imprime no terminal a lista com o nome dos pacientes que estão cadastrados, caso não tenha nenhum imprime a mensagem que nenhum paciente está cadastrado.
    """
    with open("mudanca_decubito.json","r",encoding="utf-8") as file:
        dicionario = json.load(file)

        cont = 0
        for chave,lista in dicionario.items():
            if chave == "pacientes":
                for paciente in lista:
                    cont += 1
                    print(f"{cont} - {paciente['nome']}")
                if len(lista) == 0:
                    print("\nNenhum paciente cadastrado!")



def adicionarPaciente() -> None:
    """
    Função que adiciona um novo paciente caso os campos digitados forem válidos.
    """
    while True:
        try:
            print("\nInformações do Paciente\n")
            nome = input("Nome: ").upper().strip()
            while nome == "":
                print("Campo em branco!")
                nome = input("Nome: ").upper().strip()
            idade = int(input("Idade: "))
            peso = float(input("Peso(kg): "))

            with open("mudanca_decubito.json","r",encoding="utf-8") as file:
                dicionario = json.load(file)

                paciente = {"nome":nome,"idade":idade,"peso":peso}

                for chave, lista in dicionario.items():
                    if chave == "pacientes":
                        lista.append(paciente)

                with open("mudanca_decubito.json","w",encoding="utf-8") as file:
                    json.dump(dicionario,file,indent=4,ensure_ascii=False)

                print("Paciente cadastrado com sucesso!")
                break
        except ValueError:
            print("Valor digitado inválido!")
        except Exception:
            print("Ocorreu um erro inesperado!")



def editarPaciente() -> None:
    """
    Função que pede para o usuário digitar se quer continuar ou sair da edição, caso escolha sair direciona o usuário de volta para a home, se continuar pede para o usuário digitar o nome do paciente que deseja editar, caso o usuário digitado esteja cadastrado, disponibiliza campos para fazer as edições, se não estiver cadastrado, imprime uma mensagem dizendo que nenhum paciente com o nome foi encontrado.
    """
    while True:
        try:
            escolha = int(input("\nDigite 0 para sair ou 1 para editar paciente: "))

            if escolha == 0:
                break
            elif escolha == 1:

                paciente_nome = input("\nNome do paciente: ").upper().strip()

                with open("mudanca_decubito.json","r",encoding="utf-8") as file:
                    dicionario = json.load(file)

                    cont = 0
                    for chave, lista in dicionario.items():
                        if chave == "pacientes":
                            for paciente in lista:
                                for chave,valor in paciente.items():
                                    if chave == "nome" and valor == paciente_nome:
                                        cont = 1
                                        print(f"\nEditando Informações do paciente {paciente_nome}")
                                        paciente["nome"] = input("Nome: ").upper().strip()
                                        while paciente['nome'] == "":
                                            print("Campo em branco!")
                                            paciente["nome"] = input("Nome: ").upper().strip()
                                        paciente["idade"] = int(input("Idade: "))
                                        paciente["peso"] = float(input("Peso (kg): "))


                                        with open("mudanca_decubito.json","w",encoding="utf-8") as file:
                                            json.dump(dicionario,file,indent=4,ensure_ascii=False)
                                        print("\nPaciente editado com sucesso")
                                        break
                            if cont == 0:       
                                print(f"\nNenhum paciente encontrado!")
            else:
                print("Digite 0 ou 1 apenas!")
        except ValueError:
            print("Valor digitado inválido!")
        except Exception:
            print("Ocorreu um erro inesperado!")



def removerPaciente() -> None:
    """
    Função que pede ao usuário escolher o paciente que deseja realizar a exclusão e, caso o paciente estiver cadastrado, pede para confirmar a exclusão, efetuando logo em seguida ou cancelando.
    """
    nome = input("Nome do paciente que deseja excluir: ").upper().strip()

    with open("mudanca_decubito.json","r",encoding="utf-8") as file:
        dicionario = json.load(file)
        cont = 0
        for chave,lista in dicionario.items():
            if chave == "pacientes":
                for paciente in lista:
                    for chave,valor in paciente.items():
                        if chave == "nome" and valor == nome:  # se na chave nome for o nome digitado pelo usuário
                            cont = 1
                            while True:
                                try:
                                    print(f"""
Tem certeza que deseja excluir o(a) paciente {nome}?

0 - Cancelar;

1 - Tenho certeza.
""")
                                    escolha = int(input("Escolha: "))
                                    if escolha == 0:
                                        print("\nVoltando para home...")
                                        break
                                    elif escolha == 1:
                                        lista.remove(paciente)
                                        with open("mudanca_decubito.json","w",encoding="utf-8") as file:
                                            json.dump(dicionario,file,indent=4,ensure_ascii=False)
                                        print("Paciente excluído com sucesso!")
                                        break
                                    else:
                                        print("Digite apenas 0 ou 1!")
                                except ValueError:
                                    print("Valor digitado inválido!")
                                except Exception:
                                    print("Ocorreu um erro inesperado!")
                if cont == 0:
                    print("Paciente não encontrado!")



def areaLogin(username: str) -> None:
    """
    Função que recebe como parâmetro um nome de usuário para identificar quem está efetuando o login, apresentando um menu de opções para o usuário gerir melhor pacientes.
    """
    while True:
        try:
            print(f"""

Olá, {username}

0 - Logout;

1 - Sobre a mudança de decúbito;

2 - Informações sobre um paciente;

3 - Lista de pacientes monitorados;

4 - Adicionar novo paciente;

5 - Editar dados do paciente;

6 - Remover paciente.
""")
            escolha = int(input("Escolha: "))

            if escolha == 0:
                print("Logout")
                break
            elif escolha == 1:
                print("A mudança de decúbito consiste em movimentar e mudar a posição do paciente acamado afim de proporcionar  maior conforto e evitar complicações devido à imobilidade prolongada, tais como: descomprimir as áreas de    proeminências ósseas, prevenir complicações pulmonares, úlceras por pressão e estimular a circulação sanguínea.    Recomenda-se a troca de posição do paciente a cada 2 horas.")
            elif escolha == 2:
                infoPaciente()
            elif escolha == 3:
                listarPaciente()
            elif escolha == 4:
                adicionarPaciente()
            elif escolha == 5:
                editarPaciente()
            elif escolha == 6:
                removerPaciente()
            else:
                print("\nEscolha 0, 1, 2, 3, 4, 5 ou 6 para a escolha ser válida!")
        except ValueError:
            print("\nValor inválido digitado!")
        except Exception:
            print("\nOcorreu um erro inesperado!")



def validacaoLogin() -> None:
    """
    Função que mostra um menu de opções para o usuário escolher entre voltar ao menu principal ou efetuar o login. Retorna ao menu principal se for a opção escolhida ou faz a validação do usuário e senha caso a escolha seja de efetuar o login, direcionando o usuário para a área dele, caso seja autenticado, ou voltando para o menu de escolha, caso os campos digitados sejam inválidos.
    """
    while True:
        try:
            print("""

0 - Voltar;
                  
1 - Efetuar Login.
                  
""")
            escolha = int(input("Digite sua escolha: "))

            if escolha == 0:
                print("voltando ao menu principal")
                break
            elif escolha == 1:
                print("\nLogin")

                nome = input("\nNome de usuário: ").upper().strip()
                senha = input("Senha: ")

                with open("mudanca_decubito.json","r",encoding="utf-8") as file:
                    cadastros = json.load(file)

                    cont1 = 0
                    cont2 = 0

                    for key,lista in cadastros.items():  # validando username e senha com arquivo json
                        if key == "profissionais": 
                            for profissional in lista:  # percorre os dicionários(profissionais) dentro da lista
                                for chave,valor in profissional.items():
                                    if chave == "nome de usuario" and valor == nome:
                                        cont1 = 1

                                    elif chave == "senha" and valor == senha:
                                        cont2 = 1

                                if cont1 == 1 and cont2 == 1:  # se o usuário e senha tiverem corretos
                                    print("\nLogin Realizado!")
                                    areaLogin(nome)
                                    break
                                
                                cont1 = 0  # zera caso apenas o usuario estiver correto
                                cont2 = 0  # zera caso apenas a senha digitada estiver correta

                            if cont1 == 0 or cont2 == 0: # caso usuario ou senha estiver incorreta
                                print("\nUsuário ou senha incorreto")
                                break
            else:
                print("Digite 0 ou 1 para a escolha ser válida!")
        except ValueError:
            print("Valor digitado é inválido!")
        except Exception:
            print("Ocorreu um erro inesperado!")                                        
                                    


