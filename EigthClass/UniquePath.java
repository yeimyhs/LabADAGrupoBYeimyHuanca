package EigthClass;
/*
##Ejercicio 1
# Un robot está ubicado en la esquina superior 
izquierda de una m x n cuadrícula Ahora considere 
si se agregan algunos obstáculos a las cuadrículas. 
¿Cuántos caminos únicos habría?
# Entrada: {{0,0,0},{0,1,0},{0,0,0}}
# Salida: 
            2     // caminos
            0100  // tecnica de caminos unicos , sumatoria del valor superior inmediato
            0111  // junto al izquierdo inmediato , 
            0101  // si hay presencia de obstaculo no se acumula camino en es cuadrante si hay presencia de obstaculo 
            0112  // no se acumula camino en ese cuadrante

# Autor:  Yeimy Huanca
*/
public class UniquePath {
    public static void main(String[] args) {
    	int [][] obstacleGrid = {{0,0,0},{0,1,0},{0,0,0}};
    	int m=obstacleGrid.length;//vertical
    	int n=obstacleGrid[0].length;//horizontal
    	int copia [][] = new int[m+1][n+1];
    	copia[0][1]=1;
    	
        for (int i = 1; i <= m; i++) {
        	for (int j = 1; j <= n; j++) {
        		if(obstacleGrid[i-1][j-1]!=1){
        			copia[i][j]=copia[i][j-1]+copia[i-1][j];
        		}else
        			copia[i][j]=0;
			}	
        	
		}
        //copia[m][n]=5;
		System.out.println(copia[m][n]);
		
		for (int x=0; x < copia.length; x++) {
			  for (int y=0; y < copia[x].length; y++) {
			    System.out.print(copia[x][y]);
			  }
			  System.out.println();
			}
        }
}
