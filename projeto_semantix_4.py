arquivo_parcial = open("bank.csv", "r")
arquivo_completo = open("bank-full.csv", "r")

#Questão 4
linhas = arquivo_completo.readlines()
fl = False
total_adesao_anterior = 0
total_contato_anterior = 0
total_adesao = 0
total_contato = 0

for i in linhas:
    linha = i.split(';')
    if fl == True:
        total_contato_anterior += int(linha[14])
        total_contato += int(linha[12])
        if linha[15] == "\"success\"":
            total_adesao_anterior += 1
        if linha[16] == "\"yes\"\n":
            total_adesao += 1
    else:
        fl = True

print("Total de adesão na campanha anterior: " + str(total_adesao_anterior))
print("Número de contatos feitos antes da campanha atual: " + str(total_contato_anterior))
print("Total de adesão na campanha atual: " + str(total_adesao))
print("Número de contatos feitos durante a campanha atual: " + str(total_contato))
print("Aumento de adesão: " + str(float(total_adesao)/total_adesao_anterior))
print("Aumento de contatos: " + str(float(total_contato)/total_contato_anterior))
