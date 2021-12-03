package EigthClass;
/*
##Ejercicio 5
# Dado un m x n binario 'matrix'
lleno de 0's y 1's, encuentre el cuadrado más grande que contenga solo 1's 
y devuelva su área .
# Entrada: 
	    // se usa el algoritmo de la mochila con variacion en las comparaciones
		{{1,0,1,0,0},{1,0,1,1,1},{1,1,1,1,1},{1,0,0,1,0}};	
# Salida: 
		4
# Autor:  Yeimy Huanca
*/
import java.util.*;
public class MaximalSquare {
	public static void main(String[] args) {
		int [][] matrix = {{1,0,1,0,0},{1,0,1,1,1},{1,1,1,1,1},{1,0,0,1,0}};
		int height=matrix.length;//
		int width=matrix[0].length;//
		int copia [][] = new int[height+1][width+1];

		int ans=0;


		for(int i=0; i<=height; i++){
			for(int u=0; u<=width; u++){
				if(i==0||u==0){
					copia[i][u]=0;
				}else if(matrix[i-1][u-1] != '0'){
					copia[i][u]=Math.min(copia[i-1][u-1],Math.min(copia[i-1][u],copia[i][u-1]))+1;
					ans=Math.max(ans,copia[i][u]);
				}else{
					copia[i][u]=0;
				}
			}
		}

		System.out.println(ans*ans);

		for (int x=0; x < copia.length; x++) {
			for (int y=0; y < copia[x].length; y++) {
				System.out.print(copia[x][y]);
			}
			System.out.println();
		}
	}





}
