arquivo_parcial = open("bank.csv", "r")
arquivo_completo = open("bank-full.csv", "r")

#Questão 2
linhas = arquivo_completo.readlines()
fl = False
total_contatos = 0
total_adesao = 0
total_contatos_aderidos = 0
total_contatos_nao_aderidos = 0

for i in linhas:
    linha = i.split(';')
    if fl == True:
        total_contatos += int(linha[12])
        if linha[16] == "\"yes\"\n":
            total_adesao += 1
            total_contatos_aderidos += int(linha[12])
        else:
            total_contatos_nao_aderidos += int(linha[12])
    else:
        fl = True

print("Número total de contatos: " + str(total_contatos) + " Número total de adesão: " + str(total_adesao))
print("Porcentagem: " + str(float(total_adesao)/45211))
print("Média de contatos por cliente: " + str(float(total_contatos)/45211))
print("Número de contatos por adesão: " + str(float(total_contatos)/total_adesao))
print("Média de contatos por cliente que aderiu ao produto: " + str(float(total_contatos_aderidos)/total_adesao))
print("Média de contatos por cliente que não aderiu ao produto: " + str(float(total_contatos_nao_aderidos)/(45211 - total_adesao)))
