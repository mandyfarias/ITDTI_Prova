
continuar = "s"
while(continuar == "s"):
    primeiro = float(input("Primeiro número:"))
    operacao = int(input("Qual a operação? (soma = 1, subtração = 2, multiplicação = 3, divisão = 4, resto divisão = 5)"))
    segundo = float(input("Segundo número:"))

    # operacao = operacao.upper() (ia fazer com string mas desisti ;-;)
    if  operacao == 1:
        result = primeiro + segundo
    elif operacao == 2:
        result = primeiro - segundo
    elif operacao == 3:
        result = primeiro * segundo
    elif operacao == 4:
        result = primeiro / segundo
    elif operacao == 5:
        result = primeiro % segundo
    else:
        print(f"{operacao} não é um número válido para operação")


    print(result)
    continuar = str(input("Deseja continuar?: (s/n)"))