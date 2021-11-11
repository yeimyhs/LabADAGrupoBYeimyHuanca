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


def dfsRecursive(nodoaux):
    nodoaux.setVisited()
    print("Nodo visitado " , nodoaux)
    for n in nodoaux.getVecinos():
        if not n.isVisited():
            dfsRecursive(n)

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

dfsRecursive(a)
