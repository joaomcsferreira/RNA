from random import choice


class Perceptron:
  def __init__(self, rad, bias, num_epocas, operacao, gabarito, amostras):
    self.rad = rad
    self.bias = bias
    self.num_epocas = num_epocas
    self.operacao = operacao
    self.gabarito = gabarito
    self.amostras = amostras

    # adicionar os valores dos pesos de forma aleatorio no range (-1, 1)
    self.pesos = [choice(dominio_pesos) for peso in range(3)]

  def treinar(self):
    """
      Realiza o calculo do neuronio para todos as entradas e saidas, responsavel por
      continuar atualizando os pesos até o objetivo desejado
    """
    epoca = 0

    while True:
      erro = True

      # loop para testar o neuronio em cada entrada
      for i, amostra in enumerate(self.amostras):
        aux = amostra[:]
        aux.insert(0, self.bias)

        soma = self.somatorio(aux)

        # verifica se é necessário realizar o ajuste de pesos
        if self.gabarito[self.operacao][i] != soma:
          self.ajustar_peso(aux, soma, self.gabarito[self.operacao][i])
          erro = False

      epoca += 1

      if erro or epoca >= self.num_epocas:
        break
  
  def testar(self, amostras):
    """
      Tem como objetivo testar o neuronio(somatorio) para uma entrada
    """
    x, y = amostras

    result = self.somatorio([-1, x, y])

    return result


  def somatorio(self, amostra):
    """
      A execução do neuronio funciona fazendo um somatorio de todos as estradas 
      multiplicadas pelos respectivos pesos e depois aplicada em uma função de transferencia
      onde ela verifica se o valor esta mais proximo de 0 ou de 1
    """
    soma = sum([(amostra[i] * self.pesos[i]) for i in range(3)])

    return 1 if soma > 0 else 0

  def ajustar_peso(self, amostra, soma, gabarito):
    """
      Utilizando a regra DELTA para atualizar os pesos -> wi = wi + N(t - y)xi
    """
    self.pesos = [(self.pesos[i] + (self.rad * gabarito - soma) * amostra[i]) for i in range(3)]