while True:
    NUMERO1 = float(input("INFORME UM NUMERO:  "))
    NUMERO2 = float(input("INFORME OUTRO NUMERO:  "))
    OPERADOR = input("INFORME A OPERAÇÃO QUE VOCÊ DESEJA REALIZAR [ + - * \ ]: ")
    OPERADORES_PERMITIDOS = "+/*-"
    
    if len(OPERADOR)>1:
        print("DIGITE APENAS UM OPERADOR")
        continue
    if OPERADOR not in OPERADORES_PERMITIDOS:
        print("OPERADOR INFORMADO NÃO É PERMITIDO: ")
        continue
    if OPERADOR == '+':
        print(F"{NUMERO1} + {NUMERO2}=", NUMERO1 + NUMERO2)
    if OPERADOR == '-':
        print(F"{NUMERO1} - {NUMERO2}=", NUMERO1 - NUMERO2)
    if OPERADOR == '/':
        if NUMERO2 ==0:
            print("DIVISÃO POR 0 É INVÁLIDA")
            continue
        if NUMERO2 !=0:
             print(F"{NUMERO1} / {NUMERO2}=", NUMERO1 / NUMERO2)
    if OPERADOR =='*':
         print(F"{NUMERO1} * {NUMERO2}=", NUMERO1 * NUMERO2)
    SAIR = input("\n[S] SAIRB\n[N] PARA CONTINUAR ").lower().startswith("s") 
    if SAIR == True:
        break



