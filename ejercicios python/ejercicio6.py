edad = int (input("digite su edad "))
genero = input("digite su genero M)masculino F)femeninbo")


if edad >=18 :
    if genero=='M' or genero =='h':
        print("señor, usted es mayor de edad")
    elif genero=='F'or genero=='f':
        print("señorita, usted es mayor de edad")
if edad<18:
    if genero=='M' or genero=='m':
        print("señor, usted es menor de edad")
    else:
        print("señorita, usted es menor de edad")

