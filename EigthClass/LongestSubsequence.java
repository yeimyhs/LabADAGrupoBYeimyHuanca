package EigthClass;
/*
##Ejercicio 3
# Dada una matriz de enteros nums, 
devuelve la longitud de la subsecuencia 
estrictamente creciente más larga.

Una subsecuencia es una secuencia 
que se puede derivar de una matriz 
eliminando algunos o ningún elemento 
sin cambiar el orden de los elementos restantes.
Alg
# Entrada: {10,9,2,5,3,7,101,18}
# Salida: 
           4
# Autor:  Yeimy Huanca
*/
import java.util.*;
public class LongestSubsequence {
    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//
		int nums[] = {10,9,2,5,3,7,101,18};
		int n = nums.length;

		int [] cant = new int [n];

		Arrays.fill(cant, 1);
		int max = 1;
		for (int i = 1; i < n; i++) {
			for (int j = 0; j < i; j++) {
				if (nums[i] > nums[j]) {
					cant[i] = Math.max(cant[i], cant[j] + 1);
				}
			}
			max = Math.max(max, cant[i]);
		}
		//return max
		System.out.println(max);
	}
}
