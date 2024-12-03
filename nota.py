processadores = [
  {"nome" : "3400G", "nucleos" : "4 núcleos e 8 threads", "velocidade" : "3.7 GHz", "GPU" : "Radeon RX Vega 11", "preco" : "R$ 400,00"},
  {"nome" : "3600", "nucleos" : "6 núcleos e 12 threads", "velocidade" : "3.6 GHz", "GPU" : "não contém", "preco" : "R$ 450,00"},
  {"nome" : "4500", "nucleos" : "6 núcleos e 6 threads", "velocidade" : "3.6 GHz", "GPU" : "não contém", "preco" : "R$ 590,00"},
  {"nome" : "4600G", "nucleos" : "6 núcleos e 12 threads", "velocidade" : "3.7 GHz", "GPU" : "Radeon Vega 7", "preco" : "R$ 650,00"},
  {"nome" : "5500", "nucleos" : "6 núcleos e 12 threads", "velocidade" : "3.6 GHz", "GPU" : "não contém", "preco" : "R$ 597,00"},
  {"nome" : "5600G", "nucleos" : "6 núcleos e 12 threads", "velocidade" : "3.9 GHz", "GPU" : "Radeon Vega 7", "preco" : "R$ 930,00"},
  {"nome" : "5600X", "nucleos" : "6 núcleos e 12 threads", "velocidade" : "3.7 GHz", "GPU" : "não contém", "preco" : "R$ 950,00"},
  {"nome" : "7600", "nucleos" : "6 núcleos e 12 threads ", "velocidade" : "3.8 GHz", "GPU" : "não contém", "preco" : "R$ 1.370,00"},
  {"nome" : "7600X", "nucleos" : "6 núcleos e 12 threads", "velocidade" : "4.7 GHz", "GPU" : "não contém", "preco" : "R$ 1.630,00"}
]

def exibir_processador(processador):
  processador = processador.strip().lower()
  for i in processadores:
    if i["nome"] == processador:
      print("Nome:", i["nome"])
      print("Nucleos:", i["nucleos"])
      print("velocidade", i["velocidade"])
      print("GPU:", i["GPU"])
      print("preço:", i["preco"])

def perguntar_novamente():
  while True:
    pergunta = input("Deseja ver outro processador? ").strip().lower()

    if pergunta in ["sim", "s", "ss", "yes"]:
        p2 = input("Qual processador você deseja? ").strip()
        exibir_processador(p2)

    elif pergunta in ["não", "nao", "n", "no"]:
        print("Ok.")
        break
    else:
       print("Por favor, responda com sim ou não.")

def main():
    p2 = input("Qual processador Ryzen da geração 5 você deseja? Ryzen 5 ...").strip()
    exibir_processador(p2)
    perguntar_novamente()


main()