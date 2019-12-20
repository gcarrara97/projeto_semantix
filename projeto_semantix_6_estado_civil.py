arquivo_parcial = open("bank.csv", "r")
arquivo_completo = open("bank-full.csv", "r")

#Questão 6
#ESTADO CIVIL
linhas = arquivo_completo.readlines()
fl = False
emprestimo_imobiliario = 0
estado = {"married": 0, "divorced": 0, "single": 0}

for i in linhas:
    linha = i.split(';')
    if fl == True:
        if linha[6] == "\"yes\"":
            emprestimo_imobiliario += 1
            if linha[2] == "\"married\"":
                estado["married"] += 1
            if linha[2] == "\"divorced\"":
                estado["divorced"] += 1
            if linha[2] == "\"single\"":
                estado["single"] += 1
    else:
        fl = True

print("Número de clientes com empréstimo imobiliário: " + str(emprestimo_imobiliario))
print("Married: freq. absoluta de " + str(estado["married"]) + " e freq. relativa de " + str(float(estado["married"])/emprestimo_imobiliario))
print("Divorced: freq. absoluta de " + str(estado["divorced"]) + " e freq. relativa de " + str(float(estado["divorced"])/emprestimo_imobiliario))
print("Single: freq. absoluta de " + str(estado["single"]) + " e freq. relativa de " + str(float(estado["single"])/emprestimo_imobiliario))
