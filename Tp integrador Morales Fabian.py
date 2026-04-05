
#TP integrador – Repetitivas- Condicionales y Secuenciales.

#Ejercicio 1— “Caja del Kiosco”


nombre = input("Cliente: ").strip()

while nombre == "" or not nombre.isalpha():
    print("Error: Ingrese un nombre correcto y que contenga solo letras")
    nombre = input("Cliente: ").strip()

cantidad_str = input("Cantidad de productos: ").strip()

while not cantidad_str.isdigit() or int(cantidad_str) == 0:
    print("Error: Ingrese un número entero mayor a cero")
    cantidad_str = input("Cantidad de productos: ").strip()

cantidad_int = int(cantidad_str)

total_sin_descuento = 0
total_con_descuento = 0.0
detalle_productos = ""

for i in range(1, cantidad_int + 1):
    precio_str = input(f"Producto {i} - Precio: ").strip()

    while not precio_str.isdigit() or int(precio_str) == 0:
        print("Error: el precio debe ser un entero positivo")
        precio_str = input(f"Producto {i} - Precio: ").strip()

    precio_int = int(precio_str)

    desc = input("Descuento (S/N): ").strip().lower()

    while desc != "s" and desc != "n":
        print("Error: Ingrese S para si o N para no")
        desc = input("Descuento (S/N): ").strip().lower()

    total_sin_descuento += precio_int

    if desc == "s":
        precio_final = precio_int * 0.9
    else:
        precio_final = precio_int

    total_con_descuento += precio_final

    detalle_productos += f"Producto {i} - Precio: {precio_int}  Descuento (S/N): {desc}\n"

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_int

print(f"\nCliente: {nombre}")
print(f"Cantidad de productos: {cantidad_int}")
print(detalle_productos)
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")




#Ejercicio 2 — “Acceso al Campus y Menú Seguro”


usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 0
acceso = False

while intentos < 3 and not acceso:
    print("\nIntento", intentos + 1, "/3")
    usuario = input("Usuario: ").strip()
    clave = input("Clave: ").strip()

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso = True
    else:
        print("Error: credenciales inválidas.")
        intentos += 1

if not acceso:
    print("Cuenta bloqueada")
else:
    salir = False

    while not salir:
        print("\n1) Estado")
        print("2) Cambiar clave")
        print("3) Mensaje")
        print("4) Salir")

        opcion = input("Opción: ")

        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
        else:
            opcion = int(opcion)

            if opcion < 1 or opcion > 4:
                print("Error: opción fuera de rango.")
            else:
                if opcion == 1:
                    print("Inscripto")

                elif opcion == 2:
                    nueva_clave = input("Nueva clave: ")

                    if len(nueva_clave) < 6:
                        print("Error: mínimo 6 caracteres.")
                    else:
                        confirmacion = input("Confirmar clave: ")

                        if nueva_clave != confirmacion:
                            print("Error: las claves no coinciden.")
                        else:
                            clave_correcta = nueva_clave
                            print("Clave cambiada correctamente.")

                elif opcion == 3:
                    print("No tengas miedo de fallar, ten miedo de no intentarlo")

                elif opcion == 4:
                    print("Saliendo del sistema...")
                    salir = True


#    Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres”    


lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Ingrese nombre del operador: ")
while operador.isalpha() == False:
    print("Error. El nombre debe tener solo letras.")
    operador = input("Ingrese nombre del operador: ")

opcion = 0

while opcion != 5:
    print("\n--- MENU ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Ingrese una opción: ")
    while opcion.isdigit() == False or int(opcion) < 1 or int(opcion) > 5:
        print("Error. Ingrese una opción válida.")
        opcion = input("Ingrese una opción: ")

    opcion = int(opcion)

    if opcion == 1:
        dia = input("Ingrese día (1-Lunes, 2-Martes): ")
        while dia.isdigit() == False or int(dia) < 1 or int(dia) > 2:
            print("Error. Día inválido.")
            dia = input("Ingrese día (1-Lunes, 2-Martes): ")
        dia = int(dia)

        paciente = input("Ingrese nombre del paciente: ")
        while paciente.isalpha() == False:
            print("Error. El nombre debe tener solo letras.")
            paciente = input("Ingrese nombre del paciente: ")

        if dia == 1:
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Error. Ese paciente ya tiene turno en Lunes.")
            else:
                if lunes1 == "":
                    lunes1 = paciente
                elif lunes2 == "":
                    lunes2 = paciente
                elif lunes3 == "":
                    lunes3 = paciente
                elif lunes4 == "":
                    lunes4 = paciente
                else:
                    print("No hay turnos disponibles para Lunes.")

        elif dia == 2:
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Error. Ese paciente ya tiene turno en Martes.")
            else:
                if martes1 == "":
                    martes1 = paciente
                elif martes2 == "":
                    martes2 = paciente
                elif martes3 == "":
                    martes3 = paciente
                else:
                    print("No hay turnos disponibles para Martes.")

    elif opcion == 2:
        dia = input("Ingrese día (1-Lunes, 2-Martes): ")
        while dia.isdigit() == False or int(dia) < 1 or int(dia) > 2:
            print("Error. Día inválido.")
            dia = input("Ingrese día (1-Lunes, 2-Martes): ")
        dia = int(dia)

        paciente = input("Ingrese nombre del paciente: ")
        while paciente.isalpha() == False:
            print("Error. El nombre debe tener solo letras.")
            paciente = input("Ingrese nombre del paciente: ")

        if dia == 1:
            if paciente == lunes1:
                lunes1 = ""
            elif paciente == lunes2:
                lunes2 = ""
            elif paciente == lunes3:
                lunes3 = ""
            elif paciente == lunes4:
                lunes4 = ""
            else:
                print("Paciente no encontrado en Lunes.")

        elif dia == 2:
            if paciente == martes1:
                martes1 = ""
            elif paciente == martes2:
                martes2 = ""
            elif paciente == martes3:
                martes3 = ""
            else:
                print("Paciente no encontrado en Martes.")

    elif opcion == 3:
        dia = input("Ingrese día (1-Lunes, 2-Martes): ")
        while dia.isdigit() == False or int(dia) < 1 or int(dia) > 2:
            print("Error. Día inválido.")
            dia = input("Ingrese día (1-Lunes, 2-Martes): ")
        dia = int(dia)

        if dia == 1:
            print("\nAgenda de Lunes")
            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", lunes1)

            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", lunes2)

            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", lunes3)

            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print("Turno 4:", lunes4)

        elif dia == 2:
            print("\nAgenda de Martes")
            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", martes1)

            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", martes2)

            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", martes3)

    elif opcion == 4:
        ocupados_lunes = 0
        if lunes1 != "":
            ocupados_lunes = ocupados_lunes + 1
        if lunes2 != "":
            ocupados_lunes = ocupados_lunes + 1
        if lunes3 != "":
            ocupados_lunes = ocupados_lunes + 1
        if lunes4 != "":
            ocupados_lunes = ocupados_lunes + 1

        disponibles_lunes = 4 - ocupados_lunes

        ocupados_martes = 0
        if martes1 != "":
            ocupados_martes = ocupados_martes + 1
        if martes2 != "":
            ocupados_martes = ocupados_martes + 1
        if martes3 != "":
            ocupados_martes = ocupados_martes + 1

        disponibles_martes = 3 - ocupados_martes

        print("\nResumen general")
        print("Lunes - Ocupados:", ocupados_lunes, "Disponibles:", disponibles_lunes)
        print("Martes - Ocupados:", ocupados_martes, "Disponibles:", disponibles_martes)

        if ocupados_lunes > ocupados_martes:
            print("El día con más turnos es Lunes.")
        elif ocupados_martes > ocupados_lunes:
            print("El día con más turnos es Martes.")
        else:
            print("Hay empate entre Lunes y Martes.")

    elif opcion == 5:
        print("Sistema cerrado.")



#Ejercicio 4 — "Escape Room: La Bóveda"

# Variables iniciales

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0

# Nombre del agente

nombre = input("Ingresa tu nombre, agente: ")
while not nombre.isalpha():
    print("Error: solo se permiten letras.")
    nombre = input("Ingresa tu nombre, agente: ")

print(f"\nBienvenido, agente {nombre}. Debes abrir la boveda.")

# Loop principal

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:

# Regla de bloqueo por alarma

    if alarma and tiempo <= 3:
        print("SISTEMA BLOQUEADO. La boveda quedo sellada.")
        break

    print("\n" + "=" * 40)
    print(f"Energia: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {alarma} | Codigo parcial: {codigo_parcial}")
    print("=" * 40)

    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Elige una opcion: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: ingresa un numero entre 1 y 3.")
        opcion = input("Elige una opcion: ")

    opcion = int(opcion)

 # Opcion 1: Forzar cerradura

    if opcion == 1:
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        # Regla anti-spam: 3 veces seguidas forzando
        if racha_forzar == 3:
            alarma = True
            print("La cerradura se trabo. Alarma activada. No se abrio ninguna cerradura.")

        else:
            # Riesgo de alarma si energia < 40
            if energia < 40:
                print("Energia baja, riesgo de alarma.")
                num = input("Elige un numero del 1 al 3: ")
                while not num.isdigit() or int(num) < 1 or int(num) > 3:
                    print("Error: ingresa un numero entre 1 y 3.")
                    num = input("Elige un numero del 1 al 3: ")
                if int(num) == 3:
                    alarma = True
                    print("Mala suerte. La alarma se activo.")
                else:
                    cerraduras_abiertas += 1
                    print(f"Cerradura abierta. Cerraduras abiertas: {cerraduras_abiertas}/3")
            else:
                cerraduras_abiertas += 1
                print(f"Cerradura abierta. Cerraduras abiertas: {cerraduras_abiertas}/3")

    # Opcion 2: Hackear panel

    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        racha_forzar = 0

        print("Hackeando panel...")
        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"Paso {paso}/4 - Codigo parcial: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print(f"Hackeo exitoso. Cerradura abierta. Cerraduras abiertas: {cerraduras_abiertas}/3")
        else:
            print("Aun no lograste abrir la cerradura.")

    # Opcion 3: Descansar

    elif opcion == 3:
        tiempo -= 1
        racha_forzar = 0

        if alarma:
            energia -= 10
            print(f"Descansaste pero la alarma te costo 10 energia extra. Energia: {energia}")
        else:
            energia += 15
            if energia > 100:
                energia = 100
            print(f"Descansaste. Energia actual: {energia}")

# Chequeo de bloqueo al final del turno

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("SISTEMA BLOQUEADO. La boveda quedo sellada.")
        break

# Resultado final

print("\n" + "=" * 40)

if cerraduras_abiertas == 3:
    print(f"VICTORIA. Agente {nombre}, abriste la boveda.")
elif alarma and tiempo <= 3:
    print(f"DERROTA. La boveda quedo bloqueada, agente {nombre}.")
elif energia <= 0:
    print(f"DERROTA. Te quedaste sin energia, agente {nombre}.")
elif tiempo <= 0:
    print(f"DERROTA. Se acabo el tiempo, agente {nombre}.")
elif alarma:
    print(f"DERROTA. La alarma se activo, agente {nombre}.")

print("=" * 40)
print(f"Estado final - Energia: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3")



#Ejercicio 5 — “Escape Room:"La Arena del Gladiador"

#Nombre del Gladiador

nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

#Variables iniciales

vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_jugador = 15
danio_enemigo = 12
juego_activo = True

print("\n--- BIENVENIDO A LA ARENA ---")
print("=== INICIO DEL COMBATE ===")

#Loop principal


while juego_activo:

    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige accion:")
    print("1. Ataque Pesado")
    print("2. Rafaga Veloz")
    print("3. Curar")

    opcion = input("Opcion: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: Ingrese un numero valido.")
        opcion = input("Opcion: ")

    opcion = int(opcion)

# Accion 1: Ataque pesado

    if opcion == 1:
        if vida_enemigo < 20:
            danio_final = danio_jugador * 1.5
            print(f"¡Golpe Critico! Atacaste al enemigo por {danio_final} puntos de daño.")
        else:
            danio_final = danio_jugador
            print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")

        vida_enemigo -= danio_final
        if vida_enemigo < 0:
            vida_enemigo = 0

# Accion 2: Rafaga veloz

    elif opcion == 2:
        print("¡Inicias una rafaga de golpes!")
        for golpe in range(3):
            vida_enemigo -= 5
            if vida_enemigo < 0:
                vida_enemigo = 0
            print("> Golpe conectado por 5 de daño")

 # Accion 3: Curar

    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print(f"Usaste una pocion. Vida actual: {vida_jugador} | Pociones restantes: {pociones}")
        else:
            print("¡No quedan pociones!")

# Turno del enemigo

    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        if vida_jugador < 0:
            vida_jugador = 0
        print(f"¡El enemigo te ataco por {danio_enemigo} puntos de daño!")

 # Control del juego

    if vida_jugador == 0 or vida_enemigo == 0:
        juego_activo = False

# Fin del juego

print("\n" + "=" * 40)

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caido en combate.")

print("=" * 40)
print(f"Estado final - {nombre}: {vida_jugador} HP | Enemigo: {vida_enemigo} HP")
