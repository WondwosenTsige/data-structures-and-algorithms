from code_challenges.graph.graph import Graph, Vertex, Edge

def flights(Graph, city_list):

    weight = 0

    for index, city in enumerate(city_list):

        city_vertex = Vertex(city)
        city_neighbors = Graph.get_neighbor(city_vertex)
        next_city_vertex = Vertex([city_list[index+1]])

        found = False

        for edge in city_neighbors:
            if edge.vertex == next_city_vertex:
                weight += edge.weight
                found = True
                break
        if found == False:
            return False

    return True, weight
