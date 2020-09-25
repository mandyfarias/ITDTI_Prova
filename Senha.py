password = input("Informe a senha:")

if (password.isalnum()) and (password.isdigit()):
    print("Sua senha é válida")
else:
    print("Sua não senha é válida")