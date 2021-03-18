esecuzione=True
alfabeto_lista=open('alfabeto.txt', "r")
alfabeto=list(alfabeto_lista)
alfabeto_lista.close()
codice_morse_lista=open('codice_morse.txt', "r")
codice_morse=list(codice_morse_lista)
codice_morse_lista.close()

def per_morse():
    print("insert the phrase to translate to morse")
    parola=input()
    traduzione=""
    lung_parola=len(parola)
    for i in range (lung_parola):
        if parola[i] == " ":
            traduzione+="/ "
        else:
            for ind in range (49):
                if parola[i].upper()+'\n' == alfabeto[ind]:
                    traduzione+=codice_morse[ind]
                    break
    print("the translation is: ", traduzione.replace('\n', ' '))
    print("have you done?")
    fine=str(input())
    if fine.lower() != "yes" and fine.lower() != "no":
        fine = ""
    while fine == "":
        print("not a valid answer. yes o no?")
        fine=str(input().lower())
        if fine.lower() != "yes" and fine.lower() != "no":
            fine = ""
    if fine.lower() == "yes":
        esecuzione=False
    else:
        esecuzione=True
    return(esecuzione)

def da_morse():
    print("insert the phrase to translate from morse")
    parola=input()
    traduzione=""
    lettera=""
    lung_parola=len(parola)
    for i in range (lung_parola):
        if parola[i] != " " and parola[i] != "/":
            lettera+=parola[i]
        elif parola[i] == " ":
            for ind in range(49):
                if lettera+"\n" == codice_morse[ind]:
                    traduzione+=alfabeto[ind]
                    break
                if len(lettera) == 0:
                    break
            lettera=""
        elif parola[i] == "/":
            traduzione+=" "
        traduzione+=""
        if i == lung_parola-1:
            for ind in range(49):
                if lettera+"\n" == codice_morse[ind]:
                    traduzione+=alfabeto[ind]
                    break
    print("the translation is: ", traduzione.replace('\n', '').lower())
    print("have you done?")
    fine=str(input())
    if fine.lower() != "yes" and fine.lower() != "no":
        fine = ""
    while fine == "":
        print("not a valid answer. yes o no?")
        fine=str(input().lower())
        if fine.lower() != "yes" and fine.lower() != "no":
            fine = ""
    if fine.lower() == "yes":
        esecuzione=False
    else:
        esecuzione=True
    return(esecuzione)

while esecuzione==True:
    #esecuzione=main()
    print("write a if you want to translate from morse or b if you want to translate to morse")
    tipo=str(input())
    if tipo.lower() != "a" and tipo.lower() != "b":
        tipo=""
    while tipo == "":
        print("not a valid option!")
        tipo=str(input())
        if tipo.lower() != "a" and tipo.lower() != "b":
            tipo=""
    if tipo.lower() == "a":
        esecuzione=da_morse()
    else:
        esecuzione=per_morse()