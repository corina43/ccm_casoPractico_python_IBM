# ccm_casoPractico_python_IBM
Generador de Matriz y Suma de Filas/Columnas

Este es un programa simple que genera una matriz cuadrada de tamaño N y calcula la suma de cada fila y columna de dicha matriz. La interfaz gráfica está desarrollada utilizando la biblioteca Tkinter de Python.

Instrucciones de uso:

Ejecuta el programa.
Ingresa un número entero positivo N en el cuadro de texto proporcionado.
Haz clic en el botón "Generar Matriz y Calcular Sumas".
Funcionamiento:

El programa generará una matriz cuadrada de tamaño N con valores aleatorios entre 0 y 9.
Mostrará la matriz generada en la interfaz gráfica.
Luego, calculará y mostrará la suma de cada fila y columna de la matriz generada.
Nota: Asegúrate de ingresar un número entero positivo en el cuadro de texto. Si se ingresa un valor no válido, se mostrará un mensaje de error.

Cómo funciona el código:

La función generar_matriz_cuadrada(tamano) crea una matriz cuadrada de tamaño tamano con valores aleatorios entre 0 y 9.
La función calcular_suma_filas_columnas(matriz) calcula las sumas de cada fila y columna de la matriz dada.
La función imprimir_matriz_en_interfaz(matriz) convierte la matriz en una cadena legible para mostrarla en la interfaz gráfica.
La función mostrar_resultados_interfaz(sumas_filas, sumas_columnas) muestra las sumas de cada fila y columna en una ventana emergente.
La función generar_matriz_y_calcular_sumas() se ejecuta cuando se hace clic en el botón "Generar Matriz y Calcular Sumas". Recupera el valor de N, genera la matriz, la muestra en la interfaz y calcula y muestra las sumas.
Requisitos del sistema:

Python 3.x instalado.
Biblioteca Tkinter incluida en la instalación estándar de Python.
Atención:

El programa puede generar matrices grandes, lo que puede ralentizar su ejecución en algunos casos.
Asegúrate de no cerrar la ventana antes de ver los resultados, ya que los resultados se muestran en ventanas emergentes.
Instrucciones para ejecutar el programa:

Asegúrate de tener Python 3.x instalado en tu sistema.
Ejecuta el archivo generador_matriz.py.
Se abrirá una ventana con un cuadro de texto para ingresar el valor de N.
Ingresa un número entero positivo en el cuadro de texto y haz clic en el botón "Generar Matriz y Calcular Sumas".
La matriz generada y las sumas de filas y columnas se mostrarán en la ventana emergente.
Notas adicionales:

Si deseas modificar el rango de valores aleatorios para la matriz, puedes hacerlo en la función generar_matriz_cuadrada(tamano) modificando los valores 0 y 9 en random.randint(0, 9).
Ten en cuenta que este programa tiene un propósito educativo y de demostración, y puede requerir ajustes adicionales para adaptarse a casos de uso más complejos.
¡Disfruta utilizando el Generador de Matriz y Suma de Filas/Columnas! Si tienes alguna pregunta o problema, no dudes en contactarnos.
