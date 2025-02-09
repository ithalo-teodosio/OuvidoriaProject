from ouvidoria_def import *

endSGBD = 'localhost'
userSGBD = 'root'
senhaSGBD = 'himegami110395'
schemaSGBD = 'ouvidoria_xyz'

connection = criarConexao(endSGBD, userSGBD, senhaSGBD, schemaSGBD)
if connection is None:
    print("Erro ao conectar ao banco de dados. Verifique se o banco 'ouvidoria_xyz' existe.")
    exit(1)

print("Bem-vindo a ouvidoria da Universidade XYZ!")

opcao = 1
while opcao != 7:

    print('''
        MENU:
        1- Listagem das manifestações;  
        2- Listagem de manifestações por tipo;
        3- Criar nova manifestação;
        4- Exibir quantidade de manifestações;
        5- Pesquisar manifestação por código;
        6- Excluir manifestação por código;
        7- Sair do sistema.
        ''')

    try:
        opcao = int(input('Digite a opção desejada: '))
    except ValueError:
        print("Entrada inválida! Digite um número.")
        continue

    if connection is None:
        print("Erro: Conexão com o banco de dados não estabelecida.")
        continue

    if opcao == 1:
        try:
            consultaListagem(connection)
        except Exception as e:
            print(f"Erro ao listar manifestações: {e}")
    elif opcao == 2:
        try:
            tipoEscolhido(connection)
        except Exception as e:
            print(f"Erro ao listar manifestações por tipo: {e}")
    elif opcao == 3:
        try:
            consultaInserir(connection)
        except Exception as e:
            print(f"Erro ao criar nova manifestação: {e}")
    elif opcao == 4:
        try:
            consultaQuantidade(connection)
        except Exception as e:
            print(f"Erro ao exibir quantidade de manifestações: {e}")
    elif opcao == 5:
        try:
            codigoPesquisa(connection)
        except Exception as e:
            print(f"Erro ao pesquisar manifestação por código: {e}")
    elif opcao == 6:
        try:
            codigoManifestacao(connection)
        except Exception as e:
            print(f"Erro ao excluir manifestação: {e}")
    elif opcao != 7:
        print('Opção inválida.')

print("\n====== Obrigado por usar o programa da Ouvidoria. Até a próxima! ======")

if connection:
    encerrarConexao(connection)