def menu ():
    cadastro = []
    while True:

        print("\n ----------CADASTRO--DE--FUNCIONARIO------------")
        print("[1] CADASTRAR PESSOA")
        print("[2] LISTAR PESSOA")
        print("[3] EXCLUIR PESSOA")
        print("[0] ")

        opcao = input("ESCOLHA UMA OPÇÃO: ")

        if opcao == '1':
            novo_nome = input("DIGITE O NOME DA PESSOA ")
            cadastro.append(novo_nome)
            print(f"Usuário {novo_nome} foi adicionado com sucesso")
        
        elif opcao == '2':
            print("n/Lista DE CADASTRADOS: ")
            for i, nome in enumerate (cadastro, start=1):
                print(f"{i}. {nome}")
        elif opcao == '3':
            excluir_nome = input("DIGITE O NOME PARA EXCLUIR: ")
            if excluir_nome in cadastro: 
                cadastro.remove(excluir_nome)
                print(f"{excluir_nome} FOI REMOVIDO ")
            else:   
                print("nome não encontrado. ")        
        
        elif opcao == '0':
            print("SAINDO.........")
            break 
        else:
            print("!!!!!! OPÇÃO INVALIDA. TENTE NOVAMENTE!!!!!")

menu()