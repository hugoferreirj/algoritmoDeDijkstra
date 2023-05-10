
def caminhoMaisCurto(pai, ondeSeChegou):
  noAtual = ondeSeChegou
  caminho = [noAtual]
  while pai[noAtual] is not None:
    caminho.append(pai[noAtual])
    noAtual = pai[noAtual]
  caminho.reverse()
  return print(caminho)

def verticeMenorCusto(custos, verificados):
  menorCusto = float("inf")
  vMenorCusto = None
  for vertice in custos.keys():
    if custos[vertice] < menorCusto and vertice not in verificados:
      menorCusto = custos[vertice]
      vMenorCusto = vertice
  return vMenorCusto

def algoritmoDeDijkstra(graph, pontoDePartida, ondeSeQuerChegar, custos):
  paiVerticeAtual = {}
  paiVerticeAtual[pontoDePartida] = None
  if pontoDePartida == ondeSeQuerChegar:
    return print([ondeSeQuerChegar])
  if graph and pontoDePartida and ondeSeQuerChegar:
    custos[pontoDePartida] = 0
    verificados = []
    while pontoDePartida is not None:
      custo = custos[pontoDePartida]
      verticesVizinhos = graph[pontoDePartida].keys()
      for vertice in verticesVizinhos:
        novoCusto = custo + graph[pontoDePartida][vertice]
        if novoCusto < custos[vertice]:
          custos[vertice] = novoCusto
          paiVerticeAtual[vertice] = pontoDePartida
      verificados.append(pontoDePartida)
      pontoDePartida = verticeMenorCusto(custos, verificados)
    if not paiVerticeAtual[ondeSeQuerChegar]:
      return print("Não é possível chegar nesse ponto")
    else:
      return caminhoMaisCurto(paiVerticeAtual, ondeSeQuerChegar)
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

algoritmoDeDijkstra(graph, "inicio", "fim", custos)