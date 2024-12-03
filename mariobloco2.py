def bloco():
    while True:
        pergunta = input('Qual o tamanho do bloco que quer criar? (digite no formato "LarguraxAltura") ')
        try:
            p1, p2 = map(int, pergunta.split('x'))
            if p1 > 0 and p2 > 0:
                return p1, p2
            else:
                print('Dgite um valor válido.')
        except ValueError:
            print('Formato inválido. Digite no formato "LarguraxAltura".')
def main():
    p1, p2 = bloco()
    for _ in range(p2):
        print("#" * p1)

main()