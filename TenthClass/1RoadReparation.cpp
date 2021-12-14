#include<iostream>
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
/*
##Ejercicio 1
# calcular el costo que nesesario , 
  para reparar del so caminos de cierto 
  numero de cuidades relacionadas

# Autor:  Yeimy Huanca
 */


struct Arista{
  int inicio;
  int llegada;
  ll peso;
};

const int maxM = 2e5;
vector<Arista> data;
int parnert[maxM];
// el arreglo de parnert se usa para saber que aristas ya estan relacionadas
int n, m;

bool comp(Arista a, Arista b){
// el metodo comparar es util para ordenar el vector
  return a.peso < b.peso;
}

int find (int i){
// mediante find encontraremos, al valor al que ya esta relacionado
  if(parnert[i] == -1){
    return i;
  }

  parnert[i] = find(parnert[i]);
  return parnert[i];
}


bool merge(int a, int b){
// merge relaciona a las cuidades
  a = find(a);
  b = find(b);
  if(a == b){
  // si se obtiene que ya estna relacionados con anterioridad
    return false; // entonces retornaremos false
  } 
  parnert[a] = b;
  // coso contrario , los relaiconamos y debolvemos true
  return true;
}


int main() {
  ll count = 0; 
  // cuenta la cantidad de peso usados
  int numsAristas = 0; 
  // cuenta la cantidad de aristas usadas
  cin >> n;
  cin >> m;

  for(int i = 0; i < n; i++) parnert[i] = -1;
  for(int i = 0; i < m; i++){
  // ingreso de la relacion delas cuidades, y sus pesos
    int a , b;
    ll c;
    cin >> a;
    cin >> b;
    cin >> c;
    data.push_back({a,b,c});
  }
  // ordenamientod del vector, para poder trabajarlo de mejor manera , haremos uso de comp ya que es la funcion mediante la que se ordena
  sort(data.begin(), data.end(), comp);
  
  // para cada aritsta haremos lo siguiente
  for(Arista a : data){
    if(merge(a.inicio, a.llegada)){ 
    // evaluamos que no esten conectadas 
      count += a.peso; 
      // agregamos su peso a count
      numsAristas++; 
      //y aumentaremos el valor de numsAristas
    }
  }

  // el objetivo de numsAristas, es ssaber si se uso un total de n-1 aristas, ya que esta en la cantidad requerida para que todos este 
  // conectados
  if(numsAristas == (n - 1)){
    cout << count;
  }
  // si no estan todas conectadas entonces devolveremos imposible
  else {
    cout << "IMPOSSIBLE";
  }

  return 0;
}