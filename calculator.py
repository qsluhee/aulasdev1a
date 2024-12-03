def calcularascoisa():
    linha = input("Digite uma expressão com dois digitos: ").strip().split()

    i1 = None
    i2 = None
    linh = None

    for i in linha:
        match i:
            case "+" | "-" | "*" | "/" | ":" | "x":
                linh = i
            case _:
                if i1 == None:
                    i1 = float(i)
                else:
                    i2 = float(i)

    match linh:
        case "+":
            print(i1 + i2)
        case "-":
            print(i1 - i2)
        case "*" | "x":
            print(i1 * i2)
        case "/" | ":":
            print(i1 / i2)

while True:
    calcularascoisa()