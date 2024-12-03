def main():
    p1 = linha()
    p2 = coluna()
    for _ in range(p2):
        print('#' * p1)

def linha():
    while True:
        p1 = int(input('Qual o tamanho da linha que quer criar? '))
        if p1 > 0:
            return p1
        
def coluna():
    while True:
        p2 = int(input('Qual o tamanho da coluna que quer criar? '))
        if p2 > 0:
            return p2
        
main()