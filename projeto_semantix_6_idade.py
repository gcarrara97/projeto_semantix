arquivo_parcial = open("bank.csv", "r")
arquivo_completo = open("bank-full.csv", "r")

#Questão 6
#IDADE
linhas = arquivo_completo.readlines()
fl = False
emprestimo_imobiliario = 0
idades = []

for i in linhas:
    linha = i.split(';')
    if fl == True:
        if linha[6] == "\"yes\"":
            emprestimo_imobiliario += 1
            idades.append(int(linha[0]))
    else:
        fl = True

print("Número de clientes com empréstimo imobiliário: " + str(emprestimo_imobiliario))
print("MENOR IDADE: " + str(min(idades)))
print("MAIOR IDADE: " + str(max(idades)))

i20_30 = 0
i30_40 = 0
i40_50 = 0
i50_60 = 0
i60_70 = 0
i70_80 = 0
fl = False

for i in linhas:
    linha = i.split(';')
    if fl == True:
        if linha[6] == "\"yes\"":
            if int(linha[0]) >= 20 and int(linha[0]) < 30:
                i20_30 += 1
            if int(linha[0]) >= 30 and int(linha[0]) < 40:
                i30_40 += 1
            if int(linha[0]) >= 40 and int(linha[0]) < 50:
                i40_50 += 1
            if int(linha[0]) >= 50 and int(linha[0]) < 60:
                i50_60 += 1
            if int(linha[0]) >= 60 and int(linha[0]) < 70:
                i60_70 += 1
            if int(linha[0]) >= 70 and int(linha[0]) < 80:
                i70_80 += 1
    else:
        fl = True

print("20 a 30 anos: freq. absoluta de " + str(i20_30) + " e freq. relativa de " + str(float(i20_30)/emprestimo_imobiliario))
print("30 a 40 anos: freq. absoluta de " + str(i30_40) + " e freq. relativa de " + str(float(i30_40)/emprestimo_imobiliario))
print("40 a 50 anos: freq. absoluta de " + str(i40_50) + " e freq. relativa de " + str(float(i40_50)/emprestimo_imobiliario))
print("50 a 60 anos: freq. absoluta de " + str(i50_60) + " e freq. relativa de " + str(float(i50_60)/emprestimo_imobiliario))
print("60 a 70 anos: freq. absoluta de " + str(i60_70) + " e freq. relativa de " + str(float(i60_70)/emprestimo_imobiliario))
print("70 a 80 anos: freq. absoluta de " + str(i70_80) + " e freq. relativa de " + str(float(i70_80)/emprestimo_imobiliario))
