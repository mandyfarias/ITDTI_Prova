
palavra = str(input("Qual a palavra/frase?:"))
result = ""
for i in range(len(palavra)):
    if i % 2:
        result += palavra[i]
print(f"{result}")