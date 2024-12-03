def main():
    p1 = pergunta()
    for _ in range(1):
        print('#' * p1)

def pergunta():
    while True:
        p1 = int(input('Qual o tamanho da linha que quer criar? '))
        if p1 > 0:
            return p1
main()