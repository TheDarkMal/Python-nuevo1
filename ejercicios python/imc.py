print("Bienvenido a imc calculator")


altura=int(print("digite su altura"))

imc=peso/(altura*2)

if imc <18.5:
    print("esta bajo de peso")
elif imc ==18.5 and imc<=24.9:
    print("esta normal de peso")
elif imc==25 and imc <=29.9 :
    print("esta sobrepeso de peso")
elif imc ==300 and imc <=34.9:
    print("esta en ovesidad 1")
elif imc ==35 and imc<=39.9:
    print("esta ovesidad 2")
elif imc ==40 and imc <=49.9:
    print("esta en ovesidad 3")
elif imc >50:
    print("esta en ovesidad 4")
