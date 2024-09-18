
#variavel da condição
cond = 's'


while(cond == 's'):
    num1 = float(input("Insira o primeiro número para operação matemática "))

    print("Digite o número do operador matemático que deseja")

    sel = int(input("|1| + (SOMA)\n|2| - (SUBTRAÇÃO)\n|3| / (DIVISÃO)\n|4| * (MULTIPLICAÇÃO)\n"))

    num2 = float(input("Insira o segundo número para operação matemática "))


    if(sel == 1):
      print(num1+num2)
    elif(sel == 2):
      print(num1-num2)
    elif(sel == 3):
      print(num1/num2)
    elif(sel == 4):
      print(num1*num2)
    else:
      print("Número de seleção errado, tente novamente")

    cond = input("Deseja continuar? digite s ou n\n")

  #deixando o que está na variavel em minusculo
    cond = cond.lower()

    if(cond != 's' and cond != 'n'):
      print("Opção inválida, tente novamente")
      cond = 's'
