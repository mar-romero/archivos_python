'''
Archivos [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    print("Cuenta caracteres")
    cantidad_letras = 0

    '''
    Realizar un prorgrama que cuenta la cantidad de caracteres
    (todo tipo de caracter, los espacios cuentan) de un archivo.
    Abra el archivo "text.txt" en modo "lectura", lea linea a
    linea el archivo, y cuente la cantidad de caracteres de cada línea.
    Debe realizar la sumatoria total de la cantidad de caracteres de todas
    las líneas para obtener el total del archivo e imprimirlo en pantalla
    '''
    with open('texto.txt',"r") as fi:
        for line in fi:
            cantidad_letras+=len(line)
        print('La cantiad de letras en el texto es: ',cantidad_letras)

def ej2():
    print("Transcribir!")
    cantidad_letras = 0
    cantidad_letra = 0
    '''
    Deberá abrir un archivo txt para escritura (un archivo nuevo)
    Luego mediante un bucle deberá pedir por consola que
    se ingrese texto. Todo el texto ingresado por consola
    debe escribirse en el archivo txt, cada entrada de texto
    deberá ser una línea en el archivo.
    El programa termina cuando por consola no se ingresa
    nada (texto vacio). En ese momento se termina el bucle
    y se cierra el archivo.
    Durante la realización del bucle y el ingreso de texto por
    consola, se debe ir contanto cuandos caracteres se ingresaron
    por consola, al fin de al terminar el bucle saber cuantos
    caracteres se copiaron al archivo.
    NOTA: Recuerde agregar el salto de línea "\n" a cada entrada
    de texto de la consola antes de copiar la archivo.
    '''
    no = open('mer.txt', "w")
    while True:
        print('Ingrese texto que desee guardar si quiere terminar no ingrese nada y aprete enter')
        tx=str(input('Ingrese el texto que desee guardar:'))
        if tx == "":
            break
        no.write(tx + '\n')
        no.flush()
        cantidad_letras=(len(tx))
        print('Cantidad de letras ingresadas:', cantidad_letras)
    no.close()
    with open('mer.txt',"r") as fi:
        for line in fi:
            cantidad_letra+=len(line)
    print('La cantiad de letras en el texto es: ',cantidad_letra)
    

def ej3():
    print("Escrutinio de los alquileres de Capital Federal")
    cantidad_ambientes = 2

    '''
    Realizar un prorgrama que solicite la cantidad de
    ambientes de los alquileres que se desean analizar.
    Abra el archivo "propiedades.csv" y mediante un bucle analizar:
    1) Contar cuantos alquileres en "pesos" hay disponibles
    en la cantidad de ambientes deseados.
    2) Obtener el promedio del valor de los alquileres en "pesos"
    de la cantidad de ambientes deseados.
    3) Obtener el máximo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    4) Obtener el mínimo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    '''
    import csv  
    import sys
    cant_am=0
    ars_1 = 0
    min_max = []
    with open('propiedades.csv') as fo:
        data = list(csv.DictReader(fo))
        while True:
            try:
                am  = int(input('De cuantos ambientes quiere el departamento: '))
                for i in range(len(data)):
                    amb = data[i]
                    ambiente = int(amb.get('ambientes'))
                    if ambiente == am :   
                        if data[i].get('moneda') == 'ARS':
                            ars = float(amb.get('precio'))
                            min_max.append(ars)
                            cant_am += 1    
                            ars_1 += ars                        
                try:
                    promedio = ars_1 / cant_am  
                    print ('La cantidad de departamentos de {} ambientes en ARS son: {}'.format(am,cant_am))
                    print ('El promedio de los departamentos de {} ambientes en ARS es: $ %.2f'.format(am) %(promedio))
                    print('El precio mas alto de de los departamentos de',am,'es: $',max(min_max)) 
                    print('El precio mas bajo es de los departamentos de',am,'es: $',min(min_max))         
                    break
                except:
                    print('No hay departamentos con los ambientes requeridos')
                    division = sys.float_info.max
            except ValueError:
                print ("ATENCIÓN: Debe ingresar un número de ambientes.")

        
def ej4():
    print("Ahora sí! buena suerte :)")

    '''
    Para poder realizar este ejercicio deberán descargarse el
    dataset "2019 Ironman world championship results" del siguiente
    link:
    https://www.kaggle.com/andyesi/2019-ironman-world-championship-results/data#

    Una vez tengan descargado el archivo CSV lo pueden observar un poco.
    En principio le daremos importancia a las siguientes columnas:

    Division: Esta columna marca la divisón del corredor por experiencia o edad.
    Swim: Tiempo nadando
    Bike: Tiempo en bicicleta
    Run: Tiempo corriendo

    Queremos investigar las siguientes divisiones o categorias:
    - MPRO
    - M45-49
    - M25-29
    - M18-24

    De cada una de estas categorías de corredores deseamos que analices
    por separado el tiempo de Swim, Bike y Run. En cada caso (para los 3)
    se desea obtener
    1) El tiempo máximo realizado por un corredor en dicha categoria
    2) El tiempo mínimo realizado por un corredor en dicha categoria
    3) El tiempo promedio de dicha categoria

    Es decir, por ejemplo voy a investigar la categoria M45-49 en "Run"
    - Debo buscar de todos los M45-49 cual fue el mayor tiempo en Run
    - Debo buscar de todos los M45-49 cual fue el menor tiempo en Run
    - Debo buscar de todos los M45-49 el tiempo Run y calcular el promedio

    Para poder realizar este ejercicio necesitará muchas variables para almacenar
    los datos, puede organizarse como mejor prefiera, en listas, con diccionarios,
    lo que se sienta más comodo.

    Es valido recorrer todo el archivo para extrer la información ordenada
    y almacenarlas en listas según el criterio que escojan.

    NOTA:
    Recomendamos empezar de a poco, los primeros ensayos realizarlo
    con una sola categoría de edad en solo una sección (Bike, Run, Swim)
    de la carrera. Sería igual al ej4 la información recolectada y calculada.

    '''
    import csv
    import mar as ma
    import datetime
    import time
    run_1 = 0
    swim_1 = 0
    bike_1 = 0
    swim_total = 0
    run_total = 0
    bike_total = 0
    lista_swim = []
    lista_bike = []
    lista_run = []
    lista_total = ['Swim', 'Bike', 'Run']
    with open("iroman.csv") as fo:
        data = list(csv.DictReader(fo))
        run = ma.menu()
        for i in range(len(data)):
            if data[i].get('Division') == run:
                for y in lista_total:
                    if data[i].get(y) != "":  #quise hacerlo con remove o strip y no pude(eliminar el valor vacio de la lista)
                        tiempo = data[i].get(y) #lo unico que se me ocurrio es entre al bucle cuando sea diferente a ""
                        tiempo = tiempo.split(":")# hay alguna solucion con remove o strip?
                        for u in range(3):
                            tiempo[u]= int(tiempo[u])
                        total_tiempo = tiempo[0]*3600 + tiempo[1]*60 + tiempo[2]
                        if y =='Swim':
                            lista_swim.append(total_tiempo)
                            swim_1 += 1
                            swim_total += total_tiempo
                        if y == 'Bike':
                            lista_bike.append(total_tiempo)
                            bike_1 += 1
                            bike_total += total_tiempo
                        if y == 'Run':
                            run_1 += 1
                            run_total += total_tiempo
                            lista_run.append(total_tiempo)
    swim_max = (max(lista_swim))
    run_max = (max(lista_run))
    bike_max = (max(lista_bike))
    swim_min = (min(lista_swim))
    run_min = (min(lista_run))
    bike_min = (min(lista_bike))
    pro_run = run_total / run_1
    pro_bike = bike_total / bike_1
    pro_swim = swim_total / swim_1
    max_sw= time.strftime('%H:%M:%S', time.gmtime(swim_max))
    max_run= time.strftime('%H:%M:%S', time.gmtime(run_max))
    max_bike= time.strftime('%H:%M:%S', time.gmtime(bike_max))
    min_sw= time.strftime('%H:%M:%S', time.gmtime(swim_min))
    min_run= time.strftime('%H:%M:%S', time.gmtime(run_min))
    min_bike= time.strftime('%H:%M:%S', time.gmtime(bike_min))
    swim_pro= time.strftime('%H:%M:%S', time.gmtime(pro_swim))
    run_pro= time.strftime('%H:%M:%S', time.gmtime(pro_run))
    bike_pro= time.strftime('%H:%M:%S', time.gmtime(pro_bike))
    print("El tiempo mas alto es: ",max_sw,'el tiempo mas bajo es : ',min_sw,'y el promedio es: ', swim_pro,'para la division ',run,'en la categoria SWIM')
    print("El tiempo mas alto es: ",max_run,'el tiempo mas bajo es : ',min_run,'y el promedio es: ', run_pro,'para la division ',run,'en la categoria RUN')
    print("El tiempo mas alto es: ",max_bike,'el tiempo mas bajo es : ',min_bike,'y el promedio es: ', bike_pro,'para la division ',run,'en la categoria BIKE')

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    ej4()
