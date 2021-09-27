
/*Este codigo presenta la 
 * ordenacion de un array por medio del 
 * metodo insertion sort
 * 
 * 20/09/21
 * Autor: Yeimy Huanca
 */

public class exercise3 {
	public static void main(String args[]){
		int arr[] = { 21,18,5,19,3};
		sort(arr);
		print(arr);	 
	}

	static void print(int arr[]) {
		for (int i = 0; i < arr.length; i++) {
			System.out.println(arr[i]);
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
}
