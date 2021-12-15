#include <bits/stdc++.h>
/*
##Ejercicio 4 
# Uolevi ha ganado un concurso, y el premio es un vuelo gratuito 
  que puede consistir en uno o más vuelos por ciudades. Uolevi
  quiere volar de Syrjälä a Lehmälä para visitar el número máximo de ciudades. 
  Se le da la lista de vuelos posibles y sabe que no hay ciclos dirigidos en 
  la red de vuelos.

  Uso del algoritmo DFS
# Autor:  Yeimy Huanca
 */

#define int long long
#define MOD 1000000007
#define MAX 1e13
 
using namespace std;

vector<int> G[100005];
int n, m;
//n ciudades y m vuelos
bool visitado[100005];
//arreglo booleano, verifica si un vertice fue visitado anteriomente
int par[100005] = {-1};

void dfs(int root, vector<int>& path) {
    //camino mas largo dentro del Grafo
    visitado[root] = true;
    // Revisa que el hijo no haya sido visitado
    for(int i = 0; i < G[root].size(); i++) {
        //Para los Vertices que nacen de root
        if(!visitado[G[root][i]]) {
            //itera mientras que sean diferentes al padre
            dfs(G[root][i], path);
        }
    }
    path.push_back(root);
    //Vertice no ha sido visitado
}

void print_parent(int root) {
    if(root == -1) {
        return;
    }
    print_parent(par[root]);
    cout << root + 1 << " ";
}
 
void dijkstra() {
    cin >> n >> m;
    for(int i = 0; i < m; i++) {
        int x, y; 
        cin >> x >> y;
        x--; y--;
        G[x].push_back(y);
        // Agrega las Arista desde el Origen hasta el Destino
    }
    memset(visitado, false, sizeof(visitado));
    

    vector<int> nodes;
    dfs(0, nodes);
    //Se revisa el arreglo para los Vertices ya visitados 
    if(!visitado[n - 1]) {
        //si el Vertice 'n' no ha sido visitado
        cout << "IMPOSSIBLE" << endl;
        //no existe una ruta
        return;
    }
    reverse(nodes.begin(), nodes.end());
    //se guarda la respuesta en orden inverso
    int dist[n];
    for(int i = 0; i < n; i++) {
        dist[i] = 1;
    }
    
    for(int i = 0; i < nodes.size(); i++) {
        //iterar sobre las rutas 
        for(int j = 0; j < G[nodes[i]].size(); j++) {
            //se almacena en el arreglo auxiliar dist
            if (dist[G[nodes[i]][j]] < dist[nodes[i]] + 1) {
                dist[G[nodes[i]][j]] = dist[nodes[i]] + 1;
                par[G[nodes[i]][j]] = nodes[i];
            }
        }
    }
    cout << dist[n - 1] << endl;
    print_parent(n - 1);
}

int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    dijkstra();//retorna el número máximo de ciudades
    return 0;
}