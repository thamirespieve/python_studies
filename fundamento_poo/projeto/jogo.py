#Personagem: classe mae
#Hero: controlado pelo usuario
#Inimigo: adversario do usuario
import random
class Personagem:
  def __init__(self,nome,vida,nivel):
    self.__nome=nome
    self.__vida=vida
    self.__nivel=nivel
  
  def get_nome(self):
    return self.__nome
  def get_vida(self):
    return self.__vida
  def get_nivel(self):
    return self.__nivel
  def exibir_detalhes(self):
    return f"Nome: {self.get_nome()}\nVida:{self.get_vida()}\nNível:{self.get_nivel()}"
  
  def receber_ataque(self,dano):
      self.__vida -= dano
      if self.__vida <= 0:
        self.__vida=0

  def atacar(self,alvo):
    dano = random.randint(self.get_nivel()*2,self.get_nivel()*4)
    alvo.receber_ataque(dano)
    print(f"{self.get_nome()} atacaou {alvo.get_nome()} e causou {dano} de dano!")
  
class Heroi(Personagem):
  def __init__(self, nome, vida, nivel,habilidade):
    super().__init__(nome, vida, nivel)
    self.__habilidade = habilidade

  def get_habilidade(self):
    return self.__habilidade
  
  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()}\nHabilidade:{self.get_habilidade()}"
  
  def ataque_especial(self,alvo):
    dano = random.randint(self.get_nivel()*5,self.get_nivel()*8)
    alvo.receber_ataque(dano)
    print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano")

class Inimigo(Personagem):
  def __init__(self, nome, vida, nivel,tipo):
    super().__init__(nome, vida, nivel)
    self.__tipo = tipo

  def get_tipo(self):
    return self.__tipo
  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()}\nTipo:{self.get_tipo()}"

class Jogo:
  """Class mantedora do jogo"""
  def __init__(self):
    self.heroi = Heroi("Heroi",100,5,"super força")
    self.inimigo=Inimigo("Morcego",80,5,"voador")
  
  def iniciar_batalha(self):
    print("Iniciando batalha!")
    while self.heroi.get_vida() > 0 and self.inimigo.get_vida()>0:
      print("\nDetalhes do Personagens:")
      print(self.heroi.exibir_detalhes())
      print(self.inimigo.exibir_detalhes())

      input("Pressione Enter para atacar....")
      escolha = input("Escolha (1 - Ataque normal, 2-Ataque especial)")

      if escolha =='1':
        self.heroi.atacar(self.inimigo)
      elif escolha =='2':
        self.heroi.ataque_especial(self.inimigo)
      else:
        print("Escolha inválida")

      if self.inimigo.get_vida()>0:
        self.inimigo.atacar(self.heroi)

    if self.heroi.get_vida()>0:
      print('\nParabens, você venceu a batalha!')
    else:
      print('\n Você foi derrotado.')


#Instancia do jogo
jogo = Jogo()
jogo.iniciar_batalha()
