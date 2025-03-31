from operacoesbd import *

endSGBD = 'localhost'
userSGBD = 'root'
senhaSGBD = 'SUA_SENHA'
schemaSGBD = 'ouvidoria_xyz'

connection = criarConexao(endSGBD, userSGBD, senhaSGBD, schemaSGBD)

print("OUVIDORIA UNIVERSIDADE XYZ")

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

opcao = int(input("Digite a opção desejada: "))

while opcao != 7:
    if opcao == 1:
        consultaListagem = 'select * from ouvidoria'
        manifestacoes = listarBancoDados(connection, consultaListagem)
        if len(manifestacoes) > 0:
            print("Lista de manifestações: ")
            for i in manifestacoes:
                print(f"\n Código: {i[1]}. \n Autor: {i[2]}. \n Tipo {i[3]}. \n Manifestação: {i[4]}.")
        else:
            print("Não há manifestações a serem exibidas.")

    elif opcao == 2:
        tipoEscolhido = int(input("Selecione o tipo de manifestação que deseja consultar: \n 1- Crítica; 2- Elogio; 3- Sugestão."))

        if tipoEscolhido == 1:
            tipo_lista = "Crítica"
        elif tipoEscolhido == 2:
            tipo_lista = "Elogio"
        elif tipoEscolhido == 3:
            tipo_lista = "Sugestão"
        else:
            print("Opção inválida! Por gentileza, selecione uma das opções apresentadas.")
            continue

        consultaPorTipo = 'select * from ouvidoria where tipo_lista = %s'
        manifestacoesPorTipo = listarBancoDados(connection, consultaPorTipo, tipo_lista)
        if len(manifestacoesPorTipo) > 0:
            print(f"Manifestação do tipo '{tipo_lista}': ")
            for i in manifestacoes:
                print(f"\n Código: {i[1]}. \n Autor: {i[2]}. \n Tipo {i[3]}. \n Manifestação: {i[4]}.")
        else:
            print(f"Não existem manifestações do tipo '{tipo_lista}'.")

    elif opcao == 3:
        consultaInserir = 'insert into ouvidoria (autor, tipo, manifestacao) values (%s,%s,%s)'
        autorManifestacao = input("Digite o seu nome: ")
        tipoManifestacaoInt = int(input("Digite o tipo de manifestação: 1 - Crítica; 2 - Elogio; 3 - Sugestão: "))
        descManifestacao = input("Digite sua manifestação: ")

        if tipoManifestacaoInt == 1:
            tipoManifestacao = "Crítica"
        elif tipoManifestacaoInt == 2:
            tipoManifestacao = "Elogio"
        elif tipoManifestacaoInt == 3:
            tipoManifestacao = "Sugestão"
        else:
            print("Opção inválida! Tente novamente utilizando umas das opções válidas apresentadas.")
            continue

        dados = [autorManifestacao, tipoManifestacao, descManifestacao]
        insertNoBancoDados(connection, consultaInserir, dados)
        print("Manifestação inserida com sucesso!")

    elif opcao == 4:
        consultaQuantidade = 'select count(*) from ouvidoria'
        quantidade = listarBancoDados(connection, consultaQuantidade)

        if len(quantidade) > 0:
            print(f"Atualmente temos {quantidade[0][0]} manifestações registradas.")
        else:
            print("Ainda não há manifestações no sistema.")

    elif opcao == 5:
        codigoPesquisa = int(input("Digite o código da sua pesquisa: "))
        consultaListagem = 'select * from ouvidoria where codigo = %s'
        dados = [codigoPesquisa]

        ouvidoria = listarBancoDados(connection, consultaListagem, dados)
        if len(ouvidoria) > 0:
            for i in ouvidoria:
                print(f"\n Código: {i[1]}. \n Autor: {i[2]}. \n Tipo {i[3]}. \n Manifestação: {i[4]}.")
        else:
            print("Não há manifestações com o código escolhido.")

    elif opcao == 6:
        codigoManifestacao = int(input("Digite o código da manifestação que deseja excluir: "))
        consultaRemocao = 'delete from ouvidoria where codigo = %s'
        dados = [codigoManifestacao]

        linhasAfetadas = excluirBancoDados(connection, consultaRemocao, dados)
        if len(linhasAfetadas) > 0:
            print(f"Manifestação de código {codigoManifestacao} excluído com sucesso!")
        else:
            print(f"Não existe manifestação no código {codigoManifestacao} a ser excluído.")

    else:
        print("Opção inválida! Por gentileza, selecionar opção dentro do espectro apresentado no menu!")

    opcao = int(input("Digite a opção desejada: "))

encerrarConexao(connection)

print("Obrigado por utilizar o nosso sistema de ouvidoria em prol da melhoria do serviço da Universidade XYZ.")