arquivo_parcial = open("bank.csv", "r")
arquivo_completo = open("bank-full.csv", "r")

#Questão 6
#PROFISSÃO
linhas = arquivo_completo.readlines()
fl = False
emprestimo_imobiliario = 0
profissao = {"admin.": 0, "unknown": 0, "unemployed": 0, "management": 0,
             "housemaid": 0, "entrepreneur": 0, "student": 0, "blue-collar": 0,
             "self-employed": 0, "retired": 0, "technician": 0, "services": 0}

for i in linhas:
    linha = i.split(';')
    if fl == True:
        if linha[6] == "\"yes\"":
            emprestimo_imobiliario += 1
            if linha[1] == "\"admin.\"":
                profissao["admin."] += 1
            if linha[1] == "\"unknown\"":
                profissao["unknown"] += 1
            if linha[1] == "\"unemployed\"":
                profissao["unemployed"] += 1
            if linha[1] == "\"management\"":
                profissao["management"] += 1
            if linha[1] == "\"housemaid\"":
                profissao["housemaid"] += 1
            if linha[1] == "\"entrepreneur\"":
                profissao["entrepreneur"] += 1
            if linha[1] == "\"student\"":
                profissao["student"] += 1
            if linha[1] == "\"blue-collar\"":
                profissao["blue-collar"] += 1
            if linha[1] == "\"self-employed\"":
                profissao["self-employed"] += 1
            if linha[1] == "\"retired\"":
                profissao["retired"] += 1
            if linha[1] == "\"technician\"":
                profissao["technician"] += 1
            if linha[1] == "\"services\"":
                profissao["services"] += 1
    else:
        fl = True

print("Número de clientes com empréstimo imobiliário: " + str(emprestimo_imobiliario))
print("Admin.: freq. absoluta de " + str(profissao["admin."]) + " e freq. relativa de " + str(float(profissao["admin."])/emprestimo_imobiliario))
print("Unknown: freq. absoluta de " + str(profissao["unknown"]) + " e freq. relativa de " + str(float(profissao["unknown"])/emprestimo_imobiliario))
print("Unemployed: freq. absoluta de " + str(profissao["unemployed"]) + " e freq. relativa de " + str(float(profissao["unemployed"])/emprestimo_imobiliario))
print("Management: freq. absoluta de " + str(profissao["management"]) + " e freq. relativa de " + str(float(profissao["management"])/emprestimo_imobiliario))
print("Housemaid: freq. absoluta de " + str(profissao["housemaid"]) + " e freq. relativa de " + str(float(profissao["housemaid"])/emprestimo_imobiliario))
print("Entrepreneur: freq. absoluta de " + str(profissao["entrepreneur"]) + " e freq. relativa de " + str(float(profissao["entrepreneur"])/emprestimo_imobiliario))
print("Student: freq. absoluta de " + str(profissao["student"]) + " e freq. relativa de " + str(float(profissao["student"])/emprestimo_imobiliario))
print("Blue-collar: freq. absoluta de " + str(profissao["blue-collar"]) + " e freq. relativa de " + str(float(profissao["blue-collar"])/emprestimo_imobiliario))
print("Self-employed: freq. absoluta de " + str(profissao["self-employed"]) + " e freq. relativa de " + str(float(profissao["self-employed"])/emprestimo_imobiliario))
print("Retired: freq. absoluta de " + str(profissao["retired"]) + " e freq. relativa de " + str(float(profissao["retired"])/emprestimo_imobiliario))
print("Technician: freq. absoluta de " + str(profissao["technician"]) + " e freq. relativa de " + str(float(profissao["technician"])/emprestimo_imobiliario))
print("Services: freq. absoluta de " + str(profissao["services"]) + " e freq. relativa de " + str(float(profissao["services"])/emprestimo_imobiliario))
