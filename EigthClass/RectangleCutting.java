package EigthClass;
/*
##Ejercicio 4
# Dado un a × b rectángulo, su tarea es cortarlo en cuadrados. 
En cada movimiento, puede seleccionar un rectángulo 
y cortarlo en dos rectángulos de tal manera que 
todas las longitudes de los lados sigan siendo números enteros. 
¿Cuál es el número mínimo posible de movimientos?
# Entrada: 3 5
# Salida: 
           3
# Autor:  Yeimy Huanca
*/
import java.util.*;
public class RectangleCutting {
    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int[][] data = new int[a+1][b+1];

		for (int height = 1; height < a + 1; height++) {
			for (int width = 1; width < b + 1; width++) {
				if (height == width) {
					data[height][width] = 0;
				} else {
					int ans = Integer.MAX_VALUE;
					//minimizando para : corte(x)+corte(u-x) -> cortes horizontales
					for (int i = 1; i < width; i++) {
						ans = Math.min(ans, 1 + data[height][width - i] + data[height][i]);
					}
					//minimizando para : corte(y)+corte(i-y) -> cortes verticales
					for (int i = 1; i < height; i++) {
						ans = Math.min(ans, 1 + data[height - i][width] + data[i][width]);
					}

					data[height][width] = ans;//se toma la menor opcion de las sumas

				}

			}

		}
		System.out.println(data[a][b]);
	}
}
