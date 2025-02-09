from operacoesbd import *


# Função para listar todas as manifestações
def consultaListagem(connection):
    consulta = 'SELECT * FROM ouvidoria'
    manifestacoes = listarBancoDados(connection, consulta)

    if len(manifestacoes) > 0:
        print("Lista de manifestações: ")
        for manifestacao in manifestacoes:
            print(
                f"\nCódigo: {manifestacao[0]} | Autor: {manifestacao[1]} | Tipo: {manifestacao[2]} | Manifestação: {manifestacao[3]}")
    else:
        print("Não há manifestações a serem exibidas.")


# Função para listar manifestações por tipo
def tipoEscolhido(connection):
    tipoEscolhido = int(
        input("Selecione o tipo de manifestação que deseja consultar: \n 1 - Crítica; 2 - Elogio; 3 - Sugestão: "))

    if tipoEscolhido == 1:
        tipo = "Crítica"
    elif tipoEscolhido == 2:
        tipo = "Elogio"
    elif tipoEscolhido == 3:
        tipo = "Sugestão"
    else:
        print("Opção inválida!")
        return

    consultaPorTipo = 'SELECT * FROM ouvidoria WHERE tipo = %s'
    manifestacoesPorTipo = listarBancoDados(connection, consultaPorTipo, (tipo,))

    if len(manifestacoesPorTipo) > 0:
        print(f"\nManifestações do tipo '{tipo}':")
        for manifestacao in manifestacoesPorTipo:
            print(
                f"\nCódigo: {manifestacao[0]} | Autor: {manifestacao[1]} | Tipo: {manifestacao[2]} | Manifestação: {manifestacao[3]}")
    else:
        print(f"Não existem manifestações do tipo '{tipo}'.")


# Função para criar nova manifestação
def consultaInserir(connection):
    autor = input("Digite o seu nome: ")
    tipoInt = int(input("Digite o tipo de manifestação: 1 - Crítica; 2 - Elogio; 3 - Sugestão: "))
    descricao = input("Digite sua manifestação: ")

    if tipoInt == 1:
        tipo = "Crítica"
    elif tipoInt == 2:
        tipo = "Elogio"
    elif tipoInt == 3:
        tipo = "Sugestão"
    else:
        print("Opção inválida!")
        return

    consultaInserir = 'INSERT INTO ouvidoria (autor, tipo, manifestacao) VALUES (%s, %s, %s)'
    dados = (autor, tipo, descricao)
    insertNoBancoDados(connection, consultaInserir, dados)
    print("Manifestação registrada com sucesso!")


# Função para exibir a quantidade de manifestações no banco
def consultaQuantidade(connection):
    consultaQuantidade = 'SELECT COUNT(*) FROM ouvidoria'
    quantidade = listarBancoDados(connection, consultaQuantidade)

    if quantidade:
        print(f"Total de manifestações: {quantidade[0][0]}")
    else:
        print("Erro ao contar as manifestações.")


# Função para pesquisar manifestação por código
def codigoPesquisa(connection):
    codigo = int(input("Digite o código da manifestação que deseja pesquisar: "))
    consultaPesquisa = 'SELECT * FROM ouvidoria WHERE codigo = %s'
    dados = (codigo,)
    manifestacao = listarBancoDados(connection, consultaPesquisa, dados)

    if manifestacao:
        for i in manifestacao:
            print(f"\nCódigo: {i[0]} | Autor: {i[1]} | Tipo: {i[2]} | Manifestação: {i[3]}")
    else:
        print("Manifestação não encontrada.")


# Função para excluir manifestação por código
def codigoManifestacao(connection):
    codigo = int(input("Digite o código da manifestação que deseja excluir: "))
    consultaRemover = 'DELETE FROM ouvidoria WHERE codigo = %s'
    dados = (codigo,)
    linhasAfetadas = excluirBancoDados(connection, consultaRemover, dados)

    if linhasAfetadas > 0:
        print(f"Manifestação com código {codigo} excluída com sucesso!")
    else:
        print("Não foi possível excluir a manifestação. Código não encontrado.")