##Version Iterativo
# el siguiente codigo recrea la funcio iterativa de el pseudocoddigo brindado en clase
# DFS
# Entrada:
# -                   (ejemplo ya propuesto)
# Salida:
'''
Insertar  ↓ a
Visitando nodo  a
Eliminar  X  a
Visitando nodo  b
Insertar  ↓ b
Visitando nodo  c
Insertar  ↓ c
Visitando nodo  d
Insertar  ↓ d
Eliminar  X  d
Eliminar  X  c
Visitando nodo  f
Insertar  ↓ f
Visitando nodo  g
Insertar  ↓ g
Eliminar  X  g
Eliminar  X  f
Eliminar  X  b
Visitando nodo  e
Insertar  ↓ e
Eliminar  X  e

'''

# 
# Autor:  Yeimy Huanca
class Pila:
    def __init__(self):
        self.items = []
    
    def push(self, item): # insertar
        self.items.insert(0, item)
    
    def pop(self): # eliminar ultimo nodo
        return self.items.pop(0)
    
    def __str__(self):#imprimir
        print(self.items) 

    def isEmpty(self):
        if (self.items == []):
           return True
        else:
            return False 
            

class Nodo:
    def __init__(self, valorInicial):
        self.valorInicial = valorInicial
        self.visited = False
        self.vecinos = []
    
    def addCaminoA(self, node):
        self.vecinos.append(node)
    
    def getVecinos(self):
        return self.vecinos
    
    def getValor(self):
        return self.valorInicial
    
    def setVisited(self):
        self.visited = True
    
    def isVisited(self):
        return self.visited
    
    def __str__(self):
        return str(self.valorInicial)


def dfsIterativo(nodoaux):
    pila = Pila()
    print("Insertar  ↓" , nodoaux)
    pila.push(nodoaux)
    print("Visitando nodo ",nodoaux)
    nodoaux.setVisited()
    while not pila.isEmpty():
        i = pila.pop()
        print("Eliminar  X ",i)
        for j in i.getVecinos():
            if not j.isVisited():
                print("Visitando nodo ", j)
                j.setVisited()
                print("Insertar  ↓" , j)
                pila.push(j)

a = Nodo('a')
b = Nodo('b')
c = Nodo('c')
d = Nodo('d')
e = Nodo('e')
f = Nodo('f')
g = Nodo('g')

a.addCaminoA(b)    #a ⇔ b
a.addCaminoA(c)    #a ⇔ c
a.addCaminoA(d)    #a ⇔ d
b.addCaminoA(d)    #b ⇔ d
b.addCaminoA(c)    #b ⇔ c
b.addCaminoA(e)    #b ⇔ e
c.addCaminoA(f)    #c ⇔ f
c.addCaminoA(g)    #c ⇔ g
e.addCaminoA(f)    #e ⇔ f

dfsIterativo(a)
