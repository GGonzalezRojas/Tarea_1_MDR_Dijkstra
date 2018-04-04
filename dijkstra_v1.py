from collections import defaultdict
from heapq import heappop, heappush

def dijkstra(grafo, inicio, final):
    #Diccionario se utiliza para gestionar mejor la union de los nodos
    diccionario = defaultdict(list)
    #Para cada nodo obtenido de grafo, se almacena sus nodos unidos con sus respectivos costos
    for nodo, nodo_sgte, peso in grafo:
        diccionario[nodo].append((peso,nodo_sgte))
    #Se crea cola de prioridad ingresando el primer nodo
    cola = [(0,inicio,())]
    #Se crea una lista de elementos unicos que serán los visitados 
    visitado = set()
    #Mientras la cola exista se comienza a recorrer
    while cola:
        #Se extrae el ultimo valor de la cola separandolo en las variables mostradas
        (costo, parado, ruta) = heappop(cola)
        #Parado será igual al nodo en el que estamos parados, si este no fue visitado entonces se procede
        if parado not in visitado:
            #Como no fue visitado entonces se marca como visitado
            visitado.add(parado)
            #Ruta de recorrido será una tupla, que incorpora donde estoy parado y la ruta
            ruta = (parado, ruta)
            #Si parado es igual al final es por que llegue al final del grafo
            if parado == final: return (costo,ruta)
            
            #Para cada valor de nodo siguiente almacenado en diccionario
            for peso, parado_sgte in diccionario.get(parado,()):
                #Si nodo siguiente a donde estamos parados no fue visitado
                if parado_sgte not in visitado:
                    #Entonces se alamacena en la cola de prioridad mantiendo el mayor valor bajo el "árbol"
                    heappush(cola,(costo + peso, parado_sgte, ruta))

    return float("infinito")
if __name__ == "__main__":
    grafo = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11),
        ("G", "H", 5)
    ]

print(dijkstra(grafo,"A","H"))
     
