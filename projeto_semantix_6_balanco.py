arquivo_parcial = open("bank.csv", "r")
arquivo_completo = open("bank-full.csv", "r")

#Questão 6
#BALANÇO
linhas = arquivo_completo.readlines()
fl = False
emprestimo_imobiliario = 0
balanco = []

for i in linhas:
    linha = i.split(';')
    if fl == True:
        if linha[6] == "\"yes\"":
            emprestimo_imobiliario += 1
            balanco.append(int(linha[5]))
    else:
        fl = True

print("Número de clientes com empréstimo imobiliário: " + str(emprestimo_imobiliario))
print("MENOR BALANÇO " + str(min(balanco)))
print("MAIOR BALANÇO " + str(max(balanco)))

b0 = 0
b0_10000 = 0
b10000_20000 = 0
b20000_30000 = 0
b30000_40000 = 0
b40000_50000 = 0
b50000_60000 = 0
fl = False

for i in linhas:
    linha = i.split(';')
    if fl == True:
        if linha[6] == "\"yes\"":
            if int(linha[5]) < 0:
                b0 += 1
            if int(linha[5]) >= 0 and int(linha[5]) < 10000:
                b0_10000 += 1
            if int(linha[5]) >= 10000 and int(linha[5]) < 20000:
                b10000_20000 += 1
            if int(linha[5]) >= 20000 and int(linha[5]) < 30000:
                b20000_30000 += 1
            if int(linha[5]) >= 30000 and int(linha[5]) < 40000:
                b30000_40000 += 1
            if int(linha[5]) >= 40000 and int(linha[5]) < 50000:
                b40000_50000 += 1
            if int(linha[5]) >= 50000 and int(linha[5]) < 60000:
                b50000_60000 += 1
    else:
        fl = True

print("Menor que 0 euros: freq. absoluta de " + str(b0) + " e freq. relativa de " + str(float(b0)/emprestimo_imobiliario))
print("Entre 0 e 10000 euros: freq. absoluta de " + str(b0_10000) + " e freq. relativa de " + str(float(b0_10000)/emprestimo_imobiliario))
print("Entre 10000 e 20000 euros: freq. absoluta de " + str(b10000_20000) + " e freq. relativa de " + str(float(b10000_20000)/emprestimo_imobiliario))
print("Entre 20000 e 30000 euros: freq. absoluta de " + str(b20000_30000) + " e freq. relativa de " + str(float(b20000_30000)/emprestimo_imobiliario))
print("Entre 30000 e 40000 euros: freq. absoluta de " + str(b30000_40000) + " e freq. relativa de " + str(float(b30000_40000)/emprestimo_imobiliario))
print("Entre 40000 e 50000 euros: freq. absoluta de " + str(b40000_50000) + " e freq. relativa de " + str(float(b40000_50000)/emprestimo_imobiliario))
print("Entre 50000 e 60000 euros: freq. absoluta de " + str(b50000_60000) + " e freq. relativa de " + str(float(b50000_60000)/emprestimo_imobiliario))
