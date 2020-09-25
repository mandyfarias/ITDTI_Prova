
count = 1
#print("O programa irá perguntar x10 a palavra/elemento que deseja salvar")
qntPerg = int(input("Quantos elementos deseja salvar?"))
while count <= qntPerg:
    arquivo = open("elementos.txt", "a")
    elementos = input("Informe o que deseja salvar")
    arquivo.writelines(elementos+"\n")
    arquivo.close()
    count += 1

print("Salvo com sucesso! (ou não, tem que ver ;-; )")