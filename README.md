# Pac-Man

## 1. Comprensión Del Problema

---
Al este ejercicio le obtiene los siguientes datos importantes:

* Si se encuentra con un fanstasma la comida es robada, es decir se pierde el conteo.
* Los fantasmas **no** se mueven.
* PacMan recorre el siguiente camino:
    1. Comienza en la esquina superior izquierda.
    2. Recorre de izquierda a derecha hasta el otro lado.
    3. baja de la posición donde se encuentra y recorre de derecha a izquierda.
    4. Los pasos *2* y *3* se repiten hasta recorrer todo el tablero.
* Hay que determinar la mayor cantidad de comida que se puede llevar.
* El tablero del juego esta contruido por $2<=n<=100$ donde $n$ es el primer input que se obtiene del programa determinando el tamaño del tablero.
* Dentro de ese tablero ***unicamente*** pueden estar los siguientes caracteres:
  * '.' Espacio vacio.
  * 'o' Comida.
  * 'A' Fantasma.
* No pueden haber fantasmas ni comida en la misma posición.
* No hay fantasmas ni comida en la posición inicial, es decir solo puede haber un **espacio vacio** ('.').
* El output debe de ser un unico número entero que significa la cantidad maxima de comida que se puede llevar a casa.

## 2. Definición de la estructura del problema

---
El ejercicio se divide en las siguientes partes:

1. La construcción del tablero a partir de la entrada que nos da el jugador, teniendo en cuenta que es una entrada limitada de 2 a 100.
2. Una vez se defina bien el número de filas y de columnas, es decir $n.n$, se debe ingresar estas medidas usando una matriz para simular el tablero de juego.
3. La lógica del problema nos dice que el jugador debe de ingresar las entradas en formato de $n$ filas, las cuales se guardaran en una variable que contendra dicha cadena de texto, siempre verificando que la longitud de la cadena sea igual a $n$ y ademas cumpla con los unicos 3 caracteres que se pueden ingresar, si no, no se deberá permitir continuar con el juego ni se guardaran estas cadenas en la matriz.
4. Una vez llega a la última inserción correcta de la cadena de texto se procede a hacer el recorrido en la matriz empezando por la parte izquierda, para este punto desarrolle la siguiente lógica: Si esta en una fila impar, recorrerá de izquierda derecha, de lo contrario recorrerá de derecha a izquierda. Mientras recorre y hasta que llegue a un fantasma o hasta el fin del tablero tendrá que guardar el mayor número de comida recogida antes de toparse con un fantasma y luego mostrar el mejor resultado.

## 3. Programación del problema

---
Para la programación del ejercicio se uso el lenguaje de programación *python* en su versión *3.9.4*.  
Para ver su solución ingresa [aqui](https://github.com/devBorisG/Complejidad_Algoritmos/blob/main/Ejercicios/PacMan/main.py).

## 4. Recursos consumidos

---
El tiempo de ejecución del programa mostrado en la plataforma *beecrowd* es de 0.022 segundos. Otra forma de poder evidenciar el tiempo es con la libreria de python *time*. Este programa tiene un peso de 3.03 KB

## 5. Tiempo invertido

---
El tiempo aproximado para la realización del código es de ***cuatro horas y media***.
