import csv

if __name__ == "__main__":
    
    preguntascsv = open("preguntas.csv", encoding = "utf-8")
    datoscsv = list(csv.DictReader(preguntascsv))
    preguntascsv.close()

    print("************************************************")
    print("¡¡¡¡¡¡¡BIENVENIDOS A TRIVIA: ¿Preparados?!!!!!!!")

    puntaje_jugador_1 = 0
    puntaje_jugador_2 = 0

    jugador_1 = str(input("Por favor ingrese el nombre del primer jugador: "))
    jugador_2 = str(input("Por favor ingrese el nombre del segundo jugador: "))

    print("************************************************")
    print("{} y {} mucha suerte con las 7 preguntas. Comenzemos.".format(jugador_1.capitalize(), jugador_2.capitalize()))

    pregunta_numero = 1

    for pregunta_numero in range(1, len(datoscsv) +1):
        print("-------------------------------------")
        print(f"Pregunta Nº {pregunta_numero}:", datoscsv[pregunta_numero - 1]["preguntas"])
        print("1 -", datoscsv[pregunta_numero - 1]["opcion_1"])
        print("2 -", datoscsv[pregunta_numero - 1]["opcion_2"])
        print("3 -", datoscsv[pregunta_numero - 1]["opcion_3"])
        print("4 -", datoscsv[pregunta_numero - 1]["opcion_4"])
        print("5 -", datoscsv[pregunta_numero - 1]["opcion_5"])
        print("-------------------------------------")

        print(f"{jugador_1.capitalize()} elija su respuesta:", end = " ")
        respuesta_jugador_1 = int(input())
        print(f"{jugador_2.capitalize()} elija su respuesta:", end = " ")
        respuesta_jugador_2 = int(input())
        print("---")

        if respuesta_jugador_1 == 1:
            print(f"* {jugador_1.capitalize()} tu respuesta es correcta, se te sumará 10 puntos.")
            puntaje_jugador_1 += 10
        else:
            print(f"* {jugador_1.capitalize()} tu respuesta es incorrecta, no se te sumará puntos.")
        if respuesta_jugador_2 == 1:
            print(f"* {jugador_2.capitalize()} tu respuesta es correcta, se te sumará 10 puntos.")
            puntaje_jugador_2 += 10
        else:
            print(f"* {jugador_2.capitalize()} tu respuesta es incorrecta, no se te sumará puntos.")
    
        pregunta_numero += 1

    print("-------------------------------------")
    print(f"Bien echo, ahora mostraremos sus puntajes:")
    print(f"{jugador_1.capitalize()} obtuvo {puntaje_jugador_1} puntos y {jugador_2.capitalize()} obtuvo {puntaje_jugador_2} puntos.")

    if puntaje_jugador_1 == puntaje_jugador_2:
        print(f"======= {jugador_1.upper()} y {jugador_2.upper()} HAN EMPATADO =======")
    elif puntaje_jugador_1 > puntaje_jugador_2:
        print(f"======= {jugador_1.upper()} HA GANADO =======")
    else:
        print(f"======= {jugador_2.upper()} HA GANADO =======")

    print("-------------------------------------")

    print("*******GRACIAS POR JUGAR <3*******")