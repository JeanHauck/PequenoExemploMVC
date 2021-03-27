
class Amigo:
  def __init__(self, nome: str, telefone: str):
    self.__nome = nome
    self.__telefone = telefone

  @property
  def nome(self):
    return self.__nome

  @property
  def telefone(self):
    return self.__telefone
