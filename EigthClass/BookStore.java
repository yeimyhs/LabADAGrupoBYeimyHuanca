package EigthClass;
/*
##Ejercicio 2
# Estás en una librería que vende n diferentes libros. 
Sabes el precio y el número de páginas de cada libro.

Has decidido que el precio total de tus compras será como máximo X. 
¿Cuál es el número máximo de páginas que puede comprar? 
Puedes comprar cada libro como máximo una vez.
# Entrada: 
			4 10      // se usa el algoritmo de la mochila
			4 8 5 3
			5 12 8 1
# Salida: 
            13
# Autor:  Yeimy Huanca
*/
import java.util.*;
public class BookStore {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();//n libros
		int x = sc.nextInt();//x dinero disponible
		int[] h = new int[n];
		int[] s = new int[n + 1];

		for (int i = 0; i < n; i++) {
			h[i] = sc.nextInt();
		}
		for (int i = 0; i < n; i++) {
			s[i] = sc.nextInt();
		}

		int[][] data = new int[n + 1][x + 1];

		for (int i = 0; i < n; i++) {
			for (int j = 0; j <= x; j++) {
				data[i + 1][j] = data[i][j];
				if (j >= h[i]) {
					data[i + 1][j] = Math.max(data[i][j - h[i]]  + s[i], data[i + 1][j]);
				}
			}
		}

		System.out.println(data[n][x]);

		//int n = 0;
		//n = sc.nextInt(); //numero de piedras
		//int abc [] = new int[26];
		//int conc = 0;
		//ArrayList<String>num= new ArrayList<String>();
		//int ganadores = 0;
		//int probR=0;
		//String name= sc.next();
		//String piedra ="";
		//String sgt="";
		//int n=0;
		//piedra = name.substring(0,1);
		// System.out.println(Arrays.asList(paglib));
	}





}
