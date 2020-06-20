
 
def menu():
    import os
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('clear') # NOTA para windows tienes que cambiar clear por cls
	print ("Ingrese la categoria que quiere analizar")
	print ("\tMPRO")
	print ("\tM45-49")
	print ("\tM25-29")
    print('\tM18-24')
	print ("\tsalir")
 
 
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu == 'MPRO' :
		print ("")
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")
	elif opcionMenu == 'M45-49':
		print ("")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")
	elif opcionMenu == 'M25-29' :
		print ("")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
		elif opcionMenu == 'M18-24' :
		print ("")
		input("Has pulsado la opción 4...\npulsa una tecla para continuar")
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
return opcion_Menu