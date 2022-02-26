

if __name__ == '__main__':
  gabarito = [[0, 1, 1, 1], # ou
            [0, 0, 0, 1], # e
            [1, 0, 0, 0], # não ou
            [1, 1, 1, 0], # não e
            [0, 1, 1, 0]] # ou exclusivo

  amostras = [[0, 0], [1, 0], [0, 1], [1, 1]]

  dominio_pesos = [-1, 0, 1]

  game = Game(gabarito, amostras)

  game.menu()