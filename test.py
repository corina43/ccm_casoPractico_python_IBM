import unittest
from main import generar_matriz_cuadrada, calcular_suma_filas_columnas

class TestMatriz(unittest.TestCase):
    def test_generar_matriz_cuadrada(self):
        matriz = generar_matriz_cuadrada(3)
        self.assertEqual(len(matriz), 3)  # Verifica que la matriz sea de tamaño 3x3

    def test_calcular_suma_filas_columnas(self):
        matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        sumas_filas, sumas_columnas = calcular_suma_filas_columnas(matriz)
        self.assertEqual(sumas_filas, [6, 15, 24])  # Verifica las sumas de las filas
        self.assertEqual(sumas_columnas, [12, 15, 18])  # Verifica las sumas de las columnas

if __name__ == '__main__':
    unittest.main()
