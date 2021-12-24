
/*
##Ejercicio 4
# Un borde de una cadena es un prefijo que también es 
# un sufijo de la cadena pero no la cadena completa '
# cadena. Por ejemplo, los bordes de abcababcab son ab 
# y abcab.
# 
# Entrada:
#                     Casos de prueba planteados  
# Autor:  Yeimy Huanca


#Casos de prueba (copiar en consola)
'''
abcababcab

'''

#outputs
'''
2 5
'''
*/
#include <stdio.h>
#include <string.h>

#define N 1000000

int main()
{
  static char cc[N + 1];
  static int zz[N];
  // arreglo de longitudes de bordes
  int n, i, izquierda, derecha;                         
  // n = longitud de cadena, i = indice, izquierda = indice izquierdo, derecha = indice derecho 

  scanf("%s", cc);       
  // ingreso cadena
  n = strlen(cc);  
  // longitud de cadena
  for (i = 1, izquierda = derecha = 0; i < n; i++)      
  // recorrido de cadena
    if (zz[i - izquierda] < derecha - i)           
    // si el borde es menor que el borde derecho - indice 
      zz[i] = zz[i - izquierda];
      // entonces se copia el borde izquierdo 
    else                              
    {     
      izquierda = i; 
      if (derecha < izquierda)  
        derecha = izquierda; 
        // se actualiza el borde derecho 
      while (derecha < n && cc[derecha] == cc[derecha - izquierda]) 
      // se busca el borde derecho 
        derecha++; 
      zz[i] = derecha - izquierda;                      
      // se actualiza el borde 
    }
  for (i = n - 1; i > 0; i--)             
  // recorrido de cadena inversa 
    if (zz[i] == n - i)                   
    // si el borde es igual a la longitud de la cadena - indice 
      printf("%d ", n - i);               
      // entonces se imprime la longitud del borde 
  printf("\n");                           
  // salto de linea 
  return 0;
}