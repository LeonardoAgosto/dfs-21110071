import networkx as nx
import matplotlib.pyplot as plt

def crearGrafo(levels):
    G = nx.Graph()
    node_count = 0
    nodes_by_level = []  # Lista para almacenar los nodos por nivel
    
    # Agregar nodos por niveles y guardar nodos en nodes_by_level
    for level in range(1, levels + 1):
        level_nodes = []
        for i in range(level):
            node_count += 1
            G.add_node(node_count, level=level)  # Agregar nodo con atributo de nivel
            level_nodes.append(node_count)
            #print(f"Nodo{node_count} en el nivel {level}")
        nodes_by_level.append(level_nodes)
    
    # Agregar aristas entre nodos consecutivos en los niveles
    for level in range(1, levels):
        current_level_nodes = nodes_by_level[level - 1]  # Nodos del nivel actual
        next_level_nodes = nodes_by_level[level]  # Nodos del siguiente nivel
        
        for i in range(len(current_level_nodes)):
            current_node = current_level_nodes[i]
            for next_node in next_level_nodes:
                G.add_edge(current_node, next_node)
                #print(f"Arista {current_node} y nodo {next_node}")
    
    return G

def dfsBuscarCamino(graph, start, goal):
    stack = [(start, [start])]
    
    while stack:
        (node, path) = stack.pop()
        for next_node in graph[node]:
            if next_node not in path:
                if next_node == goal:
                    return path + [next_node]
                else:
                    stack.append((next_node, path + [next_node]))

    return None  # Si no se encuentra un camino

# Este bloque de código se ejecuta solo si este script es el programa principal
if __name__ == "__main__":
    graph = crearGrafo(7)

    # Obtener la lista de aristas en el grafo
    edges = graph.edges()
    
    start_node = 7 # Nodo en el que iniciaremos
    goal_node = 28  # Nodo que deseamos llegar
    
    # Usando metodo para encontrar el camino corto
    shortest_path = dfsBuscarCamino(graph, start_node, goal_node)
    #shortest_path = None
    
    if shortest_path:
        print("Camino mas corto encontrado:", shortest_path)
        print("Longitud del camino:", len(shortest_path) - 1)  # Numero de aristas en el camino
        
        # Visualizar el grafo y resaltar el camino mas corto
        pos = nx.spring_layout(graph)  # Definir la disposición de los nodos para la visualización
        nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)  # Dibujar el grafo
        path_edges = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)]
        nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=2)  # Resaltar el camino más corto
        plt.title(f"Camino mas corto desde {start_node} a {goal_node}")
        plt.show()
    else:
        print("No se encontro un camino desde", start_node, "a", goal_node)
