from collections import deque, defaultdict
import csv
import ast

# Construir o grafo
def construir_grafo(filmes):
    grafo = defaultdict(list)
    for filme in filmes:
        for actor in filmes[filme]:
            grafo[filme].append(actor)
    
    # Realizando a conversão de um grafo direto para um indireto
    undirected_graph = {}

    for node, neighbors in grafo.items():
        for neighbor in neighbors:
            if node not in undirected_graph:
                undirected_graph[node] = []
            if neighbor not in undirected_graph:
                undirected_graph[neighbor] = []
            
            if neighbor not in undirected_graph[node]:
                undirected_graph[node].append(neighbor)
            if node not in undirected_graph[neighbor]:
                undirected_graph[neighbor].append(node)

    return undirected_graph


def generate_movie_actor_dict_from_file(file_path):
    movie_actor_dict = {}
    
    # Abrindo o arquivo csv
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            title = row['title']
            cast = ast.literal_eval(row['cast'])
            actor_names = [actor['name'] for actor in cast]
            movie_actor_dict[title] = actor_names
    
    return movie_actor_dict


def bfs(graph, start_actor, end_actor):
    if end_actor not in graph:
        raise ValueError('Esse ator não existe na base de dados')
    # mantém uma fila de caminhos a serem avaliados
    queue = []
    # coloca o primeiro caminho na fila
    # o primeiro caminho é só o primeiro ator
    queue.append([start_actor])
    while queue:
        # pega o primeiro caminho da fila
        path = queue.pop(0)
        
        # pega o ultimo node do caminho
        node = path[-1]
        # se o node for o ultimo ator, o caminho foi encontrado
        if node == end_actor:
            return path
        # se não, verifica e adiciona todos os outros possíveis caminhos
        # na fila para serem verificados
        
        for adjacent in graph.get(node):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
    return None

def renderizar_pesquisa(pesquisa):
    final_str = ""
    for i in enumerate(pesquisa):
        final_str += i[1]
        if  i[0] < len(pesquisa) - 1:
            if i[0] % 2 == 0:
                if i[0] > 1:
                    final_str += " que trabalhou em "
                else:
                    final_str += " trabalhou em "
            else:
                final_str += " junto com "
    return final_str


# Carregando o arquivo de filmes e construindo um dict filme:[atores]
dict_filme_ator = generate_movie_actor_dict_from_file('movies.csv')
# Contruindo o grafo indireto para os filmes e os atores
grafo = construir_grafo(dict_filme_ator)
# Realizando a Breadth First Search para encontrar o caminho mais curto entre dois atores no grafo
print(renderizar_pesquisa(bfs(grafo, 'Chris Evans', 'Keanu Reeves')))
print(renderizar_pesquisa(bfs(grafo, 'Henry Cavill', 'Willem Dafoe')))
print(renderizar_pesquisa(bfs(grafo, 'Jason Momoa', 'Will Smith')))
print(renderizar_pesquisa(bfs(grafo, 'Kevin Bacon', 'Gal Gadot')))
print(renderizar_pesquisa(bfs(grafo, 'Nicolas Cage', 'Adam Sandler')))
print(renderizar_pesquisa(bfs(grafo, 'Dwayne Johnson', 'Adam Sandler')))
print(renderizar_pesquisa(bfs(grafo, 'Jason Momoa', 'Terry Crews')))