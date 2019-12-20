arquivo_parcial = open("bank.csv", "r")
arquivo_completo = open("bank-full.csv", "r")

#Questão 1
linhas = arquivo_completo.readlines()
fl = False
tipos = [{"emprego": "admin.", "housing": 0, "personal": 0, "pessoas": 0, "pessoas com e": 0, "tendencia": 0},
             {"emprego": "unknown", "housing": 0, "personal": 0, "pessoas": 0, "pessoas com e": 0, "tendencia": 0},
             {"emprego": "unemployed", "housing": 0, "personal": 0, "pessoas": 0, "pessoas com e": 0, "tendencia": 0},
             {"emprego": "management", "housing": 0, "personal": 0, "pessoas": 0, "pessoas com e": 0, "tendencia": 0},
             {"emprego": "housemaid", "housing": 0, "personal": 0, "pessoas": 0, "pessoas com e": 0, "tendencia": 0},
             {"emprego": "entrepreneur", "housing": 0, "personal": 0, "pessoas": 0, "pessoas com e": 0, "tendencia": 0},
             {"emprego": "student", "housing": 0, "personal": 0, "pessoas": 0, "pessoas com e": 0, "tendencia": 0},
             {"emprego": "blue-collar", "housing": 0, "personal": 0, "pessoas": 0, "pessoas com e": 0, "tendencia": 0},
             {"emprego": "self-employed", "housing": 0, "personal": 0, "pessoas": 0, "pessoas com e": 0, "tendencia": 0},
             {"emprego": "retired", "housing": 0, "personal": 0, "pessoas": 0, "pessoas com e": 0, "tendencia": 0},
             {"emprego": "technician", "housing": 0, "personal": 0, "pessoas": 0, "pessoas com e": 0, "tendencia": 0},
             {"emprego": "services", "housing": 0, "personal": 0, "pessoas": 0, "pessoas com e": 0, "tendencia": 0}]

for i in linhas:
    linha = i.split(';')
    if fl == True:
        if linha[1] == "\"admin.\"":
            tipos[0]["pessoas"] += 1
            if linha[6] == "\"yes\"":
                tipos[0]["housing"] += 1
            if linha[7] == "\"yes\"":
                tipos[0]["personal"] += 1
            if linha[6] == "\"yes\"" or linha[7] == "\"yes\"":
                tipos[0]["pessoas com e"] += 1
            tipos[0]["tendencia"] = float(tipos[0]["pessoas com e"])/tipos[0]["pessoas"]
        if linha[1] == "\"unknown\"":
            tipos[1]["pessoas"] += 1
            if linha[6] == "\"yes\"":
                tipos[1]["housing"] += 1
            if linha[7] == "\"yes\"":
                tipos[1]["personal"] += 1
            if linha[6] == "\"yes\"" or linha[7] == "\"yes\"":
                tipos[1]["pessoas com e"] += 1
            tipos[1]["tendencia"] = float(tipos[1]["pessoas com e"])/tipos[1]["pessoas"]
        if linha[1] == "\"unemployed\"":
            tipos[2]["pessoas"] += 1
            if linha[6] == "\"yes\"":
                tipos[2]["housing"] += 1
            if linha[7] == "\"yes\"":
                tipos[2]["personal"] += 1
            if linha[6] == "\"yes\"" or linha[7] == "\"yes\"":
                tipos[2]["pessoas com e"] += 1
            tipos[2]["tendencia"] = float(tipos[2]["pessoas com e"])/tipos[2]["pessoas"]
        if linha[1] == "\"management\"":
            tipos[3]["pessoas"] += 1
            if linha[6] == "\"yes\"":
                tipos[3]["housing"] += 1
            if linha[7] == "\"yes\"":
                tipos[3]["personal"] += 1
            if linha[6] == "\"yes\"" or linha[7] == "\"yes\"":
                tipos[3]["pessoas com e"] += 1
            tipos[3]["tendencia"] = float(tipos[3]["pessoas com e"])/tipos[3]["pessoas"]
        if linha[1] == "\"housemaid\"":
            tipos[4]["pessoas"] += 1
            if linha[6] == "\"yes\"":
                tipos[4]["housing"] += 1
            if linha[7] == "\"yes\"":
                tipos[4]["personal"] += 1
            if linha[6] == "\"yes\"" or linha[7] == "\"yes\"":
                tipos[4]["pessoas com e"] += 1
            tipos[4]["tendencia"] = float(tipos[4]["pessoas com e"])/tipos[4]["pessoas"]
        if linha[1] == "\"entrepreneur\"":
            tipos[5]["pessoas"] += 1
            if linha[6] == "\"yes\"":
                tipos[5]["housing"] += 1
            if linha[7] == "\"yes\"":
                tipos[5]["personal"] += 1
            if linha[6] == "\"yes\"" or linha[7] == "\"yes\"":
                tipos[5]["pessoas com e"] += 1
            tipos[5]["tendencia"] = float(tipos[5]["pessoas com e"])/tipos[5]["pessoas"]
        if linha[1] == "\"student\"":
            tipos[6]["pessoas"] += 1
            if linha[6] == "\"yes\"":
                tipos[6]["housing"] += 1
            if linha[7] == "\"yes\"":
                tipos[6]["personal"] += 1
            if linha[6] == "\"yes\"" or linha[7] == "\"yes\"":
                tipos[6]["pessoas com e"] += 1
            tipos[6]["tendencia"] = float(tipos[6]["pessoas com e"])/tipos[6]["pessoas"]
        if linha[1] == "\"blue-collar\"":
            tipos[7]["pessoas"] += 1
            if linha[6] == "\"yes\"":
                tipos[7]["housing"] += 1
            if linha[7] == "\"yes\"":
                tipos[7]["personal"] += 1
            if linha[6] == "\"yes\"" or linha[7] == "\"yes\"":
                tipos[7]["pessoas com e"] += 1
            tipos[7]["tendencia"] = float(tipos[7]["pessoas com e"])/tipos[7]["pessoas"]
        if linha[1] == "\"self-employed\"":
            tipos[8]["pessoas"] += 1
            if linha[6] == "\"yes\"":
                tipos[8]["housing"] += 1
            if linha[7] == "\"yes\"":
                tipos[8]["personal"] += 1
            if linha[6] == "\"yes\"" or linha[7] == "\"yes\"":
                tipos[8]["pessoas com e"] += 1
            tipos[8]["tendencia"] = float(tipos[8]["pessoas com e"])/tipos[8]["pessoas"]
        if linha[1] == "\"retired\"":
            tipos[9]["pessoas"] += 1
            if linha[6] == "\"yes\"":
                tipos[9]["housing"] += 1
            if linha[7] == "\"yes\"":
                tipos[9]["personal"] += 1
            if linha[6] == "\"yes\"" or linha[7] == "\"yes\"":
                tipos[9]["pessoas com e"] += 1
            tipos[9]["tendencia"] = float(tipos[9]["pessoas com e"])/tipos[9]["pessoas"]
        if linha[1] == "\"technician\"":
            tipos[10]["pessoas"] += 1
            if linha[6] == "\"yes\"":
                tipos[10]["housing"] += 1
            if linha[7] == "\"yes\"":
                tipos[10]["personal"] += 1
            if linha[6] == "\"yes\"" or linha[7] == "\"yes\"":
                tipos[10]["pessoas com e"] += 1
            tipos[10]["tendencia"] = float(tipos[10]["pessoas com e"])/tipos[10]["pessoas"]
        if linha[1] == "\"services\"":
            tipos[11]["pessoas"] += 1
            if linha[6] == "\"yes\"":
                tipos[11]["housing"] += 1
            if linha[7] == "\"yes\"":
                tipos[11]["personal"] += 1
            if linha[6] == "\"yes\"" or linha[7] == "\"yes\"":
                tipos[11]["pessoas com e"] += 1
            tipos[11]["tendencia"] = float(tipos[11]["pessoas com e"])/tipos[11]["pessoas"]
    else:
        fl = True

max_tendencia = max(tipos[0]["tendencia"], tipos[1]["tendencia"], tipos[2]["tendencia"],
          tipos[3]["tendencia"], tipos[4]["tendencia"], tipos[5]["tendencia"],
          tipos[6]["tendencia"], tipos[7]["tendencia"], tipos[8]["tendencia"],
          tipos[9]["tendencia"], tipos[10]["tendencia"], tipos[11]["tendencia"])

for i in tipos:
    if i["tendencia"] == max_tendencia:
        print("Emprego: " + i["emprego"])

max_emprestimo = max(i["housing"], i["personal"])

for i in tipos:
    if i["housing"] == max_emprestimo:
        print("Tipo de empréstimo: Housing")
    if i["personal"] == max_emprestimo:
        print("Tipo de empréstimo: Personal")
