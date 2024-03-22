def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    pesos = int(vuelto)
    centavos = (vuelto - pesos)*100
    print("Ingresar gasto:")
    print (expense)
    print ("Dinero recibido")
    print (money)
    print("Vuelto")
    print ("Pesos:")
    print (vuelto)
    print ("Centavos:")
    print (centavos)
