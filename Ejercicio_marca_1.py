contador =1
suma= 0
mayor_100= False
while contador==10 or suma<100: 

        numero= int(input("Dame un número: "))
        contador+= 1
        suma =suma + numero


if suma>100:
    mayor_100=True
    print("La suma de los números dichos es mayor que 100, sobrepasa el límite")

if contador==10:
    print(f"Todos los números están introducidos, la suma es {suma}")
print('buenos dias amigos mios, que tal estamos, este es el cambio de Luis')