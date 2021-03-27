from limite.tela_amigo import TelaAmigo
from entidade.amigo import Amigo

class ControladorAmigos():

  def __init__(self, controlador_sistema):

    self.__amigos = []

    self.__tela_amigo = TelaAmigo()
    self.__controlador_sistema = controlador_sistema

  def incluir_amigo(self):
    dados_amigo = self.__tela_amigo.pega_dados_amigo()

    amigo = Amigo(dados_amigo["nome"], dados_amigo["telefone"])

    self.__amigos.append(amigo)

  def lista_amigos(self):
    for amigo in self.__amigos:
      self.__tela_amigo.mostra_amigo({"nome": amigo.nome, "telefone": amigo.telefone})

  def abre_tela(self):
    #Atenção: código incompleto: adicionar funcões para todas as opções da tela
    lista_opcoes = {1: self.incluir_amigo, 3: self.lista_amigos}

    continua = True
    while continua:
      lista_opcoes[self.__tela_amigo.tela_opcoes()]()


