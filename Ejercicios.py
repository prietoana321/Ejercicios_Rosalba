

#OPERACIONES SENCILLAS CON PAYTON

#PERTENECE A ANA CECILIA PRIETO GRUPO 1

#si son pares o no son pares
#num1=int(input("digite un numero:"))
#num2=int(input("digite otro numero:"))
#if num1%2==0 and num2%2==0:
#  print("ambos numeros son pares")
#elif num1%2==0 and num2%2!=0:
#  print(f"{num1}es par")


#mayor o menor
#num1=int(input("digite un numero:"))
#num2=int(input("digite otro numero:"))
#num3=int(input("digite un  numero mas:"))
#if  num1>=num2 and num1>=num3:
    #print(f"el numero mayor es: {num1}")
#elif num2>=num1 and num2>=num3:
# print(f"el numero mayor es : {num2}")
#elif num3>=


#vocal o no
#letra input("digite un <caracter")
#if letra=='a'or letra=='e'or letra=='i'or letra=='o'or letra=='u':
#  print("es una vocal")
#else:
    #print("no es una vocal")





#calculadora
#num1=float(input("digite un numero"))
#num2=float(input("digite otro numero"))
#operacion input("digite la operacion") .upper()
#if operacion =='S':
    #  suma=num1+num2
#  print(f"\n la suma es: {suma}")
#elif operacion=='R':
    # resta=num1-num2
# print(f"\n la resta es {resta}")
#elif operacion =='M':
    # multiplicacion=num1*num2
#  print(f"\n la multiplicacion es {multiplicacion}")
#elif operacion=='D':
    # dividir=num1/num2
# print(f"\n la divicion es {dividir:.2f}")
#else:
# print("se equivoco de operacion")



#cajero
#saldo=1000
#print("\t menu:.")
#print("1. ingresar dinero a la cuenta")
#print("2. Retirar dinero de la cuenta")
#print("3. Mostrar dinero disponible")
#print("4.Salir")

#opcion=int(input("digite una opcion del menu"))
#print() #salto de linea entre las opciones
#if opcion==1:
    # extra=float(input("cuanto dinero desea ingresar"))
    # saldo=saldo+extra
# print(f"el dinero de la cuenta es de {saldo}")
#elif opcion==2:
    #retirar=float(input("cuanto dinero deseas retirar"))
    #if retirar>saldo:
    # print("fondos insufisientes")
    # else:
    # retirar==saldo
        #print(f"el dinero en la cuenta es: {saldo}")
    #elif opcion==3:
    #print("el saldo disponible es:{saldo}")
    #elif opcion==4:
# print("mil gracias por utilizar nuestros servicios")
#else:
# print("Error.se equivoco de opcion ")


#intereses en la cuenta

capital=float(input("digite el capital"))
porsentajeinteres=float(input("digite el porcentaje interes"))
intereses=capital*porsentajeinteres
if intereses>7000:
 capitalf=capital+intereses
print("elcapital final fue de ",capitalf)



#aprueba o reprueba

calificacion1=float(input("digite la primera calificacion"))
calificacion2=float(input("digite la segunda calificacion"))
calificacion3=float(input("digite la tercera calificacion"))
promedio=(calificacion1+calificacion2+calificacion3)/3
if promedio>=70:
 print("el alumno a sido aprobado")
else:
  print("el alumno a sido reprobado")



#descuento almacen

compra=float(input("digite el valor de la compra"))
if compra>1000:
   descuento=compra*0.20
else:
    descuento=0

totalpagar=compra-descuento
print("el total a pagar es ",totalpagar)



#salario

horastrabajadas=int(input("digite el numero de horas trabajadas"))
horasextras=int(input("digite el numero de horas extras trabajadas"))
if horastrabajadas>40:
      horasextras=horastrabajadas-40
      salariosemanal=horasextras*20+40*16
else:
      salariosemanal=horastrabajadas*16
      print("el salario semanal del obrero es ",salariosemanal)



#dos numeros de forma ascendente

num1=float(input("digite un numero"))
num2=float(input("digite otro numero"))
if num1<num2:
 print("el numero1 es" ,num1,"el numero2 es ",num2)
else:
 print("el numero2 es" ,num2,"el numero1 es",num1)