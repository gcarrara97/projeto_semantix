arquivo_parcial = open("bank.csv", "r")
arquivo_completo = open("bank-full.csv", "r")

#Questão 6
#EDUCAÇÃO
linhas = arquivo_completo.readlines()
fl = False
emprestimo_imobiliario = 0
educacao = {"unknown": 0, "secondary": 0, "primary": 0, "tertiary": 0}

for i in linhas:
    linha = i.split(';')
    if fl == True:
        if linha[6] == "\"yes\"":
            emprestimo_imobiliario += 1
            if linha[3] == "\"unknown\"":
                educacao["unknown"] += 1
            if linha[3] == "\"secondary\"":
                educacao["secondary"] += 1
            if linha[3] == "\"primary\"":
                educacao["primary"] += 1
            if linha[3] == "\"tertiary\"":
                educacao["tertiary"] += 1
    else:
        fl = True

print("Número de clientes com empréstimo imobiliário: " + str(emprestimo_imobiliario))
print("Unknown: freq. absoluta de " + str(educacao["unknown"]) + " e freq. relativa de " + str(float(educacao["unknown"])/emprestimo_imobiliario))
print("Secondary: freq. absoluta de " + str(educacao["secondary"]) + " e freq. relativa de " + str(float(educacao["secondary"])/emprestimo_imobiliario))
print("Primary: freq. absoluta de " + str(educacao["primary"]) + " e freq. relativa de " + str(float(educacao["primary"])/emprestimo_imobiliario))
print("Tertiary: freq. absoluta de " + str(educacao["tertiary"]) + " e freq. relativa de " + str(float(educacao["tertiary"])/emprestimo_imobiliario))
