name = input("Nombre: ").capitalize()
last_name = input("Apellido: ").capitalize()
id_num = input("Cédula: ")

if (not id_num.isnumeric()):
    print("Ingreso inválido, reinicie el programa.")
else:
    height = input("Altura (en mts): ")

    if (height.isnumeric()) or ((height.count(".")==1) and (("".join(height.split(".")).isnumeric()))):
        weight = input("Peso (en kg): ")

        if (weight.isnumeric()) or ((weight.count(".")==1) and (("".join(weight.split(".")).isnumeric()))):
            sport = input("Deporte favorito: ").title()
            average = input("Promedio de calificaciones: ")

            if (average.isnumeric()) or ((average.count(".")==1) and (("".join(average.split(".")).isnumeric()))):
                # se imprime la información

                print(f"""
    Hola, {name} {last_name}.

        Tu número de cédula es {id_num}.
        Tu altura en metros es {height}m.
        Tu peso en kilogramos es {weight}kg.
        Tu Body Mass Index es {float(weight)/(float(height)**2)}Kg/m^2.
        Tu deporte favorito es {sport}.
        Tu promedio de calificaciones es {average}.

    Hasta pronto!
                """)
            else:
                print("Ingreso inválido, reinicie el programa.")
        else:
            print("Ingreso inválido, reinicie el programa.")
    else:
        print("Ingreso inválido, reinicie el programa.")
