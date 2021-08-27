def checker():
	files_check = int(input("Indique el número de ficheros a analizar:"))
	print("\n\nCheckeando los datos analizados. Espere un momento....")
	# Abre archivo en modo lectura
	archivo = open('check.log','r')  
	print ("Nombre del fichero: ", archivo.name)

	# Guarda en la lista line todas las líneas con \n al final
	line = archivo.readlines()

	#contador 
	linea_ok = 0
	linea_bad = 0
	num_no_process=[]

	# inicia bucle infinito para leer línea a línea

	for x in range(files_check):
		numero = str(x) + '\n'
		if numero in line:
			linea_ok += 1
		

		if numero not in line:
			linea_bad += 1
			num_no_process.append(numero)

	archivo.close()  # Cierra archivo

	print (f'Se han procesado {linea_ok + linea_bad} numeros de su base de datos.')
	print (f'Lineas procesadas correctamente: {linea_ok + 2}')
	print (f'Lineas procesadas incorrectamente: {linea_bad - 2}')
	print ("La lista de lineas de su base de datos que no se han procesado es la siguiente: ")
	print (num_no_process[2:])

