esecuzione=True
alfabeto_lista=open('alfabeto.txt', "r") #carica la lista per le lettere dell'alfabeto e dei caratteri
alfabeto=list(alfabeto_lista)
alfabeto_lista.close()
codice_morse_lista=open('codice_morse.txt', "r")
codice_morse=list(codice_morse_lista) #carica la lista per la traduzione in codice morse
codice_morse_lista.close()

def per_morse(): #la funzione che traduce in morse
    print("inserisci la parola da tradurre in morse") #inserimento della parola da tradurre in morse
    parola=input()
    traduzione=""
    lung_parola=len(parola)
    for i in range (lung_parola): #ciclo che svolge la traduzione
        if parola[i] == " ": #se è uno spazio
            traduzione+="/ "
        else:
            for ind in range (49): #se non è uno spazio
                if parola[i].upper()+'\n' == alfabeto[ind]:
                    traduzione+=codice_morse[ind]
                    break
    print("le traduzione è: ", traduzione.replace('\n', ' '))
    print("hai finito?") #il programma chiede all'utente se ha finito di lavorare al programma
    fine=str(input())
    if fine.lower() != "si" and fine.lower() != "no":
        fine = ""
    while fine == "": #continua a chiedere all'utente cosa vuole
        print("risposta non valida. si o no?")
        fine=str(input().lower())
        if fine.lower() != "si" and fine.lower() != "no":
            fine = ""
    if fine.lower() == "si":
        esecuzione=False
    else:
        esecuzione=True
    return(esecuzione) #riporta il risultato della variabile booleana "esecuzione" 


def da_morse(): #la funzione che traduce dal morse
    print("inserisci la parola da tradurre dal morse") #chiede la parola/frase in morse da tradurre
    parola=input()
    traduzione=""
    lettera=""
    lung_parola=len(parola)
    for i in range (lung_parola): #ciclo di traduzione
        if parola[i] != " " and parola[i] != "/": #crea la "parola" codice in morse che tradurra
            lettera+=parola[i]
        elif parola[i] == " ":
            for ind in range(49): #ciclo che cerca la "parola" in morse che deve tradurre
                if lettera+"\n" == codice_morse[ind]:
                    traduzione+=alfabeto[ind]
                    break
                if len(lettera) == 0:
                    break
            lettera=""
        elif parola[i] == "/": #calcola se è uno spazio
            traduzione+=" "
        traduzione+=""
        if i == lung_parola-1: #definisce la traduzione
            for ind in range(49):
                if lettera+"\n" == codice_morse[ind]:
                    traduzione+=alfabeto[ind]
                    break
    print("le traduzione è: ", traduzione.replace('\n', '').lower()) #scrive la traduzione
    print("hai finito?") #chiede all'utente se ha finito
    fine=str(input())
    if fine.lower() != "si" and fine.lower() != "no":
        fine = ""
    while fine == "": #ciclo per verificare che sia una risposta valida
        print("risposta non valida. si o no?")
        fine=str(input().lower())
        if fine.lower() != "si" and fine.lower() != "no":
            fine = ""
    if fine.lower() == "si":
        esecuzione=False
    else:
        esecuzione=True
    return(esecuzione) #la funzione restituisce esecuzione

while esecuzione==True: #il ciclo che sta al cuore del programma, quello che fa ripetere il tutto il loop
    print("scrivi a se vuoi tradurre dal morse, e b se vuoi tradurre in morse") #richiesta di cosa si viole fare
    tipo=str(input())
    if tipo.lower() != "a" and tipo.lower() != "b":
        tipo=""
    while tipo == "": #verifica se è un'operazione valida'
        print("non hai scelto una soluzione valida!")
        tipo=str(input())
        if tipo.lower() != "a" and tipo.lower() != "b":
            tipo=""
    if tipo.lower() == "a": #in base alla scelta, va a scegliere se tradurre dal morse o in morse
        esecuzione=da_morse() #avvia la funzione dal morse, e prende la variabile esecuzione restituita dalla funzione precedente
    else:
        esecuzione=per_morse() #avvia la funzione per il morse, e come l'altra, riceve la variabile esecuzione