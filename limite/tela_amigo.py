
class TelaAmigo():

  def tela_opcoes(self):
    print("-------- AMIGOS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Amigo")
    print("2 - Alterar Amigo")
    print("3 - Listar Amigos")
    print("4 - Excluir Amigo")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  def pega_dados_amigo(self):
    print("-------- INCLUIR AMIGO ----------")
    nome = input("Nome: ")
    telefone = input("Telefone: ")

    return {"nome": nome, "telefone": telefone}

  def mostra_amigo(self, dados_amigo):
    print("NOME DO AMIGO: ", dados_amigo["nome"])
    print("FONE DO AMIGO: ", dados_amigo["telefone"])

