package LaboratorioADA.NinthClass;
/*
##Ejercicio 1
# Se nos entrega un arreglo estandar de enteros que representan
  las diferentes longitudes de pedazos de cuerda. Estos pedazos
  de cuerda pueden ser unidos en caso de ser adyacente (uno al
  lado del otro). Tambien se nos entrega un numero 'k' el cual
  es la longitud 'minima' que se quiere obtener al amarrar todos
  los pedazos de cuerda.

# Entrada: { 1, 2, 3, 4, 1, 1, 3 }
# Salida: 
           3
# Autor:  Yeimy Huanca
 */
public class DosTiedRopes {

	public static void main(String[] args) {
		//caso de prueba
		int[] a = { 1, 2, 3, 4, 1, 1, 3 };
		System.out.println(ropesAmount(4, a));

	}

	public static int ropesAmount(int k, int[] a) {
		int tiedRopes = 0;
		// cantidad de cuerdas amarradas que seran aceptadas con respecto a 'k'
		int currentLength = 0;
		// guarda la longitud de la cuerda amarrada actual
		for(int i = 0; i < a.length; i++) {
			currentLength += a[i];
			// Agrega la longitud de la cuerda actual
			if(currentLength >= k) {
			// Si la longitud es mayor o igual al valor de 'k'
				currentLength = 0;
				// Reinicia la variable auxiliar
				tiedRopes++;
				// Agrega una cuerda que cumple la condicion
			}
		}
		return tiedRopes;

	}

}


