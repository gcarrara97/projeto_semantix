arquivo_parcial = open("bank.csv", "r")
arquivo_completo = open("bank-full.csv", "r")

#Quest�o 5
linhas = arquivo_completo.readlines()
fl = False
credito_default = 0

for i in linhas:
    linha = i.split(';')
    if fl == True:
        if linha[4] == "\"yes\"":
            credito_default += 1
    else:
        fl = True

print("N�mero de clientes em default: " + str(credito_default))
