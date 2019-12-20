arquivo_parcial = open("bank.csv", "r")
arquivo_completo = open("bank-full.csv", "r")

#Quest�o 2
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

print("N�mero total de contatos: " + str(total_contatos) + " N�mero total de ades�o: " + str(total_adesao))
print("Porcentagem: " + str(float(total_adesao)/45211))
print("M�dia de contatos por cliente: " + str(float(total_contatos)/45211))
print("N�mero de contatos por ades�o: " + str(float(total_contatos)/total_adesao))
print("M�dia de contatos por cliente que aderiu ao produto: " + str(float(total_contatos_aderidos)/total_adesao))
print("M�dia de contatos por cliente que n�o aderiu ao produto: " + str(float(total_contatos_nao_aderidos)/(45211 - total_adesao)))
