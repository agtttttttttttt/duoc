entradas_Platinum= [""] * 20
entradas_Gold = [""] * 30
entradas_silver = [""] * 70
asistentes = []
ganancias_Platinum = 0
ganancias_Gold = 0
ganancias_silver = 0
nombre=(input("ingrese su Nombre y Apeliido: "))
def mostrar_menu():
  print()
  print("---------------MENU----------------")
  print("1) Comprar Entradas")
  print("2) Mostrar Ubicaciones Disponibles")
  print("3) Ver Listado De asistentes")
  print("4) Mostrar Ganancias totales")
  print("5) Salir")
def mostrar_ubicaciones_disponibles():
  variable_espaciado = 0
  print("Asientos disponibles: ")
  for repeticion in range(len(entradas_Platinum)):
    variable_espaciado = variable_espaciado + 1
    if(entradas_Platinum[repeticion]==""):
      if variable_espaciado==11:
        print("")
      print(repeticion+1, end=" ")
    else:
      if variable_espaciado==11:
        print("")
      print("X",end=" ")
  print()
  for repeticion in range(len(entradas_Gold)):
    if(entradas_Gold[repeticion]==""): 
      variable_espaciado = variable_espaciado + 1
    if(entradas_silver[repeticion]==""):
      if variable_espaciado==11 or variable_espaciado==21 or variable_espaciado==31 or variable_espaciado==41 or variable_espaciado==51 or variable_espaciado==61 or variable_espaciado==71 or variable_espaciado==81 or variable_espaciado==91 :
        print("")
      print(repeticion+21,end=" ")
    else:
      print("X",end=" ")
  print()
  variable_espaciado = 0
  for repeticion in range(len(entradas_silver)):
    variable_espaciado = variable_espaciado + 1
    if(entradas_silver[repeticion]==""):
      if variable_espaciado==11 or variable_espaciado==21 or variable_espaciado==31 or variable_espaciado==41 or variable_espaciado==51 or variable_espaciado==61 or variable_espaciado==71 or variable_espaciado==81 or variable_espaciado==91 :
        print("")
      print(repeticion+31, end=" ")
    else:
      if variable_espaciado==11:
        print("")
      print("X",end=" ")
def comprar_entradas():
  global ganancias_Platinum
  global ganancias_Gold
  global ganancias_silver
  cantidad = int(input("Ingrese la cantidad de entradas solo pueden ser 1 o 3"))
  if(cantidad <= 0 or cantidad >= 4):
    print("xfavor ingrese un valor dentro del rango")
    return
  print(cantidad)
  for repeticion in range(cantidad):
    print("estas son las ubicaciones disponibles :")
    mostrar_ubicaciones_disponibles()
    ubicacion_valida = False
    while not ubicacion_valida:
      print("")
      ubicacion = int(input("escoja un opccion valida : "))
      if ubicacion >= 1 and ubicacion <= 100:
        if ubicacion <= 20 and entradas_Platinum[ubicacion-1] == "":
          entradas_Platinum[ubicacion-1] = ingresar_rut()
          ubicacion_valida = True
          ganancias_Platinum = ganancias_Platinum + 120000
          asistentes.append(entradas_Platinum[ubicacion -1])
        elif ubicacion <= 50 and entradas_Gold[ubicacion-21] == "":
          entradas_Gold[ubicacion-21] = ingresar_rut()
          ubicacion_valida = True
          ganancias_Gold = ganancias_Gold + 80000
          asistentes.append(entradas_Gold[ubicacion -21])
        elif ubicacion <= 100 and entradas_silver[ubicacion-51] == "":
          entradas_silver[ubicacion-31] = ingresar_rut()
          ubicacion_valida = True
          ganancias_silver = ganancias_silver + 50000
          asistentes.append(entradas_silver[ubicacion -31])
        if not ubicacion_valida:
          print("esta ubicacion no esta valida")
    print("Operación realizada ")
def ingresar_rut():
  run_valido = False
  while not run_valido:
    run = input("Ingrese el RUN sin el digito verificador y sin puntos :")
    if(len(run) == 7 or len(run) == 8):
      run_valido = True
  return run
def mostrar_asistentes():
  print("lista de asistentes")
  asistentes.sort()
  for asistente in asistentes:
    print(asistente, end=".")
def mostrar_ganancias():
  print ("Ganancias por segmento!")
  print (ganancias_Platinum)
  print (ganancias_Gold)
  print (ganancias_silver)
def inicio():
  try:
    while True:
      mostrar_menu()
      opcion = int(input("seleccione una opcion "))
      if opcion == 1:
        comprar_entradas()
      elif opcion == 2:
        mostrar_ubicaciones_disponibles()
      elif opcion == 3:
        mostrar_asistentes()
      elif opcion == 4:
        mostrar_ganancias()
      elif opcion == 5:
        print("usted salio del programa,gracias:",nombre)
        break
  except:
    print("error")
inicio()

