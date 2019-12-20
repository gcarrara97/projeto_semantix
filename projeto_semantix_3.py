arquivo_parcial = open("bank.csv", "r")
arquivo_completo = open("bank-full.csv", "r")

#Questão 3
linhas = arquivo_completo.readlines()
fl = False
total_adesao = 0
total_contatos_aderidos = 0

for i in linhas:
    linha = i.split(';')
    if fl == True:
        if linha[16] == "\"yes\"\n":
            total_adesao += 1
            total_contatos_aderidos += int(linha[12])
    else:
        fl = True

print("Total de ligações recomendadas: " + str(45211*(float(total_contatos_aderidos)/total_adesao)))
