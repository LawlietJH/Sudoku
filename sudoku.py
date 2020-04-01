
# Sudoku!
# By: LawlietJH
# v1.1.0

import random
import time
import os

__title__   = 'Sudoku'				# Nombre de Script
__version__ = 'v1.1.0'				# Version
__author__  = 'LawlietJH'			# Desarrollador

#=======================================================================
#=======================================================================
#=======================================================================

pause = lambda hidden=False: os.system('Pause' if not hidden else 'Pause > Nul')	# Hace una Pausa en consola.
cls = lambda: os.system('cls')													# Limpia pantalla. Windows
rnd = lambda: random.randint(1, 9)												# Genera un numero random del 1 al 9.

#=======================================================================

# Base para hacer Sudokus que pueda leer el programa.
'''
sudoku = [
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0]
]
'''

#=======================================================================
#=======================================================================
#=======================================================================

# Mostrar un Sudoku
def printSudoku(sudoku, XY=(-1, -1), formato=0):
	
	if not (type(sudoku) == list and len(sudoku) == 9):
		raise TypeError(
			'Los Parametros del Sudoku estan Mal\n'+''.join([str(_)+'\n' for _ in sudoku])
		)
	
	if not type(XY) in [list, tuple]: raise TypeError('Debes pasar [X, Y] o (X, Y) como un solo parametro.')
	X = XY[0]
	Y = XY[1]
	if X == 0 or Y == 0: raise TypeError('X y Y deben ser mayor a 0. Del 1 al 9.')
	if X  > 9 or Y  > 9: raise TypeError('X y Y deben ser menor a 10. Del 1 al 9.')
	X, Y = X-1, Y-1
	
	salida = str(sudoku)
	
	if formato == 1:
		
		salida = '\n'
		for j in range(9):
			salida += '['
			for i in range(9):
				if j == Y and i == X: salida += '*'
				if i == 8: salida += str(sudoku[j][i])
				else: salida += str(sudoku[j][i]) + ', '
			if j == 8: salida += ']\n'
			else: salida += '],\n'
	
	elif formato == 0:
		
		salida = '\n'
		for j in range(9):
			if j%3 == 0:
				salida += '+' + ('-'*7 + '+')*3 + '\n'
			for i in range(9):
				if i == 0: salida += '| '
				if j == Y and i == X: salida += '*'
				salida += str(sudoku[j][i]) + ' '
				if (i+1)%3 == 0: salida += '| '
			
			salida += '\n'
		salida += '+' + ('-'*7 + '+')*3 + '\n'
		salida = salida.replace('0','·')
	
	return salida


# Valida que el Sudoku sea Correcto.
def validateSolution(sudoku, debug=False):
	
	for y in range(9):
		for x in range(9):
			
			cuad  = []
			lineX = []
			lineY = []
			cuadX = (x//3)*3
			cuadY = (y//3)*3
			
			for j in range(cuadY, cuadY+3):
				for i in range(cuadX, cuadX+3):
					if j == y and i == x: continue
					cuad.append(sudoku[j][i])
			
			for n in range(9):
				if n == x: continue
				lineX.append(sudoku[y][n])
			for n in range(9):
				if n == y: continue
				lineY.append(sudoku[n][x])
			
			if (sudoku[y][x] in cuad) \
			or (sudoku[y][x] in lineX)\
			or (sudoku[y][x] in lineY):
				
				if debug:
					s  = 'Se repite el número '+str(sudoku[y][x])
					s += ' en la posición ('+str(x+1)+', '+str(y+1)+')'
					print(s)
				
				return False
	
	# ~ print('Es Correcto!')
	return True


# Validar que un sudoku incompleto, pertenesca a uno completo.
# Tambien valida que dos sudokus sean identicos.
def match(sudoku, match, debug=False):
	for y in range(9):
		for x in range(9):
			if sudoku[y][x] == 0: continue
			if not sudoku[y][x] == match[y][x]:
				# ~ if debug: print(x+1, y+1)
				
				if debug:
					s  = 'No coincide el número '+str(sudoku[y][x])
					s += ' en la posición ('+str(x+1)+', '+str(y+1)+'). '
					s += 'Debería haber un '+str(match[y][x])+' ahí.'
					print(s)
				
				return False
	return True


# Busca la primera colision existente en el sudoku.
def colition(sudokus, sudokus_len):
	
	print('\n Repetidos:\n\n')
	
	val2 = 0
	for x in range(sudokus_len):
		for y in range(sudokus_len):
			if not x == y:
				if sudokus[x] == sudokus[y]:
					print(printSudoku(sudokus[x]))
					print('Pos: '+str(x+1))
			
			'''
			val1 = val2
			tot = sudokus_len**2
			cant = (x*sudokus_len)+y+1
			val2 = int((cant/tot)*100)
			if val1+1 == val2:
				cls()
				print('\n\n Generados: 100%')
				print('\n Repetidos:\n\n')
				print('\n\n Analizados: '+str(val2)+'%')
			'''


# Devuelve una estimacion de dificultad de un Sudoku en base a su numero de retrocesos con backtracking.
def getDifficulty(c):
	
	# Valida el nivel de complejidad, segun la cantidad de veces que se hizo un retroceso.
	p_com = 0
	if c >=  5000 and c < 10000: p_com = 1
	if c >= 10000 and c < 20000: p_com = 2
	if c >= 20000 and c < 25000: p_com = 3
	if c >= 25000: p_com = 4
	com = ['Muy Fácil', 'Fácil', 'Normal', 'Dificil', 'Muy Dificil']
	
	return [c, com, p_com]


# Test Resolviendo un Sudoku Dando uno completo y uno sin completar Basado en el Completo.  
def test(sudoku, solve):
	
	print('\nOriginal Solucionado.')
	v = validateSolution(solve)
	print('Esta Bien Heho:', v, printSudoku(solve))
	print('Original Sin Resolver. Basado en el Original.')
	m = match(sudoku, solve)
	print('Esta Bien Heho:', m, printSudoku(sudoku))
	
	if not (v and m):
		print('Error! El Sudoku a Resolver No es basado en el Original Solucionado.')
		return
	
	print('\nBacktracking ============================================\n')
	
	sudoku_new, c = solveSudoku(sudoku)
	
	if sudoku_new:
		
		backs = c[0]
		p_com = c[2]
		com   = c[1][p_com]
		
		res = validateSolution(sudoku_new)
		
		if res:
			print('Es Identico al Original: {}\nEsta Bien Hecho!'.format(match(sudoku_new, solve, True)))
			print('Nivel de Complejidad: {} --> {}/5\nCambios Realizados: {}{}'.format(com, p_com+1, backs, printSudoku(sudoku_new)))
		else:
			print('No se pudo solucionar Correctamente!\nNivel de Complejidad: "{}" --> {}/5\nCambios Realizados: {}{}'.format(com, p_com+1, backs, printSudoku(sudoku_new)))
		
	else:
		print('Esta Mal Hecho! No Tiene Solución.{}'.format(printSudoku(sudoku)))


#=======================================================================
#=======================================================================
#=======================================================================


# Crear un Sudoku
def getNewSudoku(xx=9, yy=9):
	
	if type(xx) == float: xx = int(xx)
	if type(yy) == float: yy = int(yy)
	
	if not type(xx) == int: raise TypeError('Debes Indicar Un Entero entre 1 y 9')
	if not type(yy) == int: raise TypeError('Debes Indicar Un Entero entre 1 y 9')
	
	if xx < 1 or xx > 9: xx = 9
	if yy < 1 or yy > 9: yy = 9
	
	sudoku = [
		[1, 2, 3, 4, 5, 6, 7, 8, 9],
		[4, 5, 6, 7, 8, 9, 1, 2, 3],
		[7, 8, 9, 1, 2, 3, 4, 5, 6],
		[2, 3, 4, 5, 6, 7, 8, 9, 1],
		[5, 6, 7, 8, 9, 1, 2, 3, 4],
		[8, 9, 1, 2, 3, 4, 5, 6, 7],
		[3, 4, 5, 6, 7, 8, 9, 1, 2],
		[6, 7, 8, 9, 1, 2, 3, 4, 5],
		[9, 1, 2, 3, 4, 5, 6, 7, 8]
	]
	
	for y in range(yy):
		for x in range(xx):
			
			posX = x
			posY = y
			
			r = rnd()
			o = sudoku[y][x]			# Original
			while o == r: r = rnd()
			sudoku[y][x] = r			# Nuevo
			
			while True:
				
				c = validateSolution(sudoku)
				
				if c: break
				
				for i in range(9):
					if i == posX: continue
					if sudoku[posY][i] == r:
						sudoku[posY][i] = o
						posX = i
						break
				
				for i in range(9):
					if i == posY: continue
					if sudoku[i][posX] == o:
						sudoku[i][posX] = r
						posY = i
						break
	
	return sudoku


# Resolver Un Sudoku. Utilizando Backtracking.
def solveSudoku(sudoku):
	
	s = [[x for x in y] for y in sudoku]	# Generamos una completa copia del sudoku.
	p = []				# Pila
	posX = 0			# Puntero en posicion X de la matriz
	posY = 0			# Puntero en posicion Y de la matriz
	n = 0				# Numero para probar en casilla vacia.
	back = False		# Indica si hubo un retroceso.
	cont = 0			# Contador de Retrocesos, para medir la complejidad del Sudoku al terminar.
	
	while True:
		
		if back:
			
			cont += 1
			val = None
			
			try: val = p.pop()
			except: return False, getDifficulty(cont)
			
			posX = val[0]
			posY = val[1]
			n = s[posY][posX]
			s[posY][posX] = 0
			
		else: n = 0
		
		if s[posY][posX] == 0 or back:
			
			back = False
			
			while True:
				
				cuad  = []
				lineX = []
				lineY = []
				n += 1
				
				if n == 10: back = True; break
				
				for j in range((posY//3)*3, ((posY//3)*3)+3):
					for i in range((posX//3)*3, ((posX//3)*3)+3):
						cuad.append(s[j][i])
				for _ in range(9): lineX.append(s[posY][_])
				for _ in range(9): lineY.append(s[_][posX])
				
				v = s[posY][posX]
				exists = list(set(cuad + lineX + lineY))				# Obtiene los numeros existentes en todas las listas, pero sin repetir ninguno.
				
				if not n in exists: break								# Si n no esta en la lista, continua la ejecución normal.
				
			if not back:
				p.append([posX, posY, n])
				s[posY][posX] = n
			else:
				# Retroceso de Casillas
				continue
		
		if not back:					# Si no debe haber retroceso
			# Avance de casilla
			posX += 1
			if posX == 9:
				posX = 0
				posY += 1
				if posY == 9:
					break
	
	
	# Devuelve el Sudoku y una lista con los valores de:
	# cantidad de retrocesos, lista de dificultades y numero de dificultad.
	return s, getDifficulty(cont)


#=======================================================================
#=======================================================================
#=======================================================================


if __name__ == '__main__':
	
	# Test, cambiar a True para ver.
	# Cambiar a True para ver o False para no verlo.
	if False:
		
		# De Prueba: Original Resuelto
		resuelto = [
			[5,3,4,6,7,8,9,1,2],
			[6,7,2,1,9,5,3,4,8],
			[1,9,8,3,4,2,5,6,7],
			[8,5,9,7,6,1,4,2,3],
			[4,2,6,8,5,3,7,9,1],
			[7,1,3,9,2,4,8,5,6],
			[9,6,1,5,3,7,2,8,4],
			[2,8,7,4,1,9,6,3,5],
			[3,4,5,2,8,6,1,7,9]
		]
		
		# Original Incompleto. Basado en el Original Resuelto.
		sudoku = [
			[5,3,0,0,7,0,0,0,0],
			[6,0,0,1,9,5,0,0,0],
			[0,9,8,0,0,0,0,6,0],
			[8,0,0,0,6,0,0,0,3],
			[4,0,0,8,0,3,0,0,1],
			[7,0,0,0,2,0,0,0,6],
			[0,6,1,0,0,0,2,8,0],
			[0,0,0,4,1,9,6,3,5],
			[0,0,0,0,8,0,0,7,9]
		]
		
		test(sudoku, resuelto)
		print('\n\n')
		pause()
	
	#===================================================================
	
	# Genera 100 Sudokus distintos en un archivo.
	# Puedes generar cuantos quieras, solo debes cambiar el numero en la variable amount
	# Cambiar a True para ver o False para no verlo.
	if True:
		
		amount = 100
		sudokus = []
		cont = 0
		v = 0
		sudo_file = 'sudokus.zion'
		temp = open(sudo_file, 'w'); temp.close()		# Crea un archivo en Blanco, borra el anterior si ya existe.
		sudo = open(sudo_file, 'a')
		
		sudo.write('\n'+'-'*52)
		sudo.write('\n| By: LawlietJH.                                   |\n')
		sudo.write('|                                                  |\n')
		sudo.write('| No se repite ningún Sudoku, Todos son distintos. |\n')
		sudo.write('-'*52+'\n')
		print('\n\n Sudokus Generados: 0%')
		
		for i in range(amount):
			
			v = ((i+1)/amount)*100
			if i % 17 == 0: cls(); print('\n\n Sudokus Generados: '+str(round(v, 2))+'%')
			
			s = getNewSudoku(rnd(), rnd())
			
			# Si sale uno repetido, se generara otro hasta que no este repetido.
			while s in sudokus: s = getNewSudoku(rnd(), rnd())			# Genera un nuevo Sudoku.
			
			sudokus.append(s)
			
			sudo.write('\nSudoku: '+str(i+1))
			sudo.write(printSudoku(s))
		
		cls()
		print('\n\n Sudokus Generados: '+str(amount))
		print('\n En el archivo: '+sudo_file, '\n\n')
		sudo.close()
		pause()
	
	#===================================================================
	
	# Resuelve un Sudoku Dado y lo almacena en un archivo.
	# Cambiar a True para ver o False para no verlo.
	if True:
		
		# Sudoku de alta complejidad.
		# Este es el de prueba que sera resuelto.
		sudoku  = [
			[1,0,0,0,0,0,0,9,0],
			[8,4,0,0,0,2,0,0,0],
			[0,0,0,3,8,0,2,0,0],
			[0,0,0,9,0,0,8,5,3],
			[0,0,0,0,0,0,0,0,0],
			[5,3,8,0,0,6,0,0,0],
			[0,0,1,0,7,9,0,0,0],
			[0,0,0,5,0,0,0,6,7],
			[0,2,0,0,0,0,0,0,9],
		]
		
		sudo_file = 'sudokus-resueltos.zion'
		if not os.path.exists(sudo_file):
			sudo = open(sudo_file, 'w')				# Crea un archivo en Blanco, borra el anterior si ya existe.
			sudo.write('\nBy: LawlietJH.\n\n')
			sudo.close()
		
		sudo = open(sudo_file, 'a')
		sudo.write('\nSudoku '+'='*34)
		sudo.write(printSudoku(sudoku))
		
		cls()
		print('\n\n Sudoku Por Resolver:')
		print(printSudoku(sudoku))
		
		resuelto, c = solveSudoku(sudoku)		# Resuelve el Sudoku.
		
		if resuelto:
			
			backs = c[0]
			p_com = c[2]
			com   = c[1][p_com]
			
			res = validateSolution(resuelto)
			
			if res:
				
				sudo.write('\nResuelto!')
				sudo.write('\nNivel de Complejidad: {} --> {}/5'.format(com, p_com+1))
				sudo.write('\nCambios Realizados: {}'.format(backs))
				sudo.write(printSudoku(resuelto))
				print('Nivel de Complejidad: {} --> {}/5\nCambios Realizados: {}{}'.format(com, p_com+1, backs, printSudoku(resuelto)))
				
			else:
				
				sudo.write('\nNo se pudo solucionar Correctamente!\n')
				print('No se pudo solucionar Correctamente!\nNivel de Complejidad: "{}" --> {}/5\nCambios Realizados: {}{}'.format(com, p_com+1, backs, printSudoku(resuelto)))
		else:
			
			sudo.write('\nEsta Mal Hecho! No Tiene Solución.\n')
			print('Esta Mal Hecho! No Tiene Solución.{}'.format(printSudoku(sudoku)))
		
		sudo.write('='*41 + '\n')
		sudo.close()
		
		print('\n\n')
		
		pause()
	
	#===================================================================
	
