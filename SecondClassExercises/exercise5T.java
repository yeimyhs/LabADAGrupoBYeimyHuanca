
/*Este codigo presenta la 
 * ordenacion de un array por medio del 
 * metodo insertion sort(adpatacion para tomar el tiempo)
 * 
 * Autor: Yeimy Huanca
 */

import java.util.*;
public class exercise5T {
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		System.out.print("length:");
		int length = sc.nextInt();
		int arr[] = createList(length);
		double tik = System.currentTimeMillis();
		sort(arr);
		double tak = System.currentTimeMillis();
		print(arr);
		System.out.println("\ntime of execute: "+ (tak - tik)%0.4f+" seconds");
	}

	static void print(int arr[]) {
		for (int i = 0; i < arr.length; i++) {
			System.out.print(arr[i]+" ");
		}
	}
	static void sort(int arr[]){
		int j, key, i;
		for (j = 1; j < arr.length; j++){
			key = arr[j];
			i = j - 1;

			while (i >= 0 && arr[i] > key){
				arr[i + 1] = arr[i];
				i = i - 1;
			}
			arr[i + 1] = key;
		}
	}
	static int[] createList(int n) {
		
		int[] arr = new int[n];
		for (int i = 0; i < arr.length; i++) {
			arr[i] = (int)(Math.random()*900);
		}
		return arr;
		
	}
}
