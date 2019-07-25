num1=int(input("digite el primer numero"))
num2=int(input("digite el segundo numero"))
op=int(input("digite 1)para sumar 2)para restar 3)para multiplicar 4)para dividir"))

if op==1:
    print("la suma es ",num1+num2)
elif op==2:
    print("la resta es ",num1-num2)
elif op==3:
    print("la multiplicacion ",num1*num2)
elif op==4:
    print("la dicion es ",num1/num2)
elif op!=1 and op!=2 and op!=3 and op!=4:
    print("no ingreso un numero correspondiente a una operacion en el codigo")
