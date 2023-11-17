import json

def cadastroEnfermeiros():
    while True:
            profissional = {}
            print("Página de Cadastro")

            nome = input("Escolha seu nome de usuário: ").lower().strip()
            while nome == "":
                print("Campo em branco!")
                nome = input("Escolha seu nome de usuário: ").lower().strip()
            senha = input("Escolha sua senha: ").lower().strip()
            while senha == "":
                print("Campo em branco!")
                senha = input("Escolha sua senha: ").lower().strip()


            profissional = {"nome de usuario": nome, "senha": senha}

            with open("mudanca_decubito.json","r",encoding="utf-8") as file:
                cadastros = json.load(file)

                for key,lista in cadastros.items():
                    if key == "profissionais":
                        lista.append(profissional)

                        with open("mudanca_decubito.json","w",encoding="utf-8") as file:
                            json.dump(cadastros,file,indent=4,ensure_ascii=False)
            
            print("Cadastro do(a) enfermeiro(a) realizado com sucesso!")
            break



def areaLogin(username):
    while True:

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



def validacaoLogin():
    while True:
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

                nome = input("\nNome de usuário: ").lower().strip()
                senha = input("Senha: ").lower().strip()

                with open("mudanca_decubito.json","r",encoding="utf-8") as file:
                    cadastros = json.load(file)

                    cont1 = 0
                    cont2 = 0

                    for key,lista in cadastros.items():  # validando username e senha com arquivo json
                        if key == "profissionais":
                            for profissional in lista:
                                cont1 = 0
                                cont2 = 0
                               
                                for chave,valor in profissional.items():
                                    if chave == "nome de usuario":
                                        if valor == nome:
                                            cont1 = 1
                                    elif chave == "senha":
                                        if valor == senha:
                                            cont2 = 1
                                    
                                if cont1 == 1 and cont2 == 1:
                                    print("\nLogin Realizado!")
                                    areaLogin(nome)
                                    break

                            if cont1 == 0 or cont2 == 0:
                                print("\nUsuário ou senha incorreto")
                                break



while True:
    print("""

0 - Sair;
          
1 - Faça seu cadastro;
          
2 - Login Usuário;

""")
    
    escolha = int(input("Escolha: "))

    if escolha == 0:
        print("Programa finalizado!")
        break
    elif escolha == 1:
        cadastroEnfermeiros()
    elif escolha == 2:
        validacaoLogin()
                                    
              
                



    






