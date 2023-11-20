from modulo_matriz import cadastroEnfermeiros,validacaoLogin


while True:
    try:
        print("""
Menu Principal
                  
0 - Sair;
                  
1 - Faça seu cadastro;
                  
2 - Login Usuário;
""")

        escolha = int(input("Escolha: \n"))

        if escolha == 0:
            print("Programa finalizado!")
            break
        elif escolha == 1:
            cadastroEnfermeiros()
        elif escolha == 2:
            validacaoLogin()
        else:
            print("Digite 0, 1 ou 2 para a escolha ser válida!")
    except ValueError:
        print("Valor inválido digitado!")
    except Exception:
        print("Ocorreu um erro inesperado")
              
                



    






