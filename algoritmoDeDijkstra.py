
def caminhoMaisCurto(pai, ondeSeChegou):
  noAtual = ondeSeChegou
  caminho = [noAtual]
  while pai[noAtual] is not None:
    caminho.append(pai[noAtual])
    noAtual = pai[noAtual]
  caminho.reverse()
  return print(caminho)


def verticeMenorCusto(custos):
  return min(custos, key=custos.get)


def algoritmoDeDijkstra(graph, pontoDePartida, ondeSeQuerChegar, custos):
  paiVerticeAtual = {}
  paiVerticeAtual[pontoDePartida] = None
  if pontoDePartida == ondeSeQuerChegar:
    return print([ondeSeQuerChegar])
  if graph and pontoDePartida and ondeSeQuerChegar:
    # verticesVizinhos = graph[pontoDePartida].keys()
    # for vertice in verticesVizinhos:
    #  if graph[pontoDePartida][vertice] < custos[vertice]:
    #    custos[vertice] = graph[pontoDePartida][vertice]
    custos[pontoDePartida] = 0
    ##
    verificados = []
    # verificados = [pontoDePartida]
    # pontoDePartida = verticeMenorCusto(custos)
    while pontoDePartida is not None:
      custo = custos[pontoDePartida]
      verticesVizinhos = graph[pontoDePartida].keys()
      for vertice in verticesVizinhos:
        # aqui talvez tenha um erro
        novoCusto = custo + verticesVizinhos[vertice]
        if custos[vertice] > novoCusto:
          custos[vertice] = novoCusto
          paiVerticeAtual[vertice] = pontoDePartida
          verificados.append(pontoDePartida)
          pontoDePartida = verticeMenorCusto(custos)

    return print("Não é possível chegar nesse ponto")
  return print("Algum dos parâmetros está vazio")


graph = {}
graph["inicio"] = {}
graph["inicio"]["a"] = 6
graph["inicio"]["b"] = 2
graph["a"] = {}
graph["a"]["fim"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fim"] = 5
graph["fim"] = {}

infinito = float("inf")
custos = {}
custos["inicio"] = infinito
custos["a"] = infinito
custos["b"] = infinito
custos["fim"] = infinito
