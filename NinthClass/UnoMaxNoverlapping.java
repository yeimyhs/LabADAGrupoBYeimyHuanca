package LaboratorioADA.NinthClass;
/*
##Ejercicio 1
# Encuentre un conjunto máximo de
 segmentos que no se superpongan.

# Entrada: { 1, 3, 7, 9, 9}
		   { 5, 6, 8, 9, 10}
# Salida: 
           3
# Autor:  Yeimy Huanca
*/
public class UnoMaxNoverlapping {
	
	public static void main(String[] args) {
		//caso de prueba
		int[] a = { 1, 3, 7, 9, 9};
		int[] b = { 5, 6, 8, 9, 10};
		System.out.println(findSegment(a, b));
		
	}
	
    public static int findSegment(int[] a, int[] b) {
    	int startPos = -1;
		// variable para la posicion incial, como se trata de
		// distancias se inicia en '-1'.		
    	int segmentAmount = 0;
		// variable para la cantidad de segmentos que puede tomar
		// sin superponer uno sobre otro. Se devolve al final
		
    	for(int i = 0; i < a.length; i++) {
		// itera sobre todos los segmentos del arreglo
    		if(a[i] > startPos) {
			// si la posicion inicial del segmento es mayor a
			// la posicion incial entonces no se superponen 
    			startPos = b[i];
				// actualiza el valor de la posicion actual al
				// valor de la posicion final del segmento en revision
    			segmentAmount++;
				// Aumenta la cantidad de segmentos 'correctos'
			}
		}
    	return segmentAmount;
		// Finalmente devolve la cantidad de segmentos 'correctos'
	}
	
}
