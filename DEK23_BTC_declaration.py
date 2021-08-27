import os
import sys
import pandas as pd
from checker import checker


def presentacion():
	print ("""                  ********* BIENVENIDO A DEK23 BTC **********
		  ****** TUS DECLARACIONES DE CRYPTO ********

			       Version ALFA 1.0		    

		  ********* SOFTWARE BY DECKCARD23 ***********
				deckcard23.com
				@rickdeckard23             \n\n""")

def resumen():
	# CABECERA Y DECLARACIÓN DE VARIABLES
	os.system('clear')
	presentacion()
	global archivo
	newfile.write("""********* BIENVENIDO A DEK23 BTC **********
		  ****** TUS DECLARACIONES DE CRYPTO ********

			       Version ALFA 1.0		    

		  ********* SOFTWARE BY DECKCARD23 ***********
				deckcard23.com
				@rickdeckard23             """.encode())
	newfile.write("\n".encode())
	newfile.write("Nombre del archivo: ".encode())
	newfile.write(str(archivo).encode())
	df = pd.read_csv(archivo) # skiprows=1 es para no contar filas hay que poner la coma delante y espacio. sheet_name='Sheet1' para seleccionar la hoja. read_excel para leer bd
	num_files = df.shape[0]
	print("El número de líneas del fichero CSV es de", num_files)	
	
	
	ANODECLARA_INI = input ('Escribe la fecha de comienzo de la declaración (Ejemplo: 2018-04-04 20:19:34): ')
	ANODECLARA_FIN = input ('Escribe la fecha de final de la declaración (Ejemplo: 2018-04-04 20:19:34): ')
	type_coins = pd.unique(df['Coin'])
	len_coin = len(type_coins)
	print ("*******RESUMEN GLOBAL*******")
	newfile.write('***********RESUMEN GLOBAL BINANCE********* '.encode())
	newfile.write('\n\n'.encode())
	print("Esta declaración va desde  ", ANODECLARA_INI, "hasta  ", ANODECLARA_FIN)
	newfile.write("Esta declaración va desde la fecha:  ".encode())
	newfile.write(ANODECLARA_INI.encode())
	print("Hasta la fecha: ", ANODECLARA_FIN)
	newfile.write("hasta la fecha:  ".encode())
	newfile.write(ANODECLARA_FIN.encode())
	print("Resumen de monedas: ")
	newfile.write('\nResumen de monedas usadas: '.encode())
	newfile.write('\n\n'.encode())
	print(type_coins)
	newfile.write(str(type_coins).encode())
	newfile.write('\n\n'.encode())
	x = 0
	y = 0
	suma_sell = 0
	suma_buy = 0
	suma_fee = 0
	suma_withdraw = 0
	suma_commissionhistory = 0
	suma_distribution = 0
	suma_deposit = 0
	suma_small = 0
	tran_related = 0
	savings_p = 0
	savings_i = 0
	savings_predem = 0
	contador = 0
	datos_analizados = 0
	lineasdb = open ('check.log','wb')
	
	while contador < len_coin:	
		for x in range(num_files): # quitado -1 de num_files
			
			ROW0 = ((df.loc[x])['Operation'])
			ROW1 = ((df.loc[x])['Change'])
			ROW2 = ((df.loc[x])['Coin'])
			if ROW0 == "Sell" and ROW2 == type_coins[y]:
				suma_sell += ROW1
				lineasdb.write(f'{x+2}\n'.encode())
				datos_analizados += 1
			if ROW0 == "Buy" and ROW2 == type_coins[y]:
				suma_buy += ROW1
				lineasdb.write(f'{x+2}\n'.encode())
				datos_analizados += 1
			if ROW0 == "Fee" and ROW2 == type_coins[y]:
				suma_fee += ROW1
				lineasdb.write(f'{x+2}\n'.encode())
				datos_analizados += 1
			if ROW0 == "Withdraw" and ROW2 == type_coins[y]:
				suma_withdraw += ROW1
				lineasdb.write(f'{x+2}\n'.encode())
				datos_analizados += 1
			if ROW0 == "Commission History" and ROW2 == type_coins[y]:
				suma_commissionhistory += ROW1
				lineasdb.write(f'{x+2}\n'.encode())
				datos_analizados += 1
			if ROW0 == "Distribution" and ROW2 == type_coins[y]:
				suma_distribution += ROW1
				lineasdb.write(f'{x+2}\n'.encode())
				datos_analizados += 1
			if ROW0 == "Deposit" and ROW2 == type_coins[y]:
				suma_deposit += ROW1
				lineasdb.write(f'{x+2}\n'.encode())
				datos_analizados += 1
			if ROW0 == "Small assets exchange BNB" and ROW2 == type_coins[y]:
				suma_small += ROW1
				lineasdb.write(f'{x+2}\n'.encode())
				datos_analizados += 1
			if ROW0 == "Transaction Related" and ROW2 == type_coins[y]:
				tran_related += ROW1
				lineasdb.write(f'{x+2}\n'.encode())
				datos_analizados += 1
			if ROW0 == "Savings purchase" and ROW2 == type_coins[y]:
				savings_p += ROW1
				lineasdb.write(f'{x+2}\n'.encode())
				datos_analizados += 1
			if ROW0 == "Savings Interest" and ROW2 == type_coins[y]:
				savings_i += ROW1
				lineasdb.write(f'{x+2}\n'.encode())
				datos_analizados += 1
			if ROW0 == "Savings Principal redemption" and ROW2 == type_coins[y]:
				savings_predem += ROW1
				lineasdb.write(f'{x+2}\n'.encode())
				datos_analizados += 1
							
			x += 1
		resumen_del_ano = suma_buy + suma_deposit + suma_distribution + suma_withdraw + suma_commissionhistory + suma_small + tran_related + savings_p + savings_i + savings_predem + suma_fee + suma_sell
		print("El resumen del año es:", "BUY: ", suma_buy, "DEPOSIT: ", suma_deposit, "DISTRIBUTION: ", suma_distribution, "WITHDRAW: ", suma_withdraw, "COMISSIONS: ", suma_commissionhistory, "SMALL: ", suma_small, "TRAN: ", tran_related, "SAVINGS P: ", savings_p, "SAVINGS I: ", savings_i, "SAVINGS PRE: ", savings_predem, "FEE: ", suma_fee, "SELL: ", suma_sell)		
		newfile.write('Resumen del año en: '.encode())
		newfile.write(str(type_coins[y]).encode())
		newfile.write('\n'.encode())		
		newfile.write(f'{resumen_del_ano:9.8f}'.encode())
		newfile.write('\n\n'.encode())
		print(f'Total beneficio o perdida del año fiscal en la moneda {type_coins[y]} ha sido de: {resumen_del_ano:9.8f}')
		print(f'{resumen_del_ano:9.8f}') #imprime los 8 decimales tan preciados
		y += 1
		x = 0
		contador += 1
		suma_sell = 0
		suma_buy = 0
		suma_fee = 0
		suma_withdraw = 0
		suma_commissionhistory = 0
		suma_distribution = 0
		suma_deposit = 0
		suma_small = 0
		tran_related = 0
		savings_p = 0
		savings_i = 0
		savings_predem = 0
		if contador == len_coin:		
			newfile.write(f'Total de líneas en base de datos analizadas: {datos_analizados}'.encode())
			lineasdb.close()


def resumen_bitstamp():
	# CABECERA Y DECLARACIÓN DE VARIABLES
	os.system('clear')
	#newfile = open ('Bitstamp.txt','wb')
	#archivo = '/home/kali/Documents/DEK23_BTC/part-00000-8355b0ee-2b16-451d-b723-3f8c8757d819-c000.csv'
	global archivo
	newfile2.write(str(archivo).encode())
	df = pd.read_csv(archivo) # skiprows=1 es para no contar filas hay que poner la coma delante y espacio. sheet_name='Sheet1' para seleccionar la hoja. read_excel para leer bd
	num_files = df.shape[0]	

	
	ANODECLARA_INI = input ('Escribe la fecha de comienzo de la declaración (Ejemplo: 2018-04-04 20:19:34): ')
	ANODECLARA_FIN = input ('Escribe la fecha de final de la declaración (Ejemplo: 2018-04-04 20:19:34): ')
	type_coins = pd.unique(df['Amount'])
	len_coin = len(type_coins)
	print ("*******RESUMEN GLOBAL*******")
	newfile2.write('***********RESUMEN GLOBAL BITSTAMP********* '.encode())
	newfile2.write('\n\n'.encode())
	print("Esta declaración va desde ", ANODECLARA_INI, "hasta ", ANODECLARA_FIN)
	newfile2.write("Esta declaración va desde la fecha: ".encode())
	newfile2.write(ANODECLARA_INI.encode())
	print("Hasta la fecha: ", ANODECLARA_FIN)
	newfile2.write("hasta la fecha: ".encode())
	newfile2.write(ANODECLARA_FIN.encode())
	print("Resumen de monedas: ")
	newfile2.write('Resumen de monedas usadas: '.encode())
	newfile2.write('\n\n'.encode())
	print(type_coins)
	newfile2.write(str(type_coins).encode())
	newfile2.write('\n\n'.encode())
	x = 0
	y = 0
	suma_sell = 0
	suma_buy = 0
	suma_fee = 0
	suma_withdraw = 0
	suma_deposit = 0
	contador = 0
	
	while contador < len_coin:	
		for x in range(num_files-1):
			
			ROW0 = ((df.loc[x])['Type'])
			ROW1 = ((df.loc[x])['Amount'])
			ROW2 = ((df.loc[x])['Amount'])
			ROW3 = ((df.loc[x])['Sub Type'])
			ROW4 = ((df.loc[x])['Fee'])

			if ROW0 == "Market" and ROW3 == "Sell" and ROW2 == type_coins[y]:
				suma_sell += ROW1
				suma_fee += ROW4
			if ROW0 == "Market" and ROW3 == "Buy" and ROW2 == type_coins[y]:
				suma_buy += ROW1
				suma_fee += ROW4
			if ROW0 == "Withdrawal" and ROW2 == type_coins[y]:
				suma_withdraw += ROW1
				suma_fee += ROW4
			if ROW0 == "Deposit" and ROW2 == type_coins[y]:
				suma_deposit += ROW1
				suma_fee += ROW4
			x += 1
		resumen_del_ano = suma_deposit + suma_buy + suma_sell + suma_fee + suma_withdraw
		newfile2.write('Resumen del año en: '.encode())
		newfile2.write(str(type_coins[y]).encode())
		newfile2.write('\n'.encode())		
		newfile2.write(f'{resumen_del_ano:9.8f}'.encode())
		newfile2.write('\n\n'.encode())
		print(f'Total beneficio o perdida del año fiscal en la moneda {type_coins[y]} ha sido de: {resumen_del_ano:9.8f}')
		print(f'{resumen_del_ano:9.8f}') #imprime los 8 decimales tan preciados
		y += 1
		x = 0
		contador += 1
		suma_sell = 0
		suma_buy = 0
		suma_fee = 0
		suma_withdraw = 0
		suma_deposit = 0
		

# Argumentos en la terminal de Kali Linux

if len(sys.argv) == 1:
	print("No correct. Please use -h or --help.")
	sys.exit()	

if len(sys.argv) == (2, 3, 4):
	print("No correct. Remember:")
	print("-e binance file.csv (to choose the cryptoexchange or wallet and the file.csv where are the information.")
	print("-o output_file.txt (to choose the file.txt when all the information will be save.")
	sys.exit()


if len(sys.argv) == 6:
	
	if sys.argv[1] == "-e" or "--exchange":
		if sys.argv[2] == "binance":
			archivo = str(sys.argv[3])
			newfile = open (f'{sys.argv[5]}','wb')		
			resumen()
			newfile.close()
			checker()
			sys.exit()

	if sys.argv[1] == "-e" or "--exchange":
		if sys.argv[2] == "bitstamp":
			archivo = str(sys.argv[3])
			newfile2 = open (f'{sys.argv[5]}','wb')		
			resumen_bitstamp()
			newfile2.close()
			checker()
			sys.exit()

	else:
		print ("No correct. Please use -h or --help.)")
	
if sys.argv[1] == "-h" or "--help":
	print ("\n")
	print ("Usage: python3 DEK23_BTC_declaration.py [OPTION] [FILE]")
	print ("Concatenate FILE to standard output.")
	print ("\n")
	print ("-h, --help		This help menu")
	print ("-e, --exchange		Select the crypto exchange")
	print ("				binance") 
	print ("				bitstamp")
	print ("-o, --output		Name of file to save information")
	print ("Examples:")
	print ("	python3 DEK23_BTC_declaration.py -e binance file.csv -o output_file.txt")
	sys.exit()

		
		
 


