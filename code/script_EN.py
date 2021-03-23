esecuzione=True #the variable that defines if the loop should keep going or not
alfabeto_lista=open('alfabeto.txt', "r") #read the alphabet characters
alfabeto=list(alfabeto_lista) #applies them to a list
alfabeto_lista.close() #close the file
codice_morse_lista=open('codice_morse.txt', "r") #read the morse characters
codice_morse=list(codice_morse_lista) #applies them to a specific list
codice_morse_lista.close() #close the file again

def per_morse(): #the function that translates to morse
    print("insert the phrase to translate to morse")
    parola=input() #input from the user
    traduzione="" #translation
    lung_parola=len(parola) #lenght of the input
    for i in range (lung_parola): #the cicle that translate the word
        if parola[i] == " ":
            traduzione+="/ "
        else: #if the charater is different than a space, it chack in the list the morse conterpart
            for ind in range (49):
                if parola[i].upper()+'\n' == alfabeto[ind]:
                    traduzione+=codice_morse[ind] #add to the translation variable the translated charater
                    break #end the cycle
    print("the translation is: ", traduzione.replace('\n', ' ')) #print the translation 
    print("have you done?") #ask user if he has done the translation
    fine=str(input()) #get user answer
    if fine.lower() != "yes" and fine.lower() != "no": #first check if is valid
        fine = ""
    while fine == "": #if isn't valid enter this cicle until isn't valid
        print("not a valid answer. yes o no?")
        fine=str(input().lower())
        if fine.lower() != "yes" and fine.lower() != "no":
            fine = ""
    if fine.lower() == "yes": #if user want to exit
        esecuzione=False #the exit variable say to end
    else:
        esecuzione=True #overwise it defines it to keep going
    return(esecuzione) #return to our "main" the variable esecuzione

def da_morse(): #that is the function that translate from morse
    print("insert the phrase to translate from morse")
    parola=input()
    traduzione=""
    lettera=""
    lung_parola=len(parola)
    for i in range (lung_parola): #translation cicle
        if parola[i] != " " and parola[i] != "/": #if th charater is different that a space or a / it adds it to a temp word
            lettera+=parola[i]
        elif parola[i] == " ": #if the charater is a space, it enter in a loop until doesn't find it in the morse file
            for ind in range(49):
                if lettera+"\n" == codice_morse[ind]: #search for the word
                    traduzione+=alfabeto[ind]
                    break
                if len(lettera) == 0: #also if the lenght of the temp word is 0, it stop the cycle
                    break
            lettera=""
        elif parola[i] == "/": #get the space
            traduzione+=" "
        traduzione+=""
        if i == lung_parola-1: #if is the last charater of the phrase translate it too
            for ind in range(49):
                if lettera+"\n" == codice_morse[ind]:
                    traduzione+=alfabeto[ind]
                    break
    print("the translation is: ", traduzione.replace('\n', '').lower()) #print it
    print("have you done?") 
    fine=str(input())
    if fine.lower() != "yes" and fine.lower() != "no": #same as before
        fine = ""
    while fine == "":
        print("not a valid answer. yes or> no?")
        fine=str(input().lower())
        if fine.lower() != "yes" and fine.lower() != "no":
            fine = ""
    if fine.lower() == "yes":
        esecuzione=False
    else:
        esecuzione=True
    return(esecuzione)

while esecuzione==True: #the "heart" of the programm, it is a loop which keep going until user tell it to stop
    print("write a if you want to translate from morse or b if you want to translate to morse")
    tipo=str(input())
    if tipo.lower() != "a" and tipo.lower() != "b": #chechs if user's input is right, and accepted, if not, define the "tipo" variable as "" and enter a loop, until the user insert a valid option
        tipo=""
    while tipo == "":
        print("not a valid option!")
        tipo=str(input())
        if tipo.lower() != "a" and tipo.lower() != "b":
            tipo=""
    if tipo.lower() == "a": #this if define is wants the user to translate from or to morse code
        esecuzione=da_morse() #goes to the function that translates FROM morse
    else:
        esecuzione=per_morse() #and here goe to the function that translates TO morse