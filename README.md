# Sudoku
 Algoritmo para resolver cualquier Sudoku de cualquier dificultad en muy pocos segundos utilizando Backtracking y Algoritmo para generar miles de Sudokus distintos.

## Algoritmo para resolver Sudokus.
Resuelve cualquier Sudoku en Segundos utilizando Backtracking y el resultado lo almacena en un archivo de texto plano .zion (puedes abrirlo con cualquier editor de texto).

La salida se verá así:
```

By: LawlietJH.

Sudoku ==================================
+-------+-------+-------+
| 5 3 · | · 7 · | · · · | 
| 6 · · | 1 9 5 | · · · | 
| · 9 8 | · · · | · 6 · | 
+-------+-------+-------+
| 8 · · | · 6 · | · · 3 | 
| 4 · · | 8 · 3 | · · 1 | 
| 7 · · | · 2 · | · · 6 | 
+-------+-------+-------+
| · 6 1 | · · · | 2 8 · | 
| · · · | 4 1 9 | 6 3 5 | 
| · · · | · 8 · | · 7 9 | 
+-------+-------+-------+

Resuelto!
Nivel de Complejidad: Muy Fácil --> 1/5
Cambios Realizados: 1240
+-------+-------+-------+
| 5 3 4 | 6 7 8 | 9 1 2 | 
| 6 7 2 | 1 9 5 | 3 4 8 | 
| 1 9 8 | 3 4 2 | 5 6 7 | 
+-------+-------+-------+
| 8 5 9 | 7 6 1 | 4 2 3 | 
| 4 2 6 | 8 5 3 | 7 9 1 | 
| 7 1 3 | 9 2 4 | 8 5 6 | 
+-------+-------+-------+
| 9 6 1 | 5 3 7 | 2 8 4 | 
| 2 8 7 | 4 1 9 | 6 3 5 | 
| 3 4 5 | 2 8 6 | 1 7 9 | 
+-------+-------+-------+
=========================================

Sudoku ==================================
+-------+-------+-------+
| 1 · · | · · · | · 9 · | 
| 8 4 · | · · 2 | · · · | 
| · · · | 3 8 · | 2 · · | 
+-------+-------+-------+
| · · · | 9 · · | 8 5 3 | 
| · · · | · · · | · · · | 
| 5 3 8 | · · 6 | · · · | 
+-------+-------+-------+
| · · 1 | · 7 9 | · · · | 
| · · · | 5 · · | · 6 7 | 
| · 2 · | · · · | · · 9 | 
+-------+-------+-------+

Resuelto!
Nivel de Complejidad: Muy Dificil --> 5/5
Cambios Realizados: 27744
+-------+-------+-------+
| 1 6 2 | 7 5 4 | 3 9 8 | 
| 8 4 3 | 6 9 2 | 7 1 5 | 
| 9 5 7 | 3 8 1 | 2 4 6 | 
+-------+-------+-------+
| 2 1 6 | 9 4 7 | 8 5 3 | 
| 4 7 9 | 8 3 5 | 6 2 1 | 
| 5 3 8 | 2 1 6 | 9 7 4 | 
+-------+-------+-------+
| 6 8 1 | 4 7 9 | 5 3 2 | 
| 3 9 4 | 5 2 8 | 1 6 7 | 
| 7 2 5 | 1 6 3 | 4 8 9 | 
+-------+-------+-------+
=========================================
```

## Algoritmo para Generar Sudokus

Permite generar la cantidad que desees de sudokus, todos distintos y generados de forma aleatoria, si se detecta que un sudoku se repite, generara otro hasta que sea distinto, garantizando que todos los generados sean únicos y los almacenará todos en un archivo de salida .zion (puedes abrirlo con cualquier editor de texto).

Ejemplo de salida:

```
Sudoku: 1
+-------+-------+-------+
| 4 3 7 | 6 1 2 | 5 8 9 | 
| 6 1 2 | 5 8 9 | 4 3 7 | 
| 5 8 9 | 4 3 7 | 6 1 2 | 
+-------+-------+-------+
| 3 2 4 | 1 7 5 | 8 9 6 | 
| 1 7 5 | 8 9 6 | 3 2 4 | 
| 8 9 6 | 3 2 4 | 1 7 5 | 
+-------+-------+-------+
| 2 4 1 | 7 5 8 | 9 6 3 | 
| 7 5 8 | 9 6 3 | 2 4 1 | 
| 9 6 3 | 2 4 1 | 7 5 8 | 
+-------+-------+-------+

Sudoku: 2
+-------+-------+-------+
| 3 2 5 | 7 6 9 | 4 1 8 | 
| 7 6 9 | 4 1 8 | 3 2 5 | 
| 8 1 4 | 3 2 5 | 7 6 9 | 
+-------+-------+-------+
| 2 5 3 | 6 9 7 | 1 8 4 | 
| 6 9 7 | 1 8 4 | 2 5 3 | 
| 1 4 8 | 2 5 3 | 6 9 7 | 
+-------+-------+-------+
| 5 3 2 | 9 7 1 | 8 4 6 | 
| 9 7 1 | 8 4 6 | 5 3 2 | 
| 4 8 6 | 5 3 2 | 9 7 1 | 
+-------+-------+-------+

...

Sudoku: 30000
+-------+-------+-------+
| 5 9 3 | 8 1 2 | 4 7 6 | 
| 8 1 2 | 4 7 6 | 5 9 3 | 
| 4 7 6 | 5 9 3 | 8 1 2 | 
+-------+-------+-------+
| 9 6 5 | 1 2 4 | 7 3 8 | 
| 1 2 4 | 7 3 8 | 9 6 5 | 
| 7 3 8 | 9 6 5 | 1 2 4 | 
+-------+-------+-------+
| 2 5 1 | 3 4 7 | 6 8 9 | 
| 3 4 7 | 6 8 9 | 2 5 1 | 
| 6 8 9 | 2 5 1 | 3 4 7 | 
+-------+-------+-------+

etc...
```

## Variable Sudoku

La variable que contenga el Sudoku, debe ser una lista que contendra todo, y dentro de este una lista por cada fila, 9 en total y dentro de cada una de estas listas los 9 digitos correspondientes a la fila. Ejemplo:

```py
# Esta es la base para un Sudoku legible para cada función.
# Los 0 representan espacios vacios.

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
```

### Ejemplos de Uso:

Test de Solución de un Sudoku.
```py
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

print('\n\n Sudoku Por Resolver:')
print(printSudoku(sudoku))

resuelto, c = solveSudoku(sudoku)		# Resuelve el Sudoku.

if resuelto:
 
	backs = c[0]
	p_com = c[2]
	com   = c[1][p_com]
	print('Nivel de Complejidad: {} --> {}/5\nCambios Realizados: {}{}'.format(com, p_com+1, backs, printSudoku(resuelto)))
 
else: print('Esta Mal Hecho! No Tiene Solución.{}'.format(printSudoku(sudoku)))
```
Salida:
```
 Sudoku Por Resolver:

+-------+-------+-------+
| 1 · · | · · · | · 9 · |
| 8 4 · | · · 2 | · · · |
| · · · | 3 8 · | 2 · · |
+-------+-------+-------+
| · · · | 9 · · | 8 5 3 |
| · · · | · · · | · · · |
| 5 3 8 | · · 6 | · · · |
+-------+-------+-------+
| · · 1 | · 7 9 | · · · |
| · · · | 5 · · | · 6 7 |
| · 2 · | · · · | · · 9 |
+-------+-------+-------+

Nivel de Complejidad: Muy Dificil --> 5/5
Cambios Realizados: 27744
+-------+-------+-------+
| 1 6 2 | 7 5 4 | 3 9 8 |
| 8 4 3 | 6 9 2 | 7 1 5 |
| 9 5 7 | 3 8 1 | 2 4 6 |
+-------+-------+-------+
| 2 1 6 | 9 4 7 | 8 5 3 |
| 4 7 9 | 8 3 5 | 6 2 1 |
| 5 3 8 | 2 1 6 | 9 7 4 |
+-------+-------+-------+
| 6 8 1 | 4 7 9 | 5 3 2 |
| 3 9 4 | 5 2 8 | 1 6 7 |
| 7 2 5 | 1 6 3 | 4 8 9 |
+-------+-------+-------+
```

Para generar un Sudoku nuevo, generado de forma aleatoria, se utiliza la función:
```py
sudoku = getNewSudoku()
sudoku = printSudoku(sudoku)
print(sudoku)
```
Salida:
```
+-------+-------+-------+
| 8 1 4 | 3 6 2 | 7 5 9 |
| 3 6 2 | 7 5 9 | 8 1 4 |
| 7 5 9 | 8 1 4 | 3 6 2 |
+-------+-------+-------+
| 5 2 3 | 1 4 7 | 6 9 8 |
| 1 4 7 | 6 9 8 | 5 2 3 |
| 6 9 8 | 5 2 3 | 1 4 7 |
+-------+-------+-------+
| 2 3 1 | 4 8 5 | 9 7 6 |
| 4 8 5 | 9 7 6 | 2 3 1 |
| 9 7 6 | 2 3 1 | 4 8 5 |
+-------+-------+-------+
```

La función printSudoku devuelve una cadena con el sudoku en formato 0 (como se ve arriba).
Podemos hacer que se imprima en pantalla con formato de Lista, para reutilizar en el codigo copiando y pegandolo, indicandole a la función que el formato será el 1. De la siguiente manera:
```py
sudoku = getNewSudoku()
sudoku = printSudoku(sudoku, formato=1)
print(sudoku)
```
Salida:
```py
[8, 4, 9, 6, 1, 2, 3, 7, 5],
[2, 1, 6, 3, 7, 5, 8, 4, 9],
[3, 7, 5, 8, 4, 9, 2, 1, 6],
[1, 9, 3, 7, 2, 6, 4, 5, 8],
[7, 6, 2, 4, 5, 8, 1, 9, 3],
[4, 5, 8, 1, 9, 3, 7, 6, 2],
[5, 8, 4, 2, 6, 1, 9, 3, 7],
[6, 2, 1, 9, 3, 7, 5, 8, 4],
[9, 3, 7, 5, 8, 4, 6, 2, 1]
```

Si a esta función se le pasa un valor para X y Y le añadirá un asterisco para marcar dicha posición. Los valores para X y Y deben estar en el rango de 1 a 9 para evitar desbordar la matriz. De la siguiente manera:

```py
s = getNewSudoku()
sudoku  = printSudoku(s, XY=(2, 2))
sudoku2 = printSudoku(s, XY=(2, 2), formato=1)
print(sudoku)
print(sudoku2)
```
Salida:
```
+-------+-------+-------+
| 4 8 7 | 9 5 1 | 2 3 6 |
| 9 *5 1 | 2 3 6 | 4 8 7 |
| 2 3 6 | 4 8 7 | 9 5 1 |
+-------+-------+-------+
| 3 7 9 | 5 6 4 | 8 1 2 |
| 5 6 4 | 8 1 2 | 3 7 9 |
| 8 1 2 | 3 7 9 | 5 6 4 |
+-------+-------+-------+
| 7 9 3 | 1 2 8 | 6 4 5 |
| 1 2 8 | 6 4 5 | 7 9 3 |
| 6 4 5 | 7 9 3 | 1 2 8 |
+-------+-------+-------+

[4, 8, 7, 9, 5, 1, 2, 3, 6],
[9, *5, 1, 2, 3, 6, 4, 8, 7],
[2, 3, 6, 4, 8, 7, 9, 5, 1],
[3, 7, 9, 5, 6, 4, 8, 1, 2],
[5, 6, 4, 8, 1, 2, 3, 7, 9],
[8, 1, 2, 3, 7, 9, 5, 6, 4],
[7, 9, 3, 1, 2, 8, 6, 4, 5],
[1, 2, 8, 6, 4, 5, 7, 9, 3],
[6, 4, 5, 7, 9, 3, 1, 2, 8]
```

### Algoritmo para Validar Sudokus
Contiene una función que permite validar por completo un Sudoku y verificar que esté completamente correcto. Devuelve True o False.
Ejemplo:
```py
sudoku = [
 [4, 8, 7, 9, 5, 1, 2, 3, 6],
 [9, 5, 1, 2, 3, 6, 4, 8, 7],
 [2, 3, 6, 4, 8, 7, 9, 5, 1],
 [3, 7, 9, 5, 6, 4, 8, 1, 2],
 [5, 6, 4, 8, 1, 2, 3, 7, 9],
 [8, 1, 2, 3, 7, 9, 5, 6, 4],
 [7, 9, 3, 1, 2, 8, 6, 4, 5],
 [1, 2, 8, 6, 4, 5, 7, 9, 3],
 [6, 4, 5, 7, 9, 3, 1, 2, 8]
]
res = validateSolution(sudoku)
print(res)
```
Salida:
```
True
```

Si el Sudoku tiene una colisión o más, devolverá False, si le pasamos a la función como parametro degun=True, esta nos imprimirá en pantalla en donde ocurrió la primer colisión, veamos un ejemplo, utilizando el mismo sudoku anterior:

```py
sudoku = [
	 [4, 8, 7, 1, 5, 1, 2, 3, 6],  # Cambie el número 9 por 1 en esta fila.
	 [9, 5, 1, 2, 3, 6, 4, 8, 7],
	 [2, 3, 6, 4, 8, 7, 9, 5, 1],
	 [3, 7, 9, 5, 6, 4, 8, 1, 2],
	 [5, 6, 4, 8, 1, 2, 3, 7, 9],
	 [8, 1, 2, 3, 7, 9, 5, 6, 4],
	 [7, 9, 3, 1, 2, 8, 6, 4, 5],
	 [1, 2, 8, 6, 4, 5, 7, 9, 3],
	 [6, 4, 5, 7, 9, 3, 1, 2, 8]
	]
	res = validateSolution(sudoku, debug=True)
	print(res)
```
Salida:
```
Se repite el número 1 en la posición (4, 1)
False
```
Y así es, cambie el numero 9 que estaba en 4ta posición de la primera fila por un 1.

### Algoritmo para comparar 2 Sudokus
Contiene una función que permite comparar 2 Sudokus y verificar si son identicos.
Ademas este algoritmo permite utilizar un Sudoku incompleto y verificar con uno Completo si todos los numeros que tiene, coinciden en las mismas posiciones con el Completo, así, de esta forma, permite validar si un Sudoku por resolver pertenece a uno ya Resuelto o no y verificar los resultados de salida. Devolverá True si son semejantes o False si no lo son. Test de Ejemplo:

```py
# Original Resuelto
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

res = match(sudoku, match)
print(res)
```
Salida:
```
True
```

Tambien podremos hacer uso de la variable debug=True para esta función, Tomaremos los 2 sudokus de antes pero cambiaré 1 solo digito en el incompleto. Ejemplo:

```py
# Original Resuelto
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
	[2,0,0,8,0,3,0,0,1],  # Cambie el 4 en posición 1 de esta Fila por un 2.
	[7,0,0,0,2,0,0,0,6],
	[0,6,1,0,0,0,2,8,0],
	[0,0,0,4,1,9,6,3,5],
	[0,0,0,0,8,0,0,7,9]
]

res = match(sudoku, match, degub=True)
print(res)
```
Salida:
```
No coincide el número 2 en la posición (1, 5). Debería haber un 4 ahí.
False
```
