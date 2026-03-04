classe= str(input("Digite a classe do animal:"
"(aves, mamíferos, répteis, anfíbios e peixes)"))

if classe=="Aves" or "aves":
    animal=(input("Digite o animal da classe escolhida:"))

    if animal == "arara" or "Arara":
        print("Os alimentos ideais para uma Arara, são: " \
        "frutas frescas, vegetais, sementes e nozes."
        "A quantidade de alimento diário ideal varia conforme o tamanho, idade e nível de atividade da ave. ")
        
    if animal == "avestruz" or "Avestruz":
        print("Os alimentos ideais para um Avestruz, são: " \
        "ração balanceada e pasto verda. " \
        "A quantidade diária ideal de ração é de 1 a 2 quilos" \
        " por ave, e o pasto é de 2 a 5 quilos.")

    if animal=="maritaca" or "Maritaca":
        print("Os alimentos ideais para uma Maritaca, são: ração, frutas frescas e maduras, " \
        "sementes e outros grãos. " \
        "A quantidade de alimento diário ideal varia conforme o tamanho, idade e nível de atividade da ave.")

elif classe=="mamíferos" or "Mamífero":
    if animal == "Leão" or "leão":
        print("Os alimentos ideais para um Leão é: Carne, especialmente de grandes " \
        "ungulados como zebras, gnus, búfalos e antílopes. A quantidade de alimento diário ideal é em média de 5 a 6 quilos por mamífero.")

    if animal == "pantera" or "Pantera":
        print("Os alimentos ideais para uma Pantera são presas de animais de sangue quente, como:" \
        "Lebres, camundongos, antílopes e outros animais de tamanho médio. A quantidade de alimento diário ideal é" \
        " em média 1,4 a 2 quilos de carne.")

    if animal == "girafa" or "Girafa":
        print("Os alimentos ideais para uma Girafa são as folhas de acácias. A quantidade de alimento diário ideal é de 30 a 60 quilos.")

    if animal == "elefante" or "Elefante":
        print("Os alimentos ideais para um Elefante são folhas, frutas e cascas de árvores. " \
        "A quantidade de alimento diário ideal é de 150 a 300 quilos.")

    if animal == "sagui" or "Sagui":
        print("Os alimentos ideais para um Sagui são frutas, legumes, insetos, proteínas e ração. " \
        "A quantidade de alimento diário ideal varia conforme o tamanho, idade e nível de atividade do animal.")

    if animal == "gorila" or "Gorila":
        print("Os alimentos ideais para um Gorila são folhas, caules, brotos de bambu e frutas. " \
        "A quantidade de alimento diário ideal é de 18 quilos.")

    if animal=="onça" or "Onça":
        print("Os alimentos ideais para uma Onça são mamíferos de médio e grande porte. " \
        "A quantidade de alimento diário ideal varia de 5 a 8 quilos.")

    if animal == "Hipopótamo" or "hipopótamo":
        print("Os alimentos ideais para um Hipopótamo são plantas, principalmente capim. " \
        "A quantidade de alimento diário ideal 40 quilos.")

    if animal  == "anta" or "Anta":
        print("Os alimentos ideais para uma Anta são folhas, ramos, brotos, caules, plantas aquáticas e frutos." \
        "A quantidade de alimento diário ideal é de 6 a 9 quilos.")

    if animal == "zebra" or "Zebra":
        print("Os alimentos ideais para uma Zebra são gramineas, " \
        "complementado por folhas, brotos, cascas e alguns frutos. " \
        "A quantidade de alimento diário ideal varia conforme o tamanho, idade e nível de atividade do animal")

elif classe=="répteis" or "Répteis":
    if animal == "cobra" or "Cobra":
        print("Os alimentos ideais para uma Cobra são roedores congelados, como camundongos e ratos." \
        "A quantidade de alimento diário ideal depende da espécie, tamanho, idade e frequência com que elas se alimentam.")

    if animal == "Jacaré" or "jacaré":
        print("Os alimentos ideais para um Jacaré são carne bovina, suína, frango e peixes." \
        " A quantidade de alimento diário ideal depende do seu tamanho, idade e nível de atividade.")

    if animal == "tartaruga" or "Tartaruga":
         print("Os alimentos ideais para uma Tartaruga são vegetais de folhas escuras, legumes e proteínas." \
        " A quantidade de alimento diário ideal depende do seu tamanho, espécie e idade.")
         
    if animal == "jabuti" or "Jabuti":
         print("Os alimentos ideais para um Jabuti são vegetais, frutas e proteínas." \
        " A quantidade de alimento diário ideal depende do seu tamanho e idade.")
         
elif classe == "Anfíbios" or "anfíbios":
    print("Não há Anfíbios.")

elif classe == "peixes" or "Peixes":
    print("Não há Peixes.")



else:
    print("Não há essa classe disponível.")