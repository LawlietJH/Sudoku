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

### Algoritmo para Validar Sudokus
Contiene una función que permite validar por completo un Sudoku y verificar que esté completamente correcto.

### Algoritmo para comparar 2 Sudokus
Contiene una función que permite comparar 2 Sudokus y verificar si son identicos.
Ademas este algoritmo permite utilizar un Sudoku incompleto y verificar con uno Terminado, si todos los numeros que tiene el incmpleto coinciden en la misma posición que el Completo, de esta forma, permite validar si un Sudoku por resolver pertenece a uno ya Resuelto y verificar los resultados de salida.
