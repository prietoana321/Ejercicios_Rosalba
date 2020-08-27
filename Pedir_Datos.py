
#OPERACIONES DE INGRESO Y MUESTRA DE DATOS

#PERTENECE A ANA CECILIA PRIETO GRUPO 1

#salidas
#nombre="tony"
#edad=14
#print("hola",nombre,"tienes",edad,"años")
#entrada de datos
#nombre=input("Digite su nombre")
#print("hola"(nombre))
#numero=int(input("Digite un numero entero"))

#n=int("0b1010",2)
#print(n)

#exadecimal a entero

#n=int("0xa",16)
#print(n)

#Redondeo

#n=round(9.6578978)
#print(n)

#cuantos caracteres

#n=len("casa")
#print(n)

#a=float(input("digite el valor"))
#b=float(input("Digite el valor"))
#c=float(input("digite el vALOR"))

#A=float(input("Digite el valor de a:"))
#B=float(input("Digite el valor de b:"))

#resultado=((3+5*8)and(-6/3*4)+2)or(a>b)
#print(f"El resultado es:{resultado}")

#a=input("Digite elvalor de a ")
#b=input("digite el valor de b:")
#a,b=b,a
#print("el nuevo valor nuevo de a:")

#cap_inversion=float(input("Digite el capital invertido:"))
#ganancia=cap_inversion*0.02
#print(ganancia)

#ejercicio 2
#salario_basico=float(input("Digite su salario basico"))
#v1=float(input("digite el valor de la primera venta"))
#v2=float(input("Digite el valor de la segunda compra"))
#v3=float(input("Digite el valor de la tercera compra"))

#total_venta=v1+v2+v3
#comisiones=total_venta*0.10
#salario_final=salario_basico+comisiones
#print(salario_final)

#ejercicio 4

#calificacion_1=float(input("Digite la primera calificacion"))
#calificacion_2=float(input("digite su segunda calificacion"))
#calificacion_3=float(input("digite la tercera calificacion"))
#examen_final=float(input("Digite la calificacion del examen final"))
#Trabajo_final=float(input("Digite la calificacion del trabajo final"))
#promedio=(calificacion_1+calificacion_2+calificacion_3)/3
#porcentaje_parcial=promedio*0.55
#promedio_examen_Final=examen_final*0.30
#promedio_trabajo_final=Trabajo_final*0.15
#calificacion_final=porcentaje_parcial+promedio_examen_Final+promedio_trabajo_final
#print(calificacion_final)

#ejercicio 5

#numero_hombres=int(input("digite la cantidad de hombres"))
#numero_mujeres=int(input("Digite la cantidad de mujeres"))
#total_alumnos=numero_hombres+numero_mujeres
#porcentaje_de_hombres=(numero_hombres*100)/total_alumnos
#porcentaje_mujeres=(numero_mujeres*100)/total_alumnos
#print("el porcentaje de hombres equivale al",porcentaje_de_hombres,"porcentaje de mujeres en el grupo",porcentaje_mujeres)

#ejercicio 6

#fecha_nacimiento_dia=int(input("digite el dia en que nació"))
#fecha_nacimiento_mes=int(input("digite el mes"))
#fecha_nacimiento_año=int(input("Digite el año en que nacio"))

#fecha_actual_dia=int(input("Digite el dia actual"))
#fecha_actual_mes=int(input("Digite el mes"))
#fecha_actual_año=int(input("Digite el año actual "))

#if fecha_nacimiento_mes>fecha_actual_mes:
 #   edad=(fecha_actual_año-fecha_nacimiento_año)-1
  #  print(edad)
#elif fecha_nacimiento_mes<fecha_actual_mes:
 #     edad=fecha_actual_año-fecha_nacimiento_año
  #    print(edad)
#elif fecha_nacimiento_año==fecha_actual_año:
 #       if fecha_nacimiento_dia>fecha_actual_dia:
  #          edad=(fecha_actual_año-fecha_nacimiento_año)-1
   #         print(edad)
    #      elif fecha_nacimiento_año<fecha_actual_dia:
     #           edad=(fecha_actual_año-fecha_nacimiento_año)-1
      #          print(edad)
       #   elif fecha_nacimiento_dia==fecha_actual_dia:
        #        edad=fecha_actual_año-fecha_nacimiento_año
         #       print("feliz cumpleaños",edad)
          #else:
        #else:
#else:
 #print("edad incorrecta")

#problemas propuestos

#cantidad_pesos=float(input("Digite la cantidad en pesos que desea convertir"))

#a=cantidad_pesos
#b=0.00027
#c=a*b
#print("la cantidad equivaldria en dolares a",c)

#problema 2

#PROBLEMA 3
#presion=float(input("digite la presion"))
#volumen=float(input("digite el volumen"))
#temperatura=float(input("digite la temperatura"))
#masa=(presion*volumen)/(0.37*(temperatura+460))
#print("la masa es",masa)

#PROBLEMA 4
#edad=int(input("digite la edad"))
#numerodepulsaciones=(220-edad)/10

#PROBLEMA 5
#salarioanterior=float(input("digite su antiguo salario"))
#salarioactual=(salarioanterior*25)/100
#print("salarioactual",salarioactual)


#PROBLEMA 6
#presupuestohospital=float(input("digite el presupuesto de el hospital"))
#ginecologia=(presupuestohospital*40)/100
#print("el presupuesto que le corresponde a el area de ginecologia es", ginecologia)
#traumatologia=(presupuestohospital*30)/100
#print("el presupuesto que le corresponde a el area de traumatologia es",traumatologia)
#pediatria=(presupuestohospital*30)/100
#print("el presupuesto que le corresponde a el area de pediatria",pediatria)


#PROBLEMA 7
#presioarticulo=float(input("digite el presio del articulo"))
#presiototal=(presioarticulo*30)/100
#print("el articulo tiene un costo total de",presiototal)


#PROBLEMA 8
#cronometrolunes=float(input("digite el tiempo marcado en el cronometro hoy lunes"))
#cronometromiercoles=float(input("digite el tiempo marcado en el cronometro miercoles"))
#cronometroviernes=float(input("digite el tiempo marcado en el cronometro viernes"))
#tiempoderuta=cronometrolunes+cronometromiercoles+cronometroviernes
#promediodetiempo=tiempoderuta/3
#print("el promedio es",promediodetiempo)


#PROBLEMA 9
#persona1=float(input("digite la cantidad invertida"))
#persona2=float(input("digite la cantidad invertida"))
#persona3=float(input("digite la cantidad invertida"))




#PROBLEMA 10
#calificacionexamenmate=float(input("digite la calificacion del examen de matematicas"))
#promedioexamenmate=calificacionexamenmate*90/100
#mate1=float(input("digite la calificacion de la primera tarea de mate"))
#mate2=float(input("digite la calificacion de la segunda tarea de mate"))
#mate3=float(input("digite la calificion de la tercera tarea de mate"))
#totalcalificacion=mate1+mate2+mate3
#promediodetareas=totalcalificacion*10/100
#totalmate=promedioexamenmate+promediodetareas
#calificacionexamenfisica=float(input("digite la calificacion del examen de fisica"))
#promedioexamenfisica=calificacionexamenfisica*80/100
#fisica1=float(input("digite la calificacion de la primera tarea de fisica"))
#fisica2=float(input("digite la calificacion de la segunda tarea de fisica"))
#totalcalificacion=fisica1+fisica2
#promediodetareas=totalcalificacion*20/100
#totalfisica=promedioexamenfisica+promediodetareas
#calificacionexamenquimica=float(input("digite la calificacion del examen de quimica"))
#promedioexamenquimica=calificacionexamenquimica*85/100
#quimica1=float(input("digite la calificacion de la primera tarea de quimica"))
#quimica2=float(input("digite la calificacion de la segunda tarea de quimica"))
#quimica3=float(input("digite la calificion de la tercera tarea de quimica"))
#totalcalificacion=quimica1+quimica2+quimica3
#promediodetareas=totalcalificacion*15/100
#totalquimica=promedioexamenquimica+promediodetareas
#promediogeneral=totalmate+totalfisica+totalquimica