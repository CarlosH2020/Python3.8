#  Sistema de Login em Python
lists = [
    'root',
    'toor']
lists2 = []

while True:
    #  Menu de Login:
    print('='*13)
    print(' Fazer login')
    print('='*13)
    opc = input('Deseja fazer cadastro:')
    if opc == 'N' or opc == 'n':
        login = input('Login:')
        passwd = input('Password:')

        #  Verificação de usuário usuário:
        if login in lists and passwd in lists:
            if login == 'root' and passwd == 'toor':
                print('[$$] Logado como super usuário..')
                excluir = input('Digite (X) para excluir um user:')
                if excluir == 'X' or excluir == 'x':
                    print(lists2)
                    #  Remove um user da lista:
                    exuser = (input('excluir:'))
                    lists2.remove(exuser)
                    print(f'O user {exuser} foi excluido.')

        elif login in lists2 and passwd in lists2:
            print('[#] Logado com sucesso...')
            break
        else:
            print('[x] Login ou senha errado...')

    elif opc == 'S' or opc == 's':
        #  Faz cadastro de login de um novo usuário:
        cad = input('Cadastro Login:')
        cadsenha = input('Cadastro Password:')
        #  Verifica se já existe um user com esse ID:
        if cad in lists2:
            print('Esse login já está cadastrado tente outro!')
        else:  # ADD o login e senha:
            lists2.append(cad)
            lists2.append(cadsenha)









